# Validation and AI Use Record

> **AI disclosure:** I used ChatGPT/Codex for brainstorming the interface, drafting code, and editing documentation. I reviewed the logic and own the analysis and decision. **Education only; not investment advice.**

**Student:** Ross Dyson  
**Project:** Project 2 — Investment Management Application  
**Analysis as of:** 2026-11-22

## Named AI tools and checks

| Tool | Used for | Human check |
| --- | --- | --- |
| ChatGPT / Codex | UI/code scaffold, document structure, editing | I read the Python allocation and constraint rules, recalculated weights, and checked each UI claim against `app.py`. |

One AI suggestion was qualified: a raw “risk-off” label should not itself imply an allocation recommendation. I retained the signal only as an input and added explicit mandate verdicts, stop conditions, and a pilot-only recommendation.

## Validation runs

| Test | Expected result | Observed result | Status |
| --- | --- | --- | --- |
| Default risk-off | Sentinel weights total 100% and pass mandate | [record after run] | Pending |
| Cost stress, 100 bps | Expected return declines by 0.90 percentage points vs 10 bps | [record after run] | Pending |
| Constraint stress | Risk-off plus VaR cap below 4.5% triggers stop | [record after run] | Pending |
| Baseline check | Both baselines show their own independent verdict | [record after run] | Pending |

## Locked Changed-Input Record — commit this section *before* running

**Status:** TEMPLATE — replace bracketed fields, make a Git commit, then execute without AI assistance.

**Required order:** enter the prediction below in your own words, commit and push this file to GitHub, copy the resulting commit link and timestamp into the table, then run the stress test. Do not alter the prediction after seeing the result.

| Field | Locked entry |
| --- | --- |
| Analyst-authored prediction (AI off) | Tightening the VaR limit from 6.0% to 4.0% while the signal remains risk-off will cause the application to show “STOP PROCESS,” because the documented stop condition is below 4.5%. |
| Exact changed input | `cap`: old `0.06`; new `0.04`; `signal`: unchanged `risk_off`; `cost`: unchanged `10` bps |
| Expected output direction | No proposed allocation should be treated as validated; the stop alert becomes visible. |
| Expected decision effect | Pilot is paused and escalated; committee does not force a rebalance. |
| Prediction timestamp | [YYYY-MM-DD HH:MM timezone] |
| Pre-run Git commit | [paste commit SHA and GitHub link] |
| AI status for prediction/run | AI off for prediction and execution; AI was not consulted between commit and result. |

