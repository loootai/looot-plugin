---
name: find-and-run
description: "Find and run paid data APIs through looot (SEO and SERP data, keyword volume, backlinks, people and company enrichment, email finding and verification, social profiles, web scraping). Use whenever a task needs external or live data. Search by the job in plain words, read the job's inputs and coverage, run the job with fallback, then read who answered and what it cost."
---

# Find and run with looot

Tools: `search`, `inspect`, `run`, `runs_get`, `runs_list`, `runs_evidence`, `balance`. Searching and inspecting are free. `discover_smart` costs a small fee, so ask before you use it.

## 1. Search by the job, not the vendor

```tool
search {"query": "find a work email from a name and domain"}
```

You get 10 short rows. On each row:

- `endpointId` and `provider`.
- `capability` is the job id, such as `people.email.find`.
- `estimatedPrice` and `priceBasis`, plus `costPerSuccessUsd`, which is the price divided by the success rate.
- `works` holds `rate`, `runs` and `p50Ms`. `thin: true` means fewer than 5 runs back the rate.
- `access` is `runs_now`, `needs_your_account` (the user must connect their own account) or `coming_soon` (no key yet, do not pick it).

Top-level `jobInputs` lists each job's inputs with coverage, shaped `{"<job id>": {"<input>": {"endpoints": <how many take it>, "of": <endpoints in the job>}}}`. An input that more endpoints take gives fallback more providers to try.

To list one job's providers, pass its id as a filter. `prefer` orders the providers inside a job:

```tool
search {"filters": {"capability": "people.email.find"}, "prefer": "cheapest"}
```

`prefer` is `balanced` (the default), `cheapest`, `reliable` or `fastest`.

If `items` is empty and `warnings` holds `no_supply_for_job`, no endpoint does that job. Tell the user. `capability_request` asks looot to add it.

## 2. Run the job

Send `job:<job id>` with the shared input names from `jobInputs`. looot maps them to each provider's own fields and picks the first provider, in `prefer` order, that can run your input. Free providers go first.

```tool
run {"endpointId": "job:people.email.find", "input": {"first_name": "Patrick", "last_name": "Collison", "domain": "stripe.com"}, "idempotencyKey": "<new unique key>", "fallback": {"maxAttempts": 3, "maxCostUsd": 0.1, "prefer": "cheapest"}}
```

- `fallback`: on a miss, an error or a pattern guess, try the next provider of the same job inside one hold. Only attempts that ran are charged. `true` takes the defaults. The object takes `maxAttempts` (up to 10), `maxCostUsd`, `prefer`, `exclude` (endpoint ids) and `stopAtFirstMiss`.
- Without `fallback`, exactly one provider runs.
- `idempotencyKey`: make a new one for every new run. Sending the same key again returns the same run with `replayed: true` and never charges twice, so it is safe to retry after a dropped connection.
- `wait` is 20 seconds by default and 60 at most. If `status` is still `queued` or `running`, poll `runs_get` with the `runId`.

To call one exact provider instead, inspect it and send its own parameters:

```tool
inspect {"endpointId": "icypeas-email-verify", "detail": "run"}
```

That returns `requiredInputFields`, `inputSchema`, `estimatedMaxCost` and a `run` template. Replace its `<placeholders>` and use a new `idempotencyKey`.

## 3. Read the answer

Check `status` and `error` first. A call can succeed and still carry `status: "failed"`.

- `outcome` is `hit`, `weak`, `miss`, `error`, `rejected`, `skipped` or `pending`, and `outcomeReason` says why. A `weak` with `verdict: "guessed"` is a pattern guess: verify it before use.
- `result` is the provider's answer. `normalized` (only on some jobs, only when completed) has fixed field names: `fields`, `missing`, `verdict` and `mapVerified`. Email find gives `email` and `check`. Email verify gives `email`, `status` and `deliverable`. Company enrich gives `name`, `domain`, `industry` and `size`. Scrape to markdown gives `markdown` and `title`.
- `endpointId` is the provider the job picked. `servedEndpointId` and `servedProviderId` say who actually answered, which differs after a fallback.
- `requestedJob` (job runs only) has `job`, `prefer`, `pickedEndpointId`, `reason` and the rows it passed over in `skipped`.
- `route` (fallback runs only) has `servedBy`, `outcome`, `chargedUsd`, `capped`, each attempt with its outcome and charge, `skipped` and a `summary` such as "zerobounce: guessed ($0.01). hunter: found ($0.0245). Charged $0.0345."
- `actualCost` is what was charged. `estimatedCost` is what was held.

## 4. Receipts

```tool
runs_evidence {"runId": "<runId>"}
```

```tool
runs_list {"limit": 20}
```

Money rules: the money skill. Errors: the troubleshooting skill. Ready-made flows: the recipes skill.
