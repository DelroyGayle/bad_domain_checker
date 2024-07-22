## Domain Checker

### Task

You are to build a service that allows other services to check if a list of domains are alive and
returning a valid website. This is crucial for our purposes, because showing a dead domain to our
clients would be a bad experience.

### Requirements

- The service should be available on demand.
- The service should be able to accept a list of domains to check.
- The service should be able to check if the domains are alive in the most impartial way possible,
  and return an informative response for each domain. Assume that the downstream services will want
  to know if the domain was alive, dead, or the check itself failed.
- The definition of a valid website is one that a reasonable user, when visiting the domain in
  a browser, would consider it to be valid.
- There is no upper limit to the number of domains that can be checked, but you as the designer
  can define that limit as long as its justified.
- You are free to propose any architecture as is appropriate for use by other services.
- Whenever a serialization protocol is required, JSON is preferred.
- A balance between latency and correctness should be considered.