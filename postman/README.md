# Post Lifecycle - Postman Collection

A Postman collection demonstrating a full CRUD lifecycle test flow against the JSONPlaceholder API.

## What it covers
- **CREATE** — POST a new post
- **GET/RETRIEVE** — fetch a post by ID
- **UPDATE** — PUT to update a post's fields
- **DELETE** — remove a post

## Tests included
- Status code validation for each request
- JSON schema validation on responses
- Field-level assertions (e.g., confirming a title update was applied)

## How to run

### Via Postman UI
Import both files into Postman, select the environment, and use the Collection Runner.

### Via Newman (CLI)
```bash
npm install -g newman
newman run lifecycle.json -e env.json
```

Example output: 4 requests, 7 assertions, 0 failures.

## Notes
JSONPlaceholder is a mock API — created/updated resources are not persisted, so some responses (e.g. GET after CREATE) return 404 by design.
