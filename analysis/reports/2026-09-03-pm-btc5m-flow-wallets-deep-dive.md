# Who trades Polymarket's BTC 5-minute markets - wallet-level read (Sep 1-2 2026 UTC)

Data: Polymarket data-api `/trades` for 576 BTC 5m markets (series 10684) ending Sep 1-2 UTC; taker legs (default `takerOnly=true`, 973k fills, 530 markets with fills) and both legs (`takerOnly=false`, 2.92M records) to identify makers. Premium = shares x price. PnL-to-settlement per fill from the resolved outcome. Wallet classes by behaviour: high-frequency bot = >=300 taker fills/day or >=100/day across >=16 hours; sniper = >=50% of fills in the last 60s; semi-pro = >=30 fills/day; retail-like = the rest.

## Headline
- Taker premium $16.5M over 2 days ($8.2M/day) from 10,862 taker wallets. PM's reported "volume" for the same markets is $32.3M: **PM volume counts both legs, ~2x taker premium.**
- **Concentration:** top 10 takers = 25.5% of taker premium, top 50 = 48.7%, top 100 = 59.5%, top 500 = 81.8%.
- **By class:** high-frequency bots 593 wallets = 65.5% of taker premium (+1.5% PnL to settlement per $); semi-pro/scripted 1,954 wallets = 20.8% (-1.9%); retail-like 8,193 wallets = 10.6% (-4.9%); late-window snipers 122 wallets = 3.1% (+0.1%).
- **Fill sizes:** median $5, p90 $35, p99 $183; fills >= $1,000 are 9% of premium. Premium is flat across the 5 minutes (23/17/19/24/18% by minute).
- **What the top takers do:** the top 10 buy BOTH Up and Down in 87-100% of the windows they touch (two exceptions are directional whales with $1k median fills, 0-6% both-sides, one at -4.4%), average pair cost 0.92-1.04, 24h/day, 500 activity records in 0.2-1.5 hours, exclusively crypto up/down markets, portfolio values $400-$47k. Market-neutral over the window, positive edge per fill (+1.7% to +4.6%): latency-driven picking of stale quotes on whichever side lags the reference, not directional betting.
- **Maker side:** $17.1M maker premium across 3,723 wallets; top 10 makers = 32.5%, top 50 = 60.7%. 39% of maker premium comes from wallets that are also top-200 taker bots; 21 of the top 50 makers also take >$10k; **22% of all premium is bot-vs-bot** (top-200 bot taker hitting a top-200 bot maker). Self-trades (same wallet both legs) 0.00%. Retail takers get filled by bot makers 35% of the time; bot takers 43%.

## Top 10 takers (2 days)
Wallet-level table (addresses, display names, per-wallet PnL) removed from the published copy; it is held internally. Aggregate reading of the top 10 is in the Headline section above.

## Implications for Verdict
1. The 5m "demand" is mostly machines farming stale quotes; real retail is ~10% of taker premium and loses ~5%. A tight book on a slower reference feed will be farmed the same way - the reference/oracle latency and the maker's reprice speed are the product, not the incentives.
2. Taker rewards would be paid ~90% to bots. Points for takers must be capped per address and weighted toward non-bot behaviour (few fills, larger sizes, directional), or they are a bot subsidy.
3. Maker-fill rewards weighted by adverse selection pay exactly the fills these bots inflict; the 22% bot-vs-bot share and the 39% "makers who are also takers" mean the same firms sit on both sides - expect the same wallets on HL.
4. PM's headline 5m volume ($14.4M/day in Aug) is ~2x one-sided premium; compare like with like when sizing.
Scripts: scratchpad/pmflow/{pull.py, analyze.py}; data: taker.jsonl, both.jsonl, markets.json, top_takers.json.

