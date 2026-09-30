#!/usr/bin/env python3
"""
Model endpoint mock & proxy server running on http://127.0.0.1:8317/v1
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import urllib.request
import sys

class ModelEndpointHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Suppress logging clutter

    def do_GET(self):
        if self.path in ("/v1/models", "/v1/models/"):
            response = {
                "object": "list",
                "data": [
                    {
                        "id": "gemini-3-flash",
                        "object": "model",
                        "created": 1700000000,
                        "owned_by": "workshop"
                    }
                ]
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path in ("/v1/chat/completions", "/v1/chat/completions/"):
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            try:
                req_data = json.loads(body.decode("utf-8"))
                req_data["model"] = "workshop-gemini"
                proxy_req = urllib.request.Request(
                    "http://127.0.0.1:5001/gateway/mlflow/v1/chat/completions",
                    data=json.dumps(req_data).encode("utf-8"),
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": "Bearer not-needed"
                    }
                )
                with urllib.request.urlopen(proxy_req) as resp:
                    resp_data = resp.read()
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(resp_data)
            except Exception:
                fallback = {
                    "id": "chatcmpl-mock",
                    "object": "chat.completion",
                    "created": 1700000000,
                    "model": "gemini-3-flash",
                    "choices": [
                        {
                            "index": 0,
                            "message": {
                                "role": "assistant",
                                "content": "Ready"
                            },
                            "finish_reason": "stop"
                        }
                    ]
                }
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(fallback).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

def run(port=8317):
    server_address = ("127.0.0.1", port)
    httpd = HTTPServer(server_address, ModelEndpointHandler)
    print(f"Model endpoint server running on http://127.0.0.1:{port}/v1")
    httpd.serve_forever()

if __name__ == "__main__":
    port = 8317
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    run(port)
