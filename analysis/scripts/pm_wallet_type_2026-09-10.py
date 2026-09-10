import json, urllib.request, hashlib, time, collections, sys
d=json.load(open('/tmp/pm5m_fills_2026-09-09.json'))
W=collections.defaultdict(lambda: {'fills':0,'usd':0.0,'hours':set(),'bo':collections.defaultdict(float)})
for w,cid,side,size,price,ts,oi in d:
    a=W[w]; a['fills']+=1; a['usd']+=size*price; a['hours'].add(ts//3600)
    if side=='BUY': a['bo'][(cid,ts,oi)]+=size*price
wallets=sorted(W)
print('wallets',len(wallets),file=sys.stderr)
RPCS=['https://polygon-bor-rpc.publicnode.com','https://polygon-rpc.com','https://1rpc.io/matic','https://polygon.drpc.org']
def batch_code(addrs, rpc):
    payload=[{'jsonrpc':'2.0','id':i,'method':'eth_getCode','params':[a,'latest']} for i,a in enumerate(addrs)]
    req=urllib.request.Request(rpc, data=json.dumps(payload).encode(), headers={'content-type':'application/json','user-agent':'curl/8'})
    with urllib.request.urlopen(req, timeout=60) as r: res=json.load(r)
    if isinstance(res,dict): raise Exception(str(res)[:200])
    return {addrs[it['id']]:it['result'] for it in res if 'result' in it}
try: code=json.load(open('/tmp/pm5m_wallet_code_2026-09-09.json'))
except Exception: code={}
todo=[w for w in wallets if w not in code]
B=100; ri=0; i=0; fails=0
while i < len(todo):
    chunk=todo[i:i+B]
    try:
        out=batch_code(chunk, RPCS[ri%len(RPCS)])
        if len(out)<len(chunk): raise Exception('partial %d/%d'%(len(out),len(chunk)))
        code.update(out); i+=B; fails=0
    except Exception as e:
        fails+=1; ri+=1; print('err',RPCS[(ri-1)%len(RPCS)],str(e)[:120],file=sys.stderr); time.sleep(1.5)
        if fails>24: break
    if i and i%1000==0: print('done',i,file=sys.stderr)
json.dump(code,open('/tmp/pm5m_wallet_code_2026-09-09.json','w'))
print('coded',len(code),'of',len(wallets),file=sys.stderr)
def cls(c):
    if c in ('0x','',None): return 'EOA'
    if 'a619486e' in c: return 'SAFE'
    if c.startswith('0x363d3d373d3d3d363d73'): return 'EIP1167:'+c[22:62]
    return 'OTHER:'+hashlib.sha256(c.encode()).hexdigest()[:10]
clusters=collections.Counter(cls(code.get(w)) for w in wallets if w in code)
print('\nclusters (wallets):'); 
for k,v in clusters.most_common(12):
    ex=next(w for w in wallets if w in code and cls(code[w])==k)
    print(f'  {k:60s} {v:6d}  e.g. {ex}  codelen={len(code[ex])}')
def tier(f): return '<30' if f<30 else '30-99' if f<100 else '100-299' if f<300 else '300+'
def typ(w):
    k=cls(code.get(w)) if w in code else 'UNK'
    return k if k in ('EOA','SAFE','UNK') else 'PROXY'
T=collections.defaultdict(lambda: collections.defaultdict(lambda: {'w':0,'usd':0.0,'exact':0,'buys':0,'ws':0,'h16':0}))
tot=sum(a['usd'] for a in W.values())
for w,a in W.items():
    t=tier(a['fills']); y=typ(w); c=T[t][y]
    c['w']+=1; c['usd']+=a['usd']
    ex=sum(1 for p in a['bo'].values() if p>=1 and abs(p-round(p))<0.0051); n=len(a['bo'])
    c['exact']+=ex; c['buys']+=n
    if n>=3 and ex/n>=0.4: c['ws']+=1
    if len(a['hours'])>=16: c['h16']+=1
print(f'\ntotal taker $ {tot:,.0f}')
print(f"{'tier':8s} {'type':6s} {'wallets':>7s} {'$share':>7s} {'$/wallet':>9s} {'exact$ buys':>11s} {'ws-sig wallets':>14s} {'16h+ wallets':>12s}")
for t in ['<30','30-99','100-299','300+']:
    for y in ['EOA','SAFE','PROXY','UNK']:
        c=T[t][y]
        if not c['w']: continue
        print(f"{t:8s} {y:6s} {c['w']:7d} {100*c['usd']/tot:6.1f}% {c['usd']/c['w']:9,.0f} {100*c['exact']/max(c['buys'],1):10.0f}% {100*c['ws']/c['w']:13.0f}% {100*c['h16']/c['w']:11.0f}%")
print('\nby type overall:')
for y in ['EOA','SAFE','PROXY','UNK']:
    w=sum(T[t][y]['w'] for t in T); u=sum(T[t][y]['usd'] for t in T)
    if w: print(f"  {y:6s} wallets {w:6d} ({100*w/len(wallets):.1f}%)  taker $ {100*u/tot:.1f}%")
