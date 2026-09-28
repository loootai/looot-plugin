---
name: research-company
description: "Write a short account brief on a company from its domain through looot, with its profile, tech stack, recent news and known contacts, each fact tied to the provider that returned it."
---

# Research a company

Company: the details the user gave with the request

1. If the looot tools are missing or answer 401, follow the setup skill first.
2. Reduce the input to a bare domain (`https://www.stripe.com/about` becomes `stripe.com`). If you only have a name, ask for the domain or search for it.
3. Follow "Account research from a domain" in the recipes skill. Say the estimated total before the first run. Skip any step the user does not need.
4. Answer with one brief: what the company does, size and industry, tech stack, the last few news items with dates, and contacts found. After each fact, name the provider (`servedProviderId`). End with the total spent (sum of `actualCost`).
