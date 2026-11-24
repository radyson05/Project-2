# Executed Output Record

**Run date:** 2026-11-23  
**Application:** `app.py` Flask test client  
**Inputs:** `signal=risk_off`, `cap=0.06`, `cost=10` bps  
**Data as of:** 2026-11-22 (deterministic teaching inputs)

| Portfolio | Expected return | Volatility | 95% 1-month VaR | Mandate verdict |
| --- | ---: | ---: | ---: | --- |
| Equal weight | 6.50% | 6.98% | 2.78% | PASS — all limits met |
| 60/40-style transparent baseline | 6.92% | 7.83% | 3.15% | PASS — all limits met |
| Sentinel constrained portfolio | 5.86% | 5.56% | 2.16% | PASS — all limits met |

The local test client returned HTTP 200 for the default dashboard and for the risk-off stress case with `cap=0.04`; that stress case visibly contained `STOP PROCESS`. This record is visible executed output for the reproducible teaching-data version of the app.
