---
name: find-email
description: "Find and verify the work email of one person, or of every person in a list, through looot. Run it with a name and a company domain, a LinkedIn URL, or a file of leads."
---

# Find and verify a work email

Who to find: the details the user gave with the request

1. If the looot tools are missing or answer 401, follow the setup skill first.
2. Read the input. For one person you need `first_name` and `last_name` (or `name`) plus `domain`, or a `linkedin_url`. For a file, read every row and map its columns to those names. Ask the user only for what is missing.
3. Follow "Enrich a lead list" in the recipes skill: quote the total, check `balance`, run `job:people.email.find` with fallback, then `job:people.email.verify` on each address found.
4. Answer with a table: person, email, verification status (`valid`, `invalid`, `catch_all`, `risky` or `unknown`), the provider that answered (`servedProviderId`) and the cost (`actualCost`). Mark pattern guesses (`verdict: "guessed"`). End with the total spent.
