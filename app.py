"""Sentinel Allocation — a self-contained educational committee dashboard."""
from flask import Flask, render_template, request

app = Flask(__name__)
AS_OF = "2026-11-22"
ASSETS = {
    "SPY": {"name": "U.S. equity", "return": .108, "vol": .185}, "VXUS": {"name": "International equity", "return": .072, "vol": .205},
    "IEF": {"name": "U.S. Treasury", "return": .041, "vol": .075}, "GLD": {"name": "Gold", "return": .064, "vol": .160}, "BIL": {"name": "Treasury bills", "return": .045, "vol": .008},
}
CORR = {"SPY": 0, "VXUS": .18, "IEF": -.06, "GLD": .04, "BIL": -.08}
def metrics(w, cost):
    ret = sum(w[k]*ASSETS[k]["return"] for k in ASSETS)-cost/10000
    variance = sum((w[k]*ASSETS[k]["vol"])**2 for k in ASSETS)+sum(2*w["SPY"]*w[k]*ASSETS["SPY"]["vol"]*ASSETS[k]["vol"]*CORR[k] for k in ASSETS if k != "SPY")
    vol = variance**.5
    return {"return": ret, "vol": vol, "var": max(0, 1.65*vol/(12**.5)-ret/12)}
def verdict(w, m, cap):
    f=[]
    if w["BIL"] < .10: f.append("cash/T-bill floor below 10%")
    if max(w.values()) > .45: f.append("single-position cap above 45%")
    if w["SPY"]+w["VXUS"] > .60: f.append("equity sleeve cap above 60%")
    if m["var"] > cap: f.append("one-month 95% VaR above the limit")
    return {"status":"PASS" if not f else "FAIL", "rule":"All mandate limits met" if not f else "; ".join(f)}
def portfolios(signal, cap, cost):
    equal={k:.2 for k in ASSETS}; balanced={"SPY":.30,"VXUS":.20,"IEF":.25,"GLD":.10,"BIL":.15}
    sentinel={"risk_off":{"SPY":.15,"VXUS":.10,"IEF":.35,"GLD":.20,"BIL":.20},"neutral":{"SPY":.25,"VXUS":.15,"IEF":.30,"GLD":.15,"BIL":.15},"risk_on":{"SPY":.35,"VXUS":.20,"IEF":.20,"GLD":.10,"BIL":.15}}[signal]
    out=[]
    for n,w in [("Equal weight",equal),("60/40-style transparent baseline",balanced),("Sentinel constrained portfolio",sentinel)]:
        m=metrics(w,cost); out.append({"name":n,"weights":w,"metrics":m,"verdict":verdict(w,m,cap)})
    return out
@app.route("/")
def index():
    signal=request.args.get("signal","risk_off"); cap=float(request.args.get("cap",.06)); cost=float(request.args.get("cost",10))
    return render_template("index.html",as_of=AS_OF,portfolios=portfolios(signal,cap,cost),signal=signal,cap=cap,cost=cost,stop=signal=="risk_off" and cap<.045)
if __name__ == "__main__": app.run(debug=True)