## Kalshi KXBTC15M taker prints (24 markets sampled across Sep 2, 594k trades, 50.5M contracts ≈ 2.1M per market)
No identities (centralized venue; `/markets/trades` gives count, yes price, taker side, time). Behavioural read:
- Taker trade size: median 15 contracts, p75 56, p90 190, p99 1,000; trades >= 1,000 contracts = 27% of volume; trades <= 100 contracts = 20%.
- Price the taker pays: <10c 19% · 10-35c 18% · 35-65c 26% · 65-90c 16% · >=90c 22%. Volume rises through the window (minute 13-14 = 25%); last 60s = 11%.
- Fee burden at the published schedule ≈ 1.8% of taker premium overall (3.5% on mid-price trades, ~0.05% on last-minute >=90c buys). Taker PnL to settlement −1.6% before fees, **−3.4% after fees**: Kalshi's 15m takers lose as a class. Consistent with Whelan et al. (takers −32% Kalshi-wide over longer horizons).
- Interpretation: small odd-lot trades = Robinhood/app retail betting near the money and paying the full fee; the >=1,000-contract trades (27%) are the professional layer - MMs rebalancing and late-window "sure thing" buyers exploiting the parabolic fee (near zero at 95c+). MMs do not hedge by taking on Kalshi at 3.5%; they hedge on CME/Coinbase.

### Kalshi KXBTC15M - parent-order reconstruction (12 markets, Sep 2; prints within 2ms same side = one order)
302k prints -> 161k taker orders; ~15 taker orders/second, ~2,400 contracts/second while a market is open. 75% of orders have fractional contract counts, only 1.3% are round-dollar premiums and 9% round contract counts -> sizes are computed, not typed. By count small (median 21 contracts ≈ $7), by volume large: orders of 501-5,000 contracts = 47% of contracts, >5,000 = 20%, <=50 = 6%.
| order size | orders | share of contracts | avg px | PnL/prem pre-fee | after fee | in last 2 min | at mid 35-65c | at extremes |
|---|---|---|---|---|---|---|---|---|
| <=50 | 108k | 6% | 0.47 | -1.5% | -4.0% | 11% | 33% | 22% |
| 51-500 | 44k | 27% | 0.46 | -1.4% | -3.7% | 15% | 29% | 30% |
| 501-5,000 | 9.2k | 47% | 0.49 | -0.2% | -2.1% | 22% | 25% | 38% |
| >5,000 | 449 | 20% | 0.62 | -3.5% | -4.5% | 47% | 18% | 57% |
Read: every size class loses to settlement after the published fee, so the takers are not fee-paying arbitrageurs; the large late-window orders at extremes (>5,000 contracts, 47% in the last 2 minutes, 57% at extremes) look like designated MMs rebalancing/flattening with waived fees plus late "sure-thing" size; the small fractional odd-lot orders at ~15/second look machine-generated (API/broker-routed dollar orders and scripts), not app clicks. Hour-of-day still shows a 2:1 US-evening/overnight rhythm (human-timed demand behind the machines). Identity split retail vs systematic is not observable on Kalshi.

## The retail flow itself (8,193 retail-like PM wallets, Sep 1-2)
$1.75M taker premium / 93.8k fills; median fill $4, p90 $31; 84% have a self-set display name (humans). BUY 81% of premium (Up 49% / Down 51% - no direction bias), SELL-to-exit 19%. One side per window in 96% of wallet-windows (no hedging). Direction vs the previous window's result: 49% same / 51% opposite - no momentum or reversal logic, coin flips. Median 3 windows per active day, p90 13 (sessions). Premium by minute 22/12/17/24/24 (early bet + late "sure thing"). Price bands of BUYs: >=90c 40% of premium (win 94%, PnL -0.4%/$: the cheapest mistake), 65-90c 20% (-5.0%), 35-65c 29% (-10.1%), 10-35c 9% (-9.8%), <10c 2% (-68%). 59% of wallets negative to settlement; median wallet -5.7%. Hour-of-day flat-ish, mild 08-16 UTC (Europe/Asia daytime) tilt - PM's crypto-native audience, not US evening.
Archetypes: (1) the sure-thing buyer - 40% of retail premium buys 90-99c contracts near the close for a "guaranteed" 1-5% and loses only when the last seconds reverse; (2) the coin-flip bettor - 29% at mid-price, loses the spread plus adverse selection, ~-10%; (3) the longshot - 11% at <35c, loses 10-68%; (4) the short-session player - 3 windows a day, both directions, no system. Retail is not dumb HFT: it is small, named, one-sided, un-hedged, un-patterned human betting; the systematic layer sits above it.

