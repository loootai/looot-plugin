---
name: recipes
description: "Step lists for common looot jobs. Use to enrich a lead list (find and verify work emails), research a company from its domain, check SEO and GEO (AI answer) visibility for a keyword, turn a web page into markdown, or look up a LinkedIn, TikTok or Instagram profile."
---

# looot recipes

Every recipe uses the same loop as the find-and-run skill. Before a job you have not run yet, search for it and read `jobInputs`: live input names win over the names below. If a job run answers `needs_input`, add the field it names, or inspect one endpoint and send its own fields. Give every run its own `idempotencyKey`. Tell the user the estimated total before a batch (money skill).

## Enrich a lead list: find and verify a work email

1. Quote it. Read `costPerSuccessUsd` for `people.email.find` and again for `people.email.verify`, multiply by the number of leads, and check `balance`:

```tool
search {"filters": {"capability": "people.email.find"}, "prefer": "cheapest"}
```

2. Find, one lead per run. Send `first_name` and `last_name` (or `name`) plus `domain`. `company` or `linkedin_url` also work:

```tool
run {"endpointId": "job:people.email.find", "input": {"first_name": "Patrick", "last_name": "Collison", "domain": "stripe.com"}, "idempotencyKey": "<list>-<row>-find", "fallback": {"maxAttempts": 3, "maxCostUsd": 0.1}}
```

3. Take `normalized.fields.email` (or read `result`). An `outcome: "weak"` with `verdict: "guessed"` is a pattern guess.
4. Verify every address you keep:

```tool
run {"endpointId": "job:people.email.verify", "input": {"email": "<email>"}, "idempotencyKey": "<list>-<row>-verify", "fallback": true}
```

5. Read `normalized.fields.status`: `valid`, `invalid`, `catch_all`, `risky` or `unknown`. Keep `valid`. Flag `catch_all` and `risky` for the user.
6. Run a few leads at a time. On `too_many_inflight_runs`, wait 2 seconds and retry with the same key. Then report found, verified and the total from `actualCost`.

## Account research from a domain

Run each with `{"domain": "<domain>"}` and fallback:

1. `job:company.enrich` gives name, industry and size (`normalized.fields`).
2. `job:company.technographics` lists the technologies the site runs.
3. `job:company.news` lists recent news. It also takes `company`.
4. `job:people.domain.search` lists known email addresses at the domain.
5. With the company's LinkedIn page, `job:linkedin.company.profile` takes `linkedin_url`.

```tool
run {"endpointId": "job:company.enrich", "input": {"domain": "stripe.com"}, "idempotencyKey": "<new unique key>", "fallback": {"maxAttempts": 2, "maxCostUsd": 0.1}}
```

Write one short brief: what the company does, its size, stack, recent news and contacts. Name the provider behind each fact (`servedProviderId`).

## SEO and GEO check for a keyword

1. Google results: `job:google.serp.organic` takes `query`, and optionally `location`, `language`, `country` and `device`:

```tool
run {"endpointId": "job:google.serp.organic", "input": {"query": "best crm for startups", "location": "United States"}, "idempotencyKey": "<new unique key>", "fallback": true}
```

2. AI answers (GEO): `google.serp.ai-mode`, `search.google-ai-overview` and `search.chatgpt`. Look for the user's brand and domain in each answer and in the sources it cites.
3. Search volume: `google.keywords.volume`. It is priced higher than a results page, so quote it first.
4. Domain strength: `backlinks.domain.summary`.
5. Steps 2 to 4 are jobs with one provider each. For each, find the endpoint, inspect it, and run the endpoint id with its own `requiredInputFields`:

```tool
search {"filters": {"capability": "search.chatgpt"}}
```

```tool
inspect {"endpointId": "<endpointId from that search>", "detail": "run"}
```

6. Report the domain's position in the results, whether each AI answer mentions or cites it, the volume, and the backlink totals.

## Web page to markdown

```tool
run {"endpointId": "job:web.scrape.markdown", "input": {"url": "https://example.com/pricing"}, "idempotencyKey": "<new unique key>", "fallback": {"maxAttempts": 3, "maxCostUsd": 0.05}}
```

Read `normalized.fields.markdown` and `title`. A blocked, empty or sign-in page is a `miss`, and fallback moves on to the next scraper. `web.scrape.structured` returns JSON instead.

## Social profile lookup

| Network | Job | Input |
|---|---|---|
| LinkedIn person | `job:linkedin.person.profile` | `linkedin_url` |
| LinkedIn company | `job:linkedin.company.profile` | `linkedin_url` |
| TikTok | `job:tiktok.user.profile` | `handle` (no @) |
| Instagram | `job:instagram.user.profile` | `handle` (no @) |

```tool
run {"endpointId": "job:tiktok.user.profile", "input": {"handle": "<handle>"}, "idempotencyKey": "<new unique key>", "fallback": true}
```

For another network, search for it ("x user profile", "youtube channel") and read `jobInputs`.
