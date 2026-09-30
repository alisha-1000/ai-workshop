# Day 2 Tutorial — Parallel Execution, Streaming, and Human-in-the-Loop

This is the completed code used in the recorded tutorial. Day 1 ran graphs one node at a time; today we look at three ways execution differs. The running example is still the 0/1-knapsack bug.

## Quick start

From the workshop root:

```bash
source .venv/bin/activate
./workshop start
cd day-2/tutorial
jupyter lab
```

Open `day-2.ipynb`, select **Python 3.12 — Agentic AI Workshop**, and use the workshop kernel.

## Video flow

### Part 1 — Parallel execution
1. Build three specialist nodes that fan out from `START` and fan in at `finalize`.
2. Give the shared `diagnoses` key an `Annotated[list, add]` reducer so the three concurrent writes merge.
3. Run it, then break it by dropping the reducer to see `InvalidUpdateError`, and restore it.

### Part 2 — Streaming
4. Build a bounded self-loop and run it with `stream(stream_mode="updates")`.
5. Read each chunk as its node finishes, and contrast it with a single `invoke()`.

### Part 3 — Human-in-the-loop
6. Add a `human_review` node that pauses with `interrupt()`.
7. Resume the paused graph with `Command(resume=...)` after a human decides to retry or end.
8. Confirm the iteration limit still stops the loop even when the human keeps answering `retry`.

After watching the video, continue to the [homework](../exercise/README.md).

A successful lesson merges three parallel writes with a reducer, streams each step of the bounded loop as it finishes, and pauses for a human decision after every step in Part 3.