### Website vs API test (orders = same wallet/market/side/second)
| class | wallets | BUY orders at a round-dollar premium | round share counts | orders in the first 2s of the window | wallet-windows with a single fill |
|---|---|---|---|---|---|
| retail-like | 8,193 | **51%** ($1 most common, then $5, $2, $3, $4, $10, $20, $25, $100) | 16% | 9% | 75% |
| semi-pro | 2,076 | **51%** | 17% | 8% | 61% |
| bots | 593 | 17% | 24% | 3.5% | 41% (24% have 5+ fills) |
Read: the retail AND semi-pro classes place dollar-denominated orders through the website/app (quick-buy buttons and typed amounts), one order per window, no fixed-offset timing; the API signature (share-denominated sizes, sweeps, fixed offsets) is confined to the bot class. So ~30% of taker premium is website humans, not scripts; "semi-pro" are heavy human users, not bots.

### Human strategies (retail + semi-pro wallets, by dominant behaviour)
| archetype | wallets | share of human premium | win rate | PnL/$ | windows/day |
|---|---|---|---|---|---|
| mixed | 2,398 | 34% | 65% | -3.0% | 8.5 |
| coin-flipper (buys at 35-65c) | 3,363 | 30% | 48% | -4.5% | 5.0 |
| sure-thing collector (>=85c in the last 2 min) | 1,078 | 24% | 90% | -0.0% | 4.0 |
| trend-leaner (65-85c) | 1,353 | 7% | 68% | -0.7% | 3.0 |
| longshot buyer (<35c) | 1,871 | 6% | 24% | -4.5% | 3.0 |
65% of human buy premium goes WITH the intra-window move (buying the side already above 55c), 19% at the open before any move, 11% contrarian. No martingale: next bet after a loss = 1.00x vs 1.00x after a win (4,915 wallets with >=6 windows). Same-window exits (19% of premium) are 69% profit-taking / 31% stop-loss. Everyone loses to settlement except the sure-thing collectors (~0, before fees); the human book is a -3% to -5% game funded by hope, and 65% of it is momentum-chasing.

## Decoded human behaviour (model-based; scripts: pmflow/decode.py; 304k human orders, 10,269 wallets, $5.67M premium)
Features per order from the reconstructed tape: current Up price, move since open, 30s momentum, time left, previous window result, own last result / streak / session count / P&L so far.
1. **Side choice** = follow the state of the window. P(bet Up) is 32% when the Up price is <0.35 and 67% when >0.65; logit slope on the current Up price 2.3 (pseudo-R2 0.07); 30-second momentum, the previous window's result and the bettor's own last result have zero effect. 69% of buy premium is placed after the window is already >=15c from 50/50.
2. **Timing** = wait for the move, then join it. 31% of buy premium is in the last 2 minutes at moves >0.40 (the sure thing); 8.5% at the open before any move.
3. **Sizing** (within-wallet OLS): bets on the favourite are 44% larger (t=105); after a loss +4.6% (t=14); streak and session length ~0. Mild loss-chasing, no martingale.
4. **Continuation**: after a loss 47% play the immediately next window vs 40% after a win (79% vs 76% within 30 min).
5. **Exits**: rare (3-8% of positions); P(sell) 7.6% in a big loss vs 5.8% in a big gain at 60s after entry -> mild loss-cutting; most ride to settlement.
6. **Edge**: markout +0.7pp at 30-60s (momentum continues briefly) but -3.1% to settlement; by entry time: open -3.9%, 2-4 min -3.7%, 1-2 min -1.9%, 30-60s -1.7%, last 30s -5.4%. Bots: +2.2pp at 60s, +1.6% to settlement.
7. **Clusters** (k-means, k=6, silhouette 0.22): grinders 1,049 wallets / 31% of human premium (48 orders/day, 17 of 24 hours, $4.6 median, 71% with-move, -1%; 43% round-dollar -> heavy or semi-automated); sure-thing collectors 1,100 / 27% (78% at >=0.85, 97% with-move, $7.7, -2%); with-move casuals 2,619 / 17% (9 orders/day, -4%, 66% round-dollar); contrarians 1,755 / 10% (77% against the move, -7%, worst); late snipers 501 / 10% (94% in last 60s, 26% round-dollar -> likely scripted, -1%); hedgers 681 / 5% (57% both sides, -4%).
8. **Persistence**: 4,266 wallets active both days; corr(day-1, day-2 return) = 0.08 (no skill); day-1 losers return 50% vs winners 66%; returning losers bet 0.74x day-1 size, winners 0.88x (no cross-day chasing, churn of losers).
Composition of human premium: manual (clusters with 49-66% round-dollar orders, 8-18 orders/day) ~59%; heavy/semi-automated (grinders, snipers) ~41%. So of ALL taker premium: ~18% manual humans, ~13% heavy/semi-automated humans, ~69% bots.

