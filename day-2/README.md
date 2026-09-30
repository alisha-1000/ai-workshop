# Day 2 — Parallel Execution, Streaming, and Human-in-the-Loop

- **Time:** about 2 hours including homework
- **You will build:** a parallel fan-out graph, a streaming view of a bounded loop, and a human-in-the-loop review that pauses after every step
- **Know first:** bounded loops, routing, and structured output from Day 1
- **Not required yet:** code execution or multi-agent handoffs

## Start

From the workshop root:

```bash
source .venv/bin/activate
./workshop start
cd day-2/tutorial
jupyter lab
```

Open `day-2.ipynb` and use the workshop kernel.

## Follow this order

1. Build a fan-out graph where three specialists run in parallel, and give the shared key a reducer that merges their writes.
2. Build the bounded debug loop and run it with `stream()`; watch one update arrive as each node finishes.
3. Contrast `stream()` with `invoke()`, which returns only the final state.
4. Add the `human_review` node and predict how many times the graph pauses before you resume it.
5. Confirm the iteration limit still stops the loop even if every answer is `retry`.
6. Complete the review-and-revise graph in the [homework](exercise/README.md).

## What success looks like

- Three parallel nodes writing one key merge through a reducer instead of raising `InvalidUpdateError`.
- `stream(stream_mode="updates")` yields one chunk per node as it finishes; `invoke()` returns only the final state.
- The human-in-the-loop graph pauses after every step and resumes only after `Command(resume=...)`.
- The iteration limit still stops the loop even if every human answer is `retry`.
- The homework cannot revise more than twice.

## If you get stuck

For the parallel graph, give the shared key a reducer before wiring the fan-in. For streaming, print each chunk before adding the pause. Debug one mechanic at a time.

**Intentional failure:** drop the `Annotated[list, add]` reducer from the parallel graph and rerun to see `InvalidUpdateError`; separately, remove the checkpointer from the human-in-the-loop `compile()` and try to resume. Restore both.

**Exit check:** Why does a fan-in node need a reducer on any key its parents both write? Does streaming change what the graph computes, or only when the caller sees it? And which decisions belong to the human?
