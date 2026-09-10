import json, sys, collections
def load(day):
    T=[]
    for l in open(f'/tmp/kalshi_raw/{day}.jsonl'):
        t=json.loads(l); T.append((t[0],t[1],t[2],float(t[3]),float(t[4])))
    return T
def orders(T):
    T.sort(key=lambda t:(t[0],t[2],t[1])); O=[]; cur=None
    for tk,ts,side,cnt,yp in T:
        if cur and cur[0]==tk and cur[1]==side and ts-cur[3]<=0.002: cur[4]+=cnt; cur[3]=ts
        else:
            if cur: O.append(cur)
            cur=[tk,side,ts,ts,cnt]
    if cur: O.append(cur)
    return O
buckets=[(0,0.1,'0-100ms'),(0.1,0.3,'100-300ms'),(0.3,1,'0.3-1s'),(1,3,'1-3s'),(3,1e9,'>3s')]
agg=collections.defaultdict(lambda: collections.defaultdict(float)); conc=collections.Counter()
for day in sys.argv[1:]:
    T=load(day)
    # concurrency: distinct tickers trading per 10-second bucket
    per=collections.defaultdict(set)
    for tk,ts,*_ in T: per[int(ts//10)].add(tk)
    conc.update(len(v) for v in per.values())
    O=orders(T); O.sort(key=lambda o:(o[0],o[1],o[2]))
    # bursts: same market+side, gap <=1s chains; keep chains with >=8 orders
    i=0
    while i<len(O):
        j=i
        while j+1<len(O) and O[j+1][0]==O[i][0] and O[j+1][1]==O[i][1] and O[j+1][2]-O[j][2]<=1.0: j+=1
        chain=O[i:j+1]
        if len(chain)>=8:
            t0=chain[0][2]
            for o in chain:
                off=o[2]-t0; shape='INT' if abs(o[4]-round(o[4]))<=0.005 else 'FRAC'
                for lo,hi,name in buckets:
                    if lo<=off<hi: agg[name][shape+'_n']+=o[4]; agg[name][shape+'_o']+=1; break
        i=j+1
print('distinct KXBTC15M tickers trading per 10 s bucket (bucket counts):', sorted(conc.items())[:6])
print(f"\nBurst position (chains of 8+ same-side taker orders, gaps <=1 s), pooled {len(sys.argv)-1} days")
print(f"{'offset':10s} {'orders':>8s} {'INT share orders':>16s} {'INT share contracts':>19s}")
for lo,hi,name in buckets:
    a=agg[name]; o=a['INT_o']+a['FRAC_o']; n=a['INT_n']+a['FRAC_n']
    if o: print(f"{name:10s} {o:8.0f} {100*a['INT_o']/o:15.1f}% {100*a['INT_n']/n:18.1f}%")
