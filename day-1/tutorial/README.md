# Day 1 Tutorial — Multi-State Routing and a Retry Loop

This is the completed code used in the recorded tutorial.

The running example is the 0/1-knapsack program from `RUNNING_EXAMPLE.md`. Its upward capacity loop looks plausible but silently reuses the current item.

## Video flow

1. Connect to the shared model gateway.
2. Define the triage and specialist prompts, and their structured-output schemas.
3. Share one typed state across every node.
4. Route to a single specialist with a conditional edge, then finalize.
5. Visualize and run the multi-state graph; confirm the running bug takes the `logic` route.
6. Break the `Literal` route contract in a copy and restore it.
7. Build a one-node bounded retry loop that reviews its previous attempts.
8. Run the retry loop on the same problem, then break its stopping condition in a copy and restore it.

From the workshop root:

```bash
source .venv/bin/activate
./workshop start
cd day-1/tutorial
jupyter lab
```

Open `day-1.ipynb` and run it from top to bottom. After watching the video, continue to the [homework](../exercise/README.md).

Select **Python 3.12 — Agentic AI Workshop** if prompted. Pause at each prediction cell before running the next cell. A successful lesson produces two graph images — the router and the retry loop — and debugger results for the same input.
