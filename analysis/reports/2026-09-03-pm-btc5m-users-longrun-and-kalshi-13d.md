# Polymarket BTC 5-minute markets: who trades them, Feb-Aug 2026 (wallet-level, full life of the product)

Data: every taker fill on every BTC 5m window for 34 sample days (one day every 6 days, all weekdays represented) from launch (Feb 12) to Aug 30 2026: 495k wallet-days, **221,220 unique taker wallets**, ~27M fills. Per wallet-day aggregates from the raw fills (kept gzipped: scratchpad/long/pm/raw). "Taker $" = one-sided dollars takers paid (Polymarket's headline volume is ~2x). Classes per day by activity shape: bot = >=300 fills/day or >=100 across >=16 hours; heavy = 30-299 fills/day; manual = <30. Personas per wallet over the period. Related: `~/verdict_pm_5m_flow_wallets_2026_09_03.md` (2-day deep dives, behaviour models).

## 1. The life of the product (sample days)
| period | taker $/day | wallets/day | new wallets/day | manual $/day | heavy $/day | bot $/day | manual PnL | bot PnL |
|---|---|---|---|---|---|---|---|---|
| Feb 13 (day 2) | $11.7M | 14,400 | 14,400 | $2.5M (21%) | $3.9M (33%) | $5.4M (46%) | -6.6% | +2.4% |
| Mar 3 (peak day) | $24.2M | 17,300 | 10,700 | $3.4M (14%) | $7.0M (29%) | $14.0M (58%) | -4.9% | +1.1% |
| Apr 8 (peak wallets) | $17.9M | 21,800 | 10,700 | $3.0M (17%) | $7.0M (39%) | $7.9M (44%) | -4.3% | +1.0% |
| May 2 (V2 cutover week) | $7.9M | 14,900 | 6,200 | $1.8M (23%) | $2.7M (34%) | $3.4M (43%) | -0.8% | +1.9% |
| Jun 25 | $14.7M | 14,000 | 4,900 | $1.6M (11%) | $4.5M (31%) | $8.4M (57%) | -5.7% | 0.0% |
| Jul 31 | $10.1M | 10,400 | 2,700 | $1.4M (14%) | $3.6M (36%) | $5.2M (51%) | +1.0% | +0.6% |
| Aug 30 | $6.2M | 7,500 | 2,100 | $0.7M (11%) | $1.9M (30%) | $3.7M (59%) | -1.1% | +1.5% |
Period averages: Feb-Apr manual $2.8M/day from 12,700 wallets/day, heavy $6.1M from 4,100, bots $8.6M from 1,070; Jul-Aug manual $1.15M from 7,500, heavy $3.1M from 2,400, bots $4.9M from 680. Manual PnL -4.1% -> -1.8%; bots +1.2-1.4% throughout.
- The product opened at full size: 14,400 wallets and $11.7M of taker $ on its second day, 55-58% of it bots by the second week.
- New-wallet inflow is the story of the decline: ~10,700 first-time wallets per sample day in March-April, 2,100-2,700 in August. Total wallets per day fell 21,800 -> 7,500; taker $ 24 -> 6M.
- Bot share of $ drifted 44-49% (Mar-Apr) to 56-61% (Aug) as humans left faster; the top-10 wallets' share went 26% (launch) -> 14% (May) -> 17% (Aug); top-100 53% -> 40% -> 51%.
- Manual wallets' exact-dollar orders: 18% (Feb-Mar), 5-6% (Apr), 52-59% (from May 2). The V2 exchange cutover (Apr 28) changed order entry to dollar amounts; behaviour signatures are otherwise stable.

## 2. Lifecycle and retention (all 221k wallets)
- 62% of wallets appear on one sample day only (14% of taker $); 23% on 2-3; 11% on 4-9; **3% on 10+ sample days and they hold 39% of taker $**.
- Manual: 172,815 wallets, 65% seen once, median span 0 days. Heavy: 41,324, 55% seen once. Bots: 7,081 wallets, 42% seen once, median 2 sample days: bots churn too, only more slowly.
- New-wallet retention: seen again ~6 days later 22%, ~12 days 15%, ~24 days 9%.
- Class is sticky: wallets with 3+ sample days spend 75% of days in their modal class; 81% of manual starters stay manual, 59% of heavy starters regress to manual, 35% of bot starters end up manual (scripts that get switched off).

## 3. Signatures by class (whole period, buy-$ weighted)
| class | exact-$ orders | one order/window | buys the favourite | sure-thing (>=85c) | last-60s | contrarian | both sides | sells | PnL/$ | avg order |
|---|---|---|---|---|---|---|---|---|---|---|
| manual | 35%* | 74% | 75% | 56% | 47% | 13% | 4% | 16% | -3.4% | $23.7 |
| heavy | 32%* | 61% | 70% | 45% | 33% | 15% | 9% | 21% | -0.8% | $19.6 |
| bot | 13% | 50% | 67% | 31% | 23% | 16% | 24% | 10% | +1.2% | $15.5 |
*period mix; post-V2 manual = 52-59%.

## 4. Personas (wallets seen on >=2 sample days: 83,322 wallets holding 86% of all taker $)
| persona | wallets | share of taker $ | fills/day | avg order | hours active | buys favourite | sure-thing | PnL/$ | Feb-Apr -> Jul-Aug share |
|---|---|---|---|---|---|---|---|---|---|
| 1 engine / HFT (>=300 fills/day or >=100 across 16h+) | 3,130 | **44%** | 329 | $13 | 17 | 67% | 15% | +1% | 46% -> 50% |
| 2 script runner (100-299 fills/day) | 4,780 | 13% | 140 | $13 | 9.5 | 59% | 11% | -1% | 12% -> 13% |
| 3 power user (30-99 fills/day) | 19,987 | **27%** | 49 | $18 | 8 | 66% | 14% | -1% | 26% -> 23% |
| 4a regular, momentum (<30/day, buys the side ahead) | 30,949 | 6% | 10 | $17 | 2.7 | 56% | 4% | -3% | 6% -> 6% |
| 4b sure-thing collector (>=60% of buys at 85c+) | 9,588 | 8% | 9 | **$50** | 3.5 | 99% | 89% | 0% | 9% -> 6% |
| 5 contrarian / longshot (>=50% against the move) | 12,388 | 1% | 7 | $13 | 2 | 6% | 0% | **-7%** | 1% -> 1% |
| 6 hedger / arb (both sides in >=40% of windows) | 2,500 | 1% | 24 | $9 | 2.4 | 46% | 7% | +4% | 0.5% -> 1% |
Plus 138k wallets seen once (14% of $): mostly regulars and contrarians who tried it and left.

## 5. What this says
- The paying customer base is personas 3-5: ~73k wallets over the period holding ~42% of taker $, losing 1-7%; the machines (1-2) are 8k wallets holding 57% and earning 1%. Persona 3 (power users, 30-99 fills a day, a third with dollar-shaped orders) is the volume engine among humans; 4a/4b are the retail core; 5 is the lottery.
- Retention is the whole problem: 9% of new wallets are still there a month later. The book shrank because the funnel of new wallets dried up (10.7k -> 2.1k per sample day), not because existing users stopped.
- Structural constants across seven months: the side-choice logic (buy the side already ahead), ~$15-25 average orders for everyone, bots earning 1-2%, humans losing 2-5%, the sure-thing collector at breakeven with the biggest tickets.
Scripts: scratchpad/long/pm_long.py (sampler + per-wallet-day aggregation), pm_users.py (categorisation).

# Kalshi KXBTC15M (BTC 15-minute), Jul 2 - Aug 31 2026: 13 sample days, every 5th day, all 96 windows each day
No account identities (centralized venue), so this is an order-level categorisation. Prints within 2ms on the same side of the same market = one taker order. ~27M prints total. Retention: the trades endpoint only serves markets settled in the last ~68 days, so the series cannot go back further.

## Series
| day | windows | prints | taker orders | contracts | premium | share of contracts by order size <=50 / 51-500 / 501-5k / >5k | taker PnL after fee | 20:00-03:00 UTC share |
|---|---|---|---|---|---|---|---|---|
| Jul 2 | 87 | 1.39M | 785k | 120M | $56M | 6 / 33 / 47 / 14 | -1.5% | 41% |
| Jul 7 | 96 | 1.34M | 773k | 116M | $55M | 6 / 32 / 48 / 14 | -3.0% | 39% |
| Jul 12 | 96 | 1.79M | 894k | 113M | $53M | 7 / 34 / 46 / 12 | -3.5% | 40% |
| Jul 17 | 96 | 2.19M | 1.09M | 151M | $70M | 7 / 34 / 45 / 13 | -3.8% | 37% |
| Jul 22 | 96 | 2.04M | 1.04M | 149M | $74M | 7 / 32 / 48 / 13 | -3.0% | 40% |
| Jul 27 | 96 | 2.13M | 1.20M | 161M | $76M | 7 / 32 / 49 / 12 | -2.2% | 41% |
| Aug 1 | 96 | 1.85M | 961k | 136M | $67M | 7 / 32 / 50 / 11 | -2.5% | 39% |
| Aug 6 | 87 | 1.92M | 1.12M | 172M | $80M | 6 / 30 / 49 / 15 | -2.8% | 41% |
| Aug 11 | 96 | 2.30M | 1.26M | 177M | $84M | 7 / 32 / 49 / 13 | -1.3% | 41% |
| Aug 16 | 96 | 2.22M | 1.17M | 153M | $75M | 7 / 33 / 48 / 12 | -3.0% | 41% |
| Aug 21 | 96 | 2.92M | 1.47M | 237M | $109M | 6 / 28 / 47 / 20 | -2.0% | 42% |
| Aug 26 | 96 | 2.55M | 1.24M | 193M | $92M | 6 / 27 / 48 / 19 | -1.5% | 40% |
| Aug 31 | 96 | 2.59M | 1.35M | 212M | $102M | 6 / 27 / 47 / 20 | -2.3% | 39% |
Averages: 1.10M taker orders/day, 161M contracts/day ($76M premium/day at an average 47c), 146 contracts per order; 73-77% of orders have fractional contract counts and 1.1-1.5% are exact-dollar premiums every day; 37-42% of contracts trade 20:00-03:00 UTC every day. Trend Jul→late Aug: contracts/day 125M → 198M, orders/day 885k → 1.31M, share from >5,000-contract orders 13% → 18%, taker PnL after fee -3.0% → -2.2%.

## Order-size classes (13-day contract-weighted averages)
| order size (contracts) | orders/day | share of contracts | avg price paid | PnL pre-fee | after fee | in last 2 min | at 35-65c | at extremes (<10c or >=90c) |
|---|---|---|---|---|---|---|---|---|
| <=50 | 728k | 7% | 0.45 | -1.1% | -3.8% | 9% | 38% | 21% |
| 51-500 | 311k | 31% | 0.45 | -0.7% | -3.2% | 12% | 33% | 28% |
| 501-5,000 | 62k | 48% | 0.48 | +0.1% | -2.0% | 18% | 30% | 34% |
| >5,000 | 2.4k | 14% | 0.51 | -0.4% | -2.0% | 31% | 23% | 50% |
Read: two thirds of orders are odd lots (<=50 contracts, $2-20) that carry 7% of contracts and lose 3.8% after fees - retail-shaped flow arriving through brokers and executed by software; 62k orders a day of 501-5,000 contracts carry half the market, break even before fees and lose the fee; the >5,000 tier (2,400 orders/day) buys late and at the extremes (31% in the last 2 min, 50% at <10c/>=90c) - MMs flattening and late "sure thing" size, feasible only with reduced fees. Composition, fee burden and intraday rhythm are essentially constant across the two months while volume grew 60%; the growth came in the middle and top tiers.
