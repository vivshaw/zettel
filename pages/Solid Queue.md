---
tags: Rails, ActiveJob
---

- a job queue backend for [[ActiveJob]]
- doesn't retry jobs automatically! if you want retries, you need to explicitly set a `retry_on` in your ActiveJob for that
- if you're running in dev and jobs aren't executing, try making sure you're running `rake solid_queue:start`