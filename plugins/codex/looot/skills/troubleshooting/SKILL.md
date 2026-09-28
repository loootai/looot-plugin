---
name: troubleshooting
description: "Fix a looot run or tool call that failed or came back empty. Use when a looot result carries needs_input, no_supply_for_job, no_runnable_provider, unknown_job, invalid_input, route_capped, route_no_fit, validation_error, insufficient_balance, idempotency_conflict, too_many_inflight_runs, forbidden, a 401, or outcome miss."
---

# looot troubleshooting

Every tool error has `code`, `message` (with the fix in it), `retryable` and `requestId`. A failed run also has `error` with `code`, `message`, `whoseError` (`customer`, `provider` or `gateway`), `retryable` and `retryHint`. For a `job:` refusal the exact reason is in `result.code`, while `error.code` reads `validation_error`.

Read `status`, `error` and `outcome` before anything else. A tool call that worked can still hold a failed run.

| Code | What it means | What to do |
|---|---|---|
| `needs_input` | No provider of the job accepts the input. `result.needs` lists each provider with the fields it needs. | Add one of the named fields, using the names in the search answer's `jobInputs`. Send it with a new `idempotencyKey`. |
| `no_supply_for_job` | No endpoint does this job. Search returns it as a warning with empty `items`. | Search again in other words or pick another job. If nothing fits, tell the user and offer `capability_request`. |
| `no_runnable_provider` | The job exists, but nothing can run for this workspace right now. | Retry later with a new `idempotencyKey`, or pick another job. |
| `unknown_job` | The `job:` id does not exist. The message suggests up to 3 close ids. | Use a suggested id, or take the `capability` from a search row. |
| `invalid_input` | The `email`, `url`, `domain` or `phone` value is broken (an email with no `@`, a url with no `https://`). $0. | Fix the value and use a new `idempotencyKey`. The same key replays the refusal. |
| `route_capped` | Every provider costs more than `fallback.maxCostUsd`. No provider was called. $0. | Raise `maxCostUsd` after telling the user the price, or drop the cap. |
| `route_no_fit` | Fallback had providers but none could take the input. $0. | Read `route.skipped` (`needs_identity` says "needs <field>") and add the field. |
| `validation_error` | An argument is wrong. The message names the field; `acceptedArguments` lists what the tool takes. | Fix the named field. Never guess argument names; read `inspect` or the tool schema. |
| `insufficient_balance` | Run `status: "blocked"`. The answer has `topUp.checkoutUrl` and a `message`. | Show the link, wait for payment, retry with a NEW `idempotencyKey`. |
| `top_up_amount_out_of_range` | The top-up is below the minimum. | Call `top_up` with at least `minimumUsd`, or without an amount. |
| `top_up_unavailable` | No payment link for this workspace. | Give the user the `dashboardUrl` from the answer. |
| `idempotency_conflict` | This key was already used with another input or endpoint. | New run, new key. To replay, send the same input. |
| `too_many_inflight_runs` | Too many runs in flight for this workspace. | Wait 2 seconds and retry with the same key. |
| `catalog_loading`, `storage_busy` | Short server-side wait. Nothing was charged. | Wait the seconds the message gives and retry with the same key. |
| `forbidden` | The sign-in or token lacks the `runs:execute` scope. | Sign in again and allow running, or create a token with that scope. |
| 401, tools missing | Not signed in, or the sign-in expired. | Use the setup skill. |

Other signs:

- `status: "completed"` with `outcome: "miss"`: the provider answered but found nothing, and it may still have charged. Run the job with `fallback` so the next provider tries.
- `outcome: "weak"`: a flagged answer, such as a catch-all email or a pattern guess (`verdict: "guessed"`). Verify it before use.
- `status: "queued"` or `"running"` after `run`: poll `runs_get` with the `runId`. Do not start a second run.
- A search row with `access: "coming_soon"` has no key yet and returns a `provider_error`. With `needs_your_account`, the user must connect their own account first.

Quote the `requestId` when the user contacts support.
