# Day 3 Tutorial — Graph Mechanics and Observability

This is the completed code used in the recorded tutorial. Today is a mechanics-and-observability lab: no new agent. We reuse the knapsack bug and a multi-state routing graph and study *how it runs and how to observe it*. (Parallel execution moved to Day 2.)

## Quick start

From the workshop root:

```bash
source .venv/bin/activate
./workshop start
cd day-3/tutorial
jupyter lab
```

Open `day-3.ipynb`, select **Python 3.12 — Agentic AI Workshop**, and keep MLflow open at [http://127.0.0.1:5001](http://127.0.0.1:5001). All runs today log to one experiment, `day-3-graph-mechanics`.

## Learning goals

By the end of the day you should be able to:

- Read a checkpoint: `values`, `next`, `config`, `metadata`, and `parent_config`.
- Use `get_state`, `get_state_history`, and `update_state` to inspect and amend a thread, including how a reducer merges an `update_state` write.
- Start a graph at a chosen node by seeding state with `update_state(as_node=...)` and continuing with `invoke(None)`.
- List, filter, and read every run in MLflow with `mlflow.search_traces` and the trace UI.
- Explain why one Human-in-the-Loop thread produces several MLflow traces.

## Video flow

### Part 1 — Checkpoints and state updates
1. Build a multi-state routing graph with a reduced `notes` key, then recompile it with a `MemorySaver` checkpointer and run it under a `thread_id`.
2. Read the latest snapshot with `get_state`, then the whole chain with `get_state_history` (newest first).
3. Amend the thread with `update_state(..., as_node=...)`; note the new checkpoint and that the reduced key was appended, not replaced.

### Part 2 — Start at a particular node
4. Seed `category="logic"` with `update_state(as_node="triage")` so `get_state(...).next` becomes `('logic',)`.
5. Continue with `invoke(None)` — the graph enters the logic specialist directly and never calls the triage model.

### Part 3 — See all run data in MLflow
6. Build Simple Retry (Day 1), Multi-State routing (Day 1), and Human-in-the-Loop (Day 2) inline.
7. Run all three (HITL is resumed programmatically), tagging each trace with its `agent` name.
8. List every run with `mlflow.search_traces(experiment_ids=[...])`, then filter `tags.agent = 'hitl'` to see that one thread produced several traces.

## Threads span traces

The Day 2 human-in-the-loop graph pauses with `interrupt()` and resumes with `Command(resume=...)`, and every `invoke()` — the first call and each resume — creates its own MLflow trace, so a two-decision run produces three traces, not one. MLflow has no concept of the `thread_id` that ties them together unless you tag them yourself. LangGraph's checkpointer does: `get_state_history(config)` returns one snapshot per graph step. That checkpoint history lives only in the running process — restart the kernel and it is gone, while the MLflow traces remain.

## Reference

- [LangGraph persistence, checkpoints, and threads](https://docs.langchain.com/oss/python/langgraph/persistence)
- [MLflow LangGraph tracing](https://mlflow.org/docs/latest/genai/tracing/integrations/listing/langgraph/)
- [MLflow trace search and UI](https://mlflow.org/docs/latest/genai/tracing/observe-with-traces/ui/)