## Peak month vs now, 5m vs 15m (same pipeline; Apr 14-15 = peak month for both series in the Mar-Aug window)
| Product / period | Headline vol/day | Taker premium/day | Taker wallets (2d) | Manual humans | Heavy humans | Bots | Top-10 takers | Maker legs by bots |
|---|---|---|---|---|---|---|---|---|
| BTC 5m, Apr 14-15 | $32.5M | $15.8M | 28,425 | 18% (21,507 w, -3.8%) | 35% (5,463 w, -1.3%) | 48% (1,455 w, +2.1%) | 13% | 78% |
| BTC 5m, Sep 1-2 | $16.2M | $8.2M | 10,862 | 11% (8,193 w, -4.9%) | 24% (2,076 w, -1.6%) | 66% (593 w, +1.5%) | 25% | 86% |
| BTC 15m, Apr 14-15 | $6.6M | $3.2M | 9,090 | 31% (7,774 w, -1.4%) | 24% (1,102 w, +0.3%) | 45% (214 w, +2.1%) | 22% | 74% |
| BTC 15m, Sep 1-2 | $2.5M | $1.3M | 3,321 | 26% (2,859 w, -0.7%) | 21% (348 w, -0.8%) | 53% (114 w, +2.8%) | 31% | 72% |
Per $1M of headline volume, humans (both legs): 5m April ≈ $370k, 5m now ≈ $220k; 15m April ≈ $400k, 15m now ≈ $370k.
Reading: the April peak was human-driven - 5m had 53% human taker premium and 21,500 manual wallets in two days (2.6x today), the bot count was 2.5x today's but their share was lower; since then humans left faster than bots (manual wallets -62%, bots -59%, bot share 48%→66%, top-10 concentration 13%→25%). 15m is the more human product in both periods (55%→47% human) and humans roughly break even there (-1.4% → -0.7%); on 5m they lose 3-5%.
Behaviour is identical across all four samples: side-choice logit slope on the current Up price 2.25-2.57 with momentum/previous window/own result ≈0; favourites bet 44-66% larger; +4.6-6.3% size after a loss; immediate replay 47-50% after a loss vs 40-46% after a win; exits 3-8%; day-to-day return correlation 0.08-0.09 (15m Apr -0.20, n=486). Timing PnL: on 5m the open is worst (-3.9% now, -5.2% in April) and the last 30s went from -0.8% (April) to -5.4% (now) - the sure-thing trade got crowded by sniper bots; on 15m the 1-2-minutes-left entry is the only human timing that is positive (+1.1% April, +8.2% now on small n).
