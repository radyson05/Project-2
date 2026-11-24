# Data Card — Sentinel Allocation

**Purpose:** classify a monthly risk regime and estimate transparent portfolio risk.  
**As-of convention:** decision after market close on the final business day of month *t*; inputs must be available by that close; weights apply during *t+1*.  
**Frequency:** monthly.  
**Fields:** adjusted ETF prices/returns for SPY, VXUS, IEF, GLD, BIL; 12-month SPY return; 10-year minus 3-month Treasury-yield proxy; annualized return and volatility estimates.

**Proposed sources:** CRSP or issuer-adjusted prices, cross-checked against Yahoo Finance; FRED Treasury series DGS10 and TB3MS. Preserve source URLs, retrieval time, observation date, and transformation version before production use.

**Point-in-time handling:** lag all monthly inputs by one month; do not revise historical signals after a later data revision; retain the exact downloaded raw file and its hash. A defensive signal requires both negative 12-month SPY momentum and an inverted curve proxy.

**Included artifact:** the app uses disclosed deterministic teaching estimates as of 2026-11-22 so it runs offline. They are not a market-data claim or a backtest. Their use is limited to validating application flow, constraint logic, and the changed-input record.

**Known quality risks:** survivorship/vendor differences, adjusted-price methodology, Treasury-series release timing, stale ETF prices, and the Gaussian VaR assumption. Data-timestamp failure is a stop trigger.
