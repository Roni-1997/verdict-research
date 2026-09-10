import json, collections
d=json.load(open('/tmp/pm5m_fills_2026-09-09.json'))
day0=(min(t[5] for t in d)//86400)*86400; day1=day0+86400
W={}
for w,cid,side,size,price,ts,oi in d:
    a=W.setdefault(w,{'fills':0,'usd':0.0,'ts':[],'orders':{},'mk':collections.defaultdict(set),'buy':0.0,'sell':0.0})
    a['fills']+=1; a['usd']+=size*price; a['ts'].append(ts)
    o=a['orders'].setdefault((cid,side,ts,oi),[0.0,0.0]); o[0]+=size; o[1]+=size*price
    a['mk'][cid].add((side,oi)); a['buy' if side=='BUY' else 'sell']+=size*price
F={}
for w,a in W.items():
    ts=sorted(set(a['ts'])); gaps=[b-c for b,c in zip(ts[1:],ts[:-1])]+[(ts[0]-day0)+(day1-ts[-1])]
    maxgap=max(gaps)/3600; hours=len(set(t//3600 for t in ts))
    orders=list(a['orders'].values()); n=len(orders)
    buys=[(k,v) for k,v in a['orders'].items() if k[1]=='BUY']
    exact=sum(1 for k,v in buys if v[1]>=1 and abs(v[1]-round(v[1]))<0.0051)/max(len(buys),1)
    two=sum(1 for m in a['mk'].values() if ('BUY',0) in m and ('BUY',1) in m)/len(a['mk'])
    sizes=collections.Counter(round(v[0],2) for v in orders); modal=sizes.most_common(1)[0][1]/n
    F[w]={'fills':a['fills'],'orders':n,'usd':a['usd'],'maxgap':maxgap,'hours':hours,'windows':len(a['mk']),'exact':exact,'two':two,'modal':modal,'sellshare':a['sell']/a['usd'] if a['usd'] else 0}
tot=sum(f['usd'] for f in F.values())
def tier(f): return '<30' if f<30 else '30-99' if f<100 else '100-299' if f<300 else '300+'
print(f'wallets {len(F):,} taker $ {tot:,.0f}\n')
print('A. Does the wallet sleep? Longest gap between orders in the UTC day (wrap-around included). Share of tier $ / wallets')
print(f"{'tier':8s} {'wallets':>7s} {'$share':>7s} | {'gap>=8h $':>9s} {'6-8h $':>7s} {'3-6h $':>7s} {'<3h $':>7s} | {'gap>=8h w':>9s} {'<3h w':>7s} | {'median windows':>14s} {'median orders':>13s} {'median hrs':>10s}")
import statistics as st
for t in ['<30','30-99','100-299','300+']:
    fs=[f for f in F.values() if tier(f['fills'])==t]; u=sum(f['usd'] for f in fs)
    def sh(lo,hi): return 100*sum(f['usd'] for f in fs if lo<=f['maxgap']<hi)/u
    def shw(lo,hi): return 100*sum(1 for f in fs if lo<=f['maxgap']<hi)/len(fs)
    print(f"{t:8s} {len(fs):7d} {100*u/tot:6.1f}% | {sh(8,99):8.0f}% {sh(6,8):6.0f}% {sh(3,6):6.0f}% {sh(0,3):6.0f}% | {shw(8,99):8.0f}% {shw(0,3):6.0f}% | {st.median(f['windows'] for f in fs):14.0f} {st.median(f['orders'] for f in fs):13.0f} {st.median(f['hours'] for f in fs):10.0f}")
print('\nB. Inside the heavy band, cross the sleep gap with order denomination and two-sidedness (share of band $)')
for t in ['30-99','100-299']:
    fs=[f for f in F.values() if tier(f['fills'])==t]; u=sum(f['usd'] for f in fs)
    cells=collections.defaultdict(float); cw=collections.Counter()
    for f in fs:
        g='sleeps>=6h' if f['maxgap']>=6 else 'no sleep<6h'
        k='two-sided' if f['two']>=0.4 and f['windows']>=5 else ('dollar-typed' if f['exact']>=0.4 else 'share-typed')
        cells[(g,k)]+=f['usd']; cw[(g,k)]+=1
    print(f'  {t}:')
    for g in ('sleeps>=6h','no sleep<6h'):
        print('    '+g.ljust(12)+'  '+'  '.join(f"{k}: {100*cells[(g,k)]/u:4.0f}% $ ({cw[(g,k)]} w)" for k in ('dollar-typed','share-typed','two-sided')))
print('\nC. PnL sanity: median hours active and modal-size share by sleep class within heavy band')
for t in ['30-99','100-299']:
    for g,lo,hi in (('sleeps>=6h',6,99),('no sleep<6h',0,6)):
        fs=[f for f in F.values() if tier(f['fills'])==t and lo<=f['maxgap']<hi]
        if fs: print(f"  {t:8s} {g:12s} wallets {len(fs):5d}  median hours {st.median(f['hours'] for f in fs):4.0f}  median windows {st.median(f['windows'] for f in fs):4.0f}  median modal-size share {100*st.median(f['modal'] for f in fs):3.0f}%  median exact$ {100*st.median(f['exact'] for f in fs):3.0f}%  sells {100*sum(f['sellshare']*f['usd'] for f in fs)/sum(f['usd'] for f in fs):3.0f}%")
json.dump(F,open('/tmp/pm_wallet_features_2026-09-09.json','w'))
