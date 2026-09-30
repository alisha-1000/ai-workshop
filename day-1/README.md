# Day 1 — Multi-State Routing and a Bounded Retry Loop

- **Time:** 2–2.5 hours including homework
- **You will build:** a multi-state routing debugger and a bounded retry debugger
- **Know first:** state, nodes, and edges from Day 0
- **Not required yet:** executable tools, streaming, or human review

## Start

From the workshop root:

```bash
source .venv/bin/activate
./workshop start
cd day-1/tutorial
jupyter lab
```

Open `day-1.ipynb` and use the workshop kernel.

## Follow this order

1. Build the triage-and-route graph in the [tutorial](tutorial/README.md): one `triage` node classifies the bug and a deterministic router sends it to exactly one specialist.
2. Confirm that a single run visits triage, one specialist, and finalize.
3. Build the bounded retry loop: one node that reviews its own previous attempts and stops on a deterministic rule.
4. Compare the two shapes on the same knapsack bug.
5. Complete the [checkpoint homework](exercise/README.md) with a different problem.

## What success looks like

- Structured triage can return only a defined category.
- The router reads state and makes no model call.
- One routing run visits triage, one specialist, and finalize.
- In the retry loop, history is appended rather than replaced.
- Deterministic code prevents more than the allowed number of iterations.

## If you get stuck

Test the router — and the retry stopping rule — with a small hand-written state before invoking the graph. Do not debug model output and graph wiring at the same time.

**Intentional failure:** in a copy, return an undefined route from `route_bug`, inspect the error, and restore the `Literal` contract; separately, remove the iteration guard from `simple_route`, explain the risk, and restore it.

**Exit check:** Which decisions belong to the model, and which belong to deterministic code? If the model never sets `solved` to true, who stops the loop?
