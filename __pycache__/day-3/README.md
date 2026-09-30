# Day 3 — Graph Mechanics and Observability

- **Time:** about 2 hours including homework
- **You will explore:** checkpoint and state internals, entering a graph mid-way, and reading every run in MLflow
- **Know first:** the Simple Retry graph (Day 1), Multi-State routing (Day 1), and the Human-in-the-Loop graph (Day 2)
- **Not required yet:** LLM-as-judge or executable verification

## Start

From the workshop root:

```bash
source .venv/bin/activate
./workshop start
cd day-3/tutorial
jupyter lab
```

Open `day-3.ipynb` and keep [MLflow](http://127.0.0.1:5001) open in another browser tab.

## Follow this order

1. **Part 1 — Checkpoints and state updates.** Inspect what a checkpointer stores with `get_state`, `get_state_history`, and `update_state`.
2. **Part 2 — Enter at a specific node.** Seed a thread's state and start the graph at a chosen node with `invoke(None)` instead of `START`.
3. **Part 3 — All runs in MLflow.** Run Simple Retry, Multi-State, and Human-in-the-Loop, tag their traces, and list them all with `mlflow.search_traces`.
4. Complete the mechanics homework in [evaluation-lab.ipynb](exercise/evaluation-lab.ipynb) and record results with the [submission guide](exercise/README.md).

(Parallel execution moved to Day 2.)

## What success looks like

- `get_state_history` shows one checkpoint per superstep, newest first, each with a parent pointer.
- `update_state` adds a new checkpoint and, on a reduced key, appends rather than replaces.
- A seeded thread's `get_state(...).next` names the node you are about to enter, and `invoke(None)` runs only from there.
- `mlflow.search_traces` lists every run; the HITL thread shows several traces while Simple Retry and Multi-State show one each.

## If you get stuck

Print `get_state(config)` and `list(get_state_history(config))` before reasoning about a thread. Trace status `OK` means the run finished, not that the answer is correct.

**Exit check:** Why does an append-only checkpoint history survive edits and replays more safely than mutating state in place? And why does one HITL thread produce several traces?
