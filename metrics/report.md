# Agent metrics

Read from the sessions stored on this branch. Nothing here is recorded specially: every number is something the agents already wrote down while working.

Generated 2026-11-28.

A session appears in a dated window only if it recorded when its runs ended. Sessions from before run recording existed are counted under All time alone, so the dated windows are thinner than the project was — that gap closes as new sessions arrive, not by anything changing here.

## Runs

| window | runs | gave up | median seconds | longest | median round trips | median seconds each |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Last 7 days | 2 | 0% | 3,201 | 3,201 | 20 | 160.1 |
| Last 30 days | 2 | 0% | 3,201 | 3,201 | 20 | 160.1 |
| Last year | 2 | 0% | 3,201 | 3,201 | 20 | 160.1 |
| All time | 2 | 0% | 3,201 | 3,201 | 20 | 160.1 |

**Gave up** is every ending that is not `completed` — a ceiling reached, a person asking, a provider hanging up, a loop cut short. Each one is a mechanism deciding the run should not continue, which is worth watching whether or not it was right.

What is left over is not the same as work delivered. `completed` is the core saying its own loop ended rather than being stopped — it says nothing about whether the run produced a report. **Ran to an end without a report**, in each window below, is that question asked separately.

| ended because | runs |
| --- | ---: |
| `completed` | 2 |

## Last 7 days

2 sessions.

**Ran to an end without a report:** 1 of 2 sessions whose last run the core recorded as `completed` — 50%. These are not runs that gave up: nothing stopped them, they simply ended without writing a closing line, so the work is in a saved session and nowhere a person or the next agent reads.

**1,027,355 tokens** over 1 run that reported them, **98.1% of it prompt** — what the agents were made to read, not what they wrote. Anything spent on making runs cheaper belongs on that side. No money here, deliberately: of the four providers only one reports a cost, and a price table goes quietly stale and then prints confident wrong numbers.

**91.5% of that prompt was served from cache**, over the runs whose provider reported it. A cached prompt token costs a fraction of a fresh one, so this is most of what separates the counts above from the bill — and it is the figure that moves when what gets resent changes.

| | p50 | p90 | p99 | max | total |
| --- | ---: | ---: | ---: | ---: | ---: |
| tokens per run | 1,027,355 | 1,027,355 | 1,027,355 | 1,027,355 | 1,027,355 |
| messages per session | 75 | 75 | 75 | 75 | 134 |

| agent | sessions | share |
| --- | ---: | ---: |
| `atomaton` | 1 | 50% |
| `reviewer` | 1 | 50% |

**Refused** is the machinery saying no — a denylist, an allowlist, a hook. A guard working is not a tool breaking, and a reader cannot act on the two the same way, so they are counted apart. **Failed** is everything else that came back as an error, by string match, so it is an estimate.

| tool | calls | failed | refused | failure rate |
| --- | ---: | ---: | ---: | ---: |
| `read` | 23 | 0 | 0 | 0% |
| `fetch` | 15 | 1 | 0 | 6.7% |
| `bash` | 14 | 1 | 3 | 7.1% |
| `grep` | 10 | 0 | 0 | 0% |
| `list` | 6 | 0 | 0 | 0% |
| `commit_and_push` | 2 | 1 | 0 | 50% |
| `write` | 2 | 0 | 0 | 0% |
| `check_merge_readiness` | 1 | 0 | 0 | 0% |
| `create_pr` | 1 | 0 | 0 | 0% |
| `edit` | 1 | 0 | 0 | 0% |
| `get_branch` | 1 | 0 | 0 | 0% |
| `get_check_runs` | 1 | 0 | 0 | 0% |
| `get_issue_comments` | 1 | 0 | 0 | 0% |
| `get_pr` | 1 | 0 | 0 | 0% |
| `get_pr_reviews` | 1 | 0 | 0 | 0% |
| `glob` | 1 | 0 | 0 | 0% |
| `search_remote_code` | 1 | 1 | 0 | 100% |

What the agents do when they reach for a shell. `search` without a matching `open` is the shape that produced this project's most expensive runs; `edit` against `verify` is the shape that turned out not to occur at all.

| act | calls | share |
| --- | ---: | ---: |
| `other` | 11 | 78.6% |
| `edit` | 1 | 7.1% |
| `open` | 1 | 7.1% |
| `verify` | 1 | 7.1% |

No skill recorded.

## Last 30 days

2 sessions.

**Ran to an end without a report:** 1 of 2 sessions whose last run the core recorded as `completed` — 50%. These are not runs that gave up: nothing stopped them, they simply ended without writing a closing line, so the work is in a saved session and nowhere a person or the next agent reads.

