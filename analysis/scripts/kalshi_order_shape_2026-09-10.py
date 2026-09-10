import json, sys, collections, bisect
def load(day):
    T=[]
    for l in open(f'/tmp/kalshi_raw/{day}.jsonl'):
        t=json.loads(l); T.append((t[0],t[1],t[2],float(t[3]),float(t[4]),t[5],t[6]))
    return T
def orders(T):
    T.sort(key=lambda t:(t[0],t[2],t[1]))
    O=[]; cur=None
    for tk,ts,side,cnt,yp,cl,res in T:
        px = yp if side=='yes' else 1-yp
        if cur and cur['tk']==tk and cur['side']==side and ts-cur['ts_last']<=0.002:
            cur['n']+=cnt; cur['prem']+=cnt*px; cur['ts_last']=ts
        else:
            if cur: O.append(cur)
            cur={'tk':tk,'side':side,'ts':ts,'ts_last':ts,'n':cnt,'prem':cnt*px,'cl':cl,'res':res}
    if cur: O.append(cur)
    return O
def binsize(n): return '<=50' if n<=50 else '51-500' if n<=500 else '501-5000' if n<=5000 else '>5000'
def stats(O):
    A=collections.defaultdict(lambda: collections.defaultdict(float))
    # cross-market twin flag: another order in a different ticker within 1 ms
    O.sort(key=lambda o:o['ts']); ts=[o['ts'] for o in O]
    for i,o in enumerate(O):
        lo=bisect.bisect_left(ts,o['ts']-0.001); hi=bisect.bisect_right(ts,o['ts']+0.001)
        o['twin']=any(O[j]['tk']!=o['tk'] for j in range(lo,hi) if j!=i)
    for o in O:
        n=o['n']; px=o['prem']/n if n else 0
        frac = abs(n-round(n))>0.005
        shape='FRAC' if frac else 'INT'
        win = (o['side']==o['res']); pnl=(1-px)*n if win else -px*n; fee=0.07*px*(1-px)*n
        h=int((o['ts']%86400)//3600); us_eve = h>=20 or h<3
        for key in ((shape,'all'),(shape,binsize(n)),('ALL','all')):
            a=A[key]; a['orders']+=1; a['n']+=n; a['prem']+=o['prem']; a['pnl']+=pnl; a['fee']+=fee
            if o['cl']-o['ts']<=120: a['late2m_n']+=n
            if px<=0.10 or px>=0.90: a['ext_n']+=n
            if us_eve: a['useve_n']+=n
            if o['twin']: a['twin_n']+=n
            if n>=1 and abs(o['prem']-round(o['prem']))<0.0051: a['exact_n']+=n
            if not frac and n>=100 and round(n)%50==0: a['round50_n']+=n
    return A
tot=collections.defaultdict(lambda: collections.defaultdict(float))
for day in sys.argv[1:]:
    T=load(day); O=orders(T); A=stats(O)
    allc=A[('ALL','all')]['n']
    print(f"\n{day}: trades {len(T):,} orders {len(O):,} contracts {allc/1e6:.1f}M")
    print(f"{'shape':5s} {'bin':9s} {'orders%':>7s} {'contr%':>7s} {'pnl_pre':>8s} {'pnl_post':>8s} {'late2m':>7s} {'extreme':>7s} {'US eve':>7s} {'twin1ms':>7s} {'exact$':>7s} {'rnd50':>6s}")
    for shape in ('FRAC','INT'):
        for b in ('all','<=50','51-500','501-5000','>5000'):
            a=A[(shape,b)]
            if not a['n']: continue
            print(f"{shape:5s} {b:9s} {100*a['orders']/A[('ALL','all')]['orders']:6.1f}% {100*a['n']/allc:6.1f}% {100*a['pnl']/a['prem']:7.2f}% {100*(a['pnl']-a['fee'])/a['prem']:7.2f}% {100*a['late2m_n']/a['n']:6.0f}% {100*a['ext_n']/a['n']:6.0f}% {100*a['useve_n']/a['n']:6.0f}% {100*a['twin_n']/a['n']:6.0f}% {100*a['exact_n']/a['n']:6.0f}% {100*a['round50_n']/a['n']:5.0f}%")
    for k,a in A.items():
        for f,v in a.items(): tot[k][f]+=v
allc=tot[('ALL','all')]['n']
print(f"\nPOOLED {len(sys.argv)-1} days: orders {tot[('ALL','all')]['orders']:,.0f} contracts {allc/1e6:.1f}M")
print(f"{'shape':5s} {'bin':9s} {'orders%':>7s} {'contr%':>7s} {'pnl_pre':>8s} {'pnl_post':>8s} {'late2m':>7s} {'extreme':>7s} {'US eve':>7s} {'twin1ms':>7s} {'exact$':>7s} {'rnd50':>6s}")
for shape in ('FRAC','INT'):
    for b in ('all','<=50','51-500','501-5000','>5000'):
        a=tot[(shape,b)]
        if not a['n']: continue
        print(f"{shape:5s} {b:9s} {100*a['orders']/tot[('ALL','all')]['orders']:6.1f}% {100*a['n']/allc:6.1f}% {100*a['pnl']/a['prem']:7.2f}% {100*(a['pnl']-a['fee'])/a['prem']:7.2f}% {100*a['late2m_n']/a['n']:6.0f}% {100*a['ext_n']/a['n']:6.0f}% {100*a['useve_n']/a['n']:6.0f}% {100*a['twin_n']/a['n']:6.0f}% {100*a['exact_n']/a['n']:6.0f}% {100*a['round50_n']/a['n']:5.0f}%")
