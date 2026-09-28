---
name: money
description: "How looot charges. Use before a paid run or a batch of runs, when the user asks what something will cost, sets a budget, runs out of credit, or wants receipts. Covers quotes, holds, what is refused for free, the fallback.maxCostUsd cap, top-ups and where receipts live."
---

# Money in looot

The workspace has a prepaid USD balance. Runs spend it. Searching, `inspect`, `catalog_overview`, `balance` and the run history are free. `discover_smart` is a paid search (well under a cent per call), so ask first.

## Quote before you run

- A search row has `estimatedPrice`, `priceBasis` (per call, or per result) and `costPerSuccessUsd` (the price divided by the success rate, the better number for comparing providers).
- `inspect` gives the exact price formula in `endpoint.price` and `estimatedMaxCost`, the most one run can hold:

```tool
inspect {"endpointId": "<endpointId>", "detail": "run"}
```

For a batch, multiply `costPerSuccessUsd` by the row count, tell the user the total, and check `balance` before you start. Get the user's go-ahead when the total is more than they expect to spend.

## Holds and settlement

1. A run first holds its estimated cost. It shows in `balance` as `reserved` and in `holds`.
2. The provider answers and the run settles at the real charge (`actualCost`).
3. The rest of the hold goes back to `available`.

A fallback run takes one hold for the whole route. It covers the first `maxAttempts` providers, and never more than `fallback.maxCostUsd`. Only attempts that ran are charged, and `route.chargedUsd` is their sum.

## Refused for free

These never reach a provider and charge $0: an input that fails the basic check (`invalid_input`, such as an email with no `@`), `needs_input`, `unknown_job`, `no_supply_for_job`, `no_runnable_provider`, any `validation_error`, and a route that called nobody (`route_capped`, `route_no_fit`, "No provider was called, so nothing was charged."). Provider errors, 402s and rejected calls are not charged either.

A "not found" answer can be charged, because some providers bill every call. In a job run, free providers go first, and a provider that only bills a found result moves ahead of paid ones that hold at least as much. `route.summary` shows each attempt's charge.

## The cost cap

`fallback.maxCostUsd` caps the route's hold:

```tool
run {"endpointId": "job:company.enrich", "input": {"domain": "stripe.com"}, "idempotencyKey": "<new unique key>", "fallback": {"maxAttempts": 2, "maxCostUsd": 0.05}}
```

A provider priced above what is left of the cap is skipped as `over_cost_cap`. If every provider is over it, the run fails as `route_capped` and charges nothing. One caveat: a route that can only run one provider settles like a direct run, so a provider that bills by volume can charge up to 3 times its estimate.

## Out of credit

A run with too little balance comes back `status: "blocked"`, code `insufficient_balance`, with `topUp.checkoutUrl` (a Stripe page) and a `message` to show the user. Show the link, wait for the payment, then retry with a NEW `idempotencyKey`. To get a link before that happens:

```tool
top_up
```

## Receipts

- `actualCost` on the run, and `route.summary` with the exact charge per attempt, such as "Charged $0.0287.".
- Every attempt with its status, the provider's own status, latency, receipt id and cost:

```tool
runs_evidence {"runId": "<runId>"}
```

- History, newest first, with `servedEndpointId` and `actualCost` on each row. Pass `nextCursor` back as `cursor` for the next page:

```tool
runs_list {"status": "completed", "limit": 50}
```