**1,027,355 tokens** over 1 run that reported them, **98.1% of it prompt** — what the agents were made to read, not what they wrote. Anything spent on making runs cheaper belongs on that side. No money here, deliberately: of the four providers only one reports a cost, and a price table goes quietly stale and then prints confident wrong numbers.

**91.5% of that prompt was served from cache**, over the runs whose provider reported it. A cached prompt token costs a fraction of a fresh one, so this is most of what separates the counts above from the bill — and it is the figure that moves when what gets resent changes.

| | p50 | p90 | p99 | max | total |
| --- | ---: | ---: | ---: | ---: | ---: |
| tokens per run | 1,027,355 | 1,027,355 | 1,027,355 | 1,027,355 | 1,027,355 |
| messages per session | 75 | 75 | 75 | 75 | 134 |

| agent | sessions | share |
| --- | ---: | ---: |
| `atomaton` | 1 | 50% |
| `reviewer` | 1 | 50% |

**Refused** is the machinery saying no — a denylist, an allowlist, a hook. A guard working is not a tool breaking, and a reader cannot act on the two the same way, so they are counted apart. **Failed** is everything else that came back as an error, by string match, so it is an estimate.

| tool | calls | failed | refused | failure rate |
| --- | ---: | ---: | ---: | ---: |
| `read` | 23 | 0 | 0 | 0% |
| `fetch` | 15 | 1 | 0 | 6.7% |
| `bash` | 14 | 1 | 3 | 7.1% |
| `grep` | 10 | 0 | 0 | 0% |
| `list` | 6 | 0 | 0 | 0% |
| `commit_and_push` | 2 | 1 | 0 | 50% |
| `write` | 2 | 0 | 0 | 0% |
| `check_merge_readiness` | 1 | 0 | 0 | 0% |
| `create_pr` | 1 | 0 | 0 | 0% |
| `edit` | 1 | 0 | 0 | 0% |
| `get_branch` | 1 | 0 | 0 | 0% |
| `get_check_runs` | 1 | 0 | 0 | 0% |
| `get_issue_comments` | 1 | 0 | 0 | 0% |
| `get_pr` | 1 | 0 | 0 | 0% |
| `get_pr_reviews` | 1 | 0 | 0 | 0% |
| `glob` | 1 | 0 | 0 | 0% |
| `search_remote_code` | 1 | 1 | 0 | 100% |

What the agents do when they reach for a shell. `search` without a matching `open` is the shape that produced this project's most expensive runs; `edit` against `verify` is the shape that turned out not to occur at all.

| act | calls | share |
| --- | ---: | ---: |
| `other` | 11 | 78.6% |
| `edit` | 1 | 7.1% |
| `open` | 1 | 7.1% |
| `verify` | 1 | 7.1% |

No skill recorded.

## Last year

2 sessions.

**Ran to an end without a report:** 1 of 2 sessions whose last run the core recorded as `completed` — 50%. These are not runs that gave up: nothing stopped them, they simply ended without writing a closing line, so the work is in a saved session and nowhere a person or the next agent reads.

**1,027,355 tokens** over 1 run that reported them, **98.1% of it prompt** — what the agents were made to read, not what they wrote. Anything spent on making runs cheaper belongs on that side. No money here, deliberately: of the four providers only one reports a cost, and a price table goes quietly stale and then prints confident wrong numbers.

**91.5% of that prompt was served from cache**, over the runs whose provider reported it. A cached prompt token costs a fraction of a fresh one, so this is most of what separates the counts above from the bill — and it is the figure that moves when what gets resent changes.

| | p50 | p90 | p99 | max | total |
| --- | ---: | ---: | ---: | ---: | ---: |
| tokens per run | 1,027,355 | 1,027,355 | 1,027,355 | 1,027,355 | 1,027,355 |
| messages per session | 75 | 75 | 75 | 75 | 134 |

| agent | sessions | share |
| --- | ---: | ---: |
| `atomaton` | 1 | 50% |
| `reviewer` | 1 | 50% |

**Refused** is the machinery saying no — a denylist, an allowlist, a hook. A guard working is not a tool breaking, and a reader cannot act on the two the same way, so they are counted apart. **Failed** is everything else that came back as an error, by string match, so it is an estimate.

| tool | calls | failed | refused | failure rate |
| --- | ---: | ---: | ---: | ---: |
| `read` | 23 | 0 | 0 | 0% |
| `fetch` | 15 | 1 | 0 | 6.7% |
| `bash` | 14 | 1 | 3 | 7.1% |
| `grep` | 10 | 0 | 0 | 0% |
| `list` | 6 | 0 | 0 | 0% |
| `commit_and_push` | 2 | 1 | 0 | 50% |
| `write` | 2 | 0 | 0 | 0% |
| `check_merge_readiness` | 1 | 0 | 0 | 0% |
| `create_pr` | 1 | 0 | 0 | 0% |
| `edit` | 1 | 0 | 0 | 0% |
| `get_branch` | 1 | 0 | 0 | 0% |
| `get_check_runs` | 1 | 0 | 0 | 0% |
| `get_issue_comments` | 1 | 0 | 0 | 0% |
| `get_pr` | 1 | 0 | 0 | 0% |
| `get_pr_reviews` | 1 | 0 | 0 | 0% |
| `glob` | 1 | 0 | 0 | 0% |
| `search_remote_code` | 1 | 1 | 0 | 100% |

What the agents do when they reach for a shell. `search` without a matching `open` is the shape that produced this project's most expensive runs; `edit` against `verify` is the shape that turned out not to occur at all.

| act | calls | share |
| --- | ---: | ---: |
| `other` | 11 | 78.6% |
| `edit` | 1 | 7.1% |
| `open` | 1 | 7.1% |
| `verify` | 1 | 7.1% |

No skill recorded.

## All time

2 sessions.

**Ran to an end without a report:** 1 of 2 sessions whose last run the core recorded as `completed` — 50%. These are not runs that gave up: nothing stopped them, they simply ended without writing a closing line, so the work is in a saved session and nowhere a person or the next agent reads.

**1,027,355 tokens** over 1 run that reported them, **98.1% of it prompt** — what the agents were made to read, not what they wrote. Anything spent on making runs cheaper belongs on that side. No money here, deliberately: of the four providers only one reports a cost, and a price table goes quietly stale and then prints confident wrong numbers.

**91.5% of that prompt was served from cache**, over the runs whose provider reported it. A cached prompt token costs a fraction of a fresh one, so this is most of what separates the counts above from the bill — and it is the figure that moves when what gets resent changes.

| | p50 | p90 | p99 | max | total |
| --- | ---: | ---: | ---: | ---: | ---: |
| tokens per run | 1,027,355 | 1,027,355 | 1,027,355 | 1,027,355 | 1,027,355 |
| messages per session | 75 | 75 | 75 | 75 | 134 |

| agent | sessions | share |
| --- | ---: | ---: |
| `atomaton` | 1 | 50% |
| `reviewer` | 1 | 50% |

**Refused** is the machinery saying no — a denylist, an allowlist, a hook. A guard working is not a tool breaking, and a reader cannot act on the two the same way, so they are counted apart. **Failed** is everything else that came back as an error, by string match, so it is an estimate.

| tool | calls | failed | refused | failure rate |
| --- | ---: | ---: | ---: | ---: |
| `read` | 23 | 0 | 0 | 0% |
| `fetch` | 15 | 1 | 0 | 6.7% |
| `bash` | 14 | 1 | 3 | 7.1% |
| `grep` | 10 | 0 | 0 | 0% |
| `list` | 6 | 0 | 0 | 0% |
| `commit_and_push` | 2 | 1 | 0 | 50% |
| `write` | 2 | 0 | 0 | 0% |
| `check_merge_readiness` | 1 | 0 | 0 | 0% |
| `create_pr` | 1 | 0 | 0 | 0% |
| `edit` | 1 | 0 | 0 | 0% |
| `get_branch` | 1 | 0 | 0 | 0% |
| `get_check_runs` | 1 | 0 | 0 | 0% |
| `get_issue_comments` | 1 | 0 | 0 | 0% |
| `get_pr` | 1 | 0 | 0 | 0% |
| `get_pr_reviews` | 1 | 0 | 0 | 0% |
| `glob` | 1 | 0 | 0 | 0% |
| `search_remote_code` | 1 | 1 | 0 | 100% |

What the agents do when they reach for a shell. `search` without a matching `open` is the shape that produced this project's most expensive runs; `edit` against `verify` is the shape that turned out not to occur at all.

| act | calls | share |
| --- | ---: | ---: |
| `other` | 11 | 78.6% |
| `edit` | 1 | 7.1% |
| `open` | 1 | 7.1% |
| `verify` | 1 | 7.1% |

No skill recorded.

## Degraded answers

A tool can answer and report that it answered badly — a search that came back unranked, a log that went nowhere. The call succeeded, so it is neither a failure nor a refusal, and it is easy for one of these to run for months with nobody reading it. **Read `last seen` before `reports`**: an old count is a fixed fault. That date is when the session file was last written, which is the run that touched it last and not necessarily the run that reported the problem — so it errs recent.

Nothing reported a problem alongside an answer.

## Never used

Over all time, because something used once a year is still used. Each of these sits in the prompt of every run and returns nothing.

Every declared server has been called at least once.

Skills never loaded:

- `agent-prompt-surface`
- `customer-doc`
- `environment`
- `gh-actions-surface`
- `japanese`
- `on-demand-audit`
- `pipeline-setup`
- `secrets-in-a-check`
- `web-search`
