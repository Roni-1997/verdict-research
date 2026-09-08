# Who trades short-term BTC binaries (Polymarket 5m/15m, Kalshi 15m)

Analysis run 2026-09-01 to 09-04 for Verdict (HIP-4 outcome-market venue on Hyperliquid). Everything
below is measured from venue APIs, not from third-party statistics, except where a line is labelled
"per venue announcement". Cross-checked against the two source reports in `reports/` on 2026-09-08;
see section 11. Do not re-derive unless you want to extend the sample.

## 0. Vocabulary (most published numbers get this wrong)

- **Taker volume** = one-sided dollars takers actually paid (shares x price). All numbers below use it unless labelled otherwise.
- **Headline volume** (what Polymarket publishes) counts both legs, about 2x taker volume.
- **Order** = one wallet, one market, one side, one second (fills aggregated). **Fill** = one matched print.
- **Wallet classes** are behavioural, per wallet per day: **bot** = 300+ fills/day, or 100+ fills spread across 16+ hours; **heavy** = 30-299 fills/day; **manual** = under 30 fills/day. Thresholds are ours; boundaries are soft.
- Validation of the classes: Polymarket's web app takes dollar amounts, the API takes share counts. Manual and heavy wallets place 51-66% of buy orders at exact dollar amounts ($1, $5, $2, $3, $10, $20, $25, $100); bots 13-17%. Manual wallets also place one order per window in about 75% of cases and 84% have a self-set display name.
- **Caveat:** the dollar signature is period-dependent. Exact-dollar share among manual wallets was about 18% in Feb-Mar, about 5% in Apr, and 52-59% from May 2. Polymarket's V2 exchange cutover (Apr 28) changed order entry. Use activity shape (fills/day, hours, both sides, timing) as the primary classifier and the dollar test as confirmation after May.

## 1. Datasets

| Dataset | Source | Coverage | Size |
|---|---|---|---|
| PM BTC 5m long run | data-api `/trades` per market, gamma `/events?series_id=10684` | 34 sample days, one every 6 days, Feb 13 (launch Feb 12) to Aug 30 2026 | ~27M fills, 495k wallet-days, 221,220 unique taker wallets |
| PM BTC 5m deep dives | same, taker legs and both legs (`takerOnly=false`) to identify makers | Sep 1-2 and Apr 14-15, all 576 windows each | 973k + 2.2M taker fills; 2.9M + 5.4M legs |
| PM BTC 15m deep dives | `series_id=10192` | Sep 1-2 and Apr 14-15, 192 windows each | 181k + 453k taker fills |
| Kalshi KXBTC15M | trade-api v2 `/markets/trades`, all 96 windows per day | 13 sample days, every 5th day, Jul 2 to Aug 31 2026 | ~27M prints, 14M reconstructed taker orders |

API limits found: Kalshi `/markets` (settled) only serves roughly the last 68 days; older markets come from `/historical/markets` (newest-first cursor walk, time filters ignored, limit 1000 or less). Kalshi has no account identities. Polymarket gamma `volumeNum` is missing on many older markets, so use measured taker volume, not headline.

## 2. Polymarket BTC 5m: the whole life of the product

| Date | Taker $/day | Wallets/day | New wallets/day | Bot share of $ | Manual PnL to settlement |
|---|---|---|---|---|---|
| Feb 13 (day 2) | $11.7M | 14,435 | all | 46% | -6.6% |
| Mar 3 (peak $) | $24.2M | 17,276 | 10,700 | 58% | -4.9% |
| Apr 8 (peak wallets) | $17.9M | 21,793 | 10,700 | 44% | -4.3% |
| May 2 (V2 cutover week) | $7.9M | 14,853 | 6,200 | 43% | -0.8% |
| Jul 31 | $10.1M | 10,408 | 2,700 | 51% | +1.0% |
| Aug 30 | $6.2M | 7,531 | 2,100 | 59% | -1.1% |

- The product opened at full size: 14.4k wallets, $11.7M, 46% bots on day two. It did not grow into it.
- The decline is a funnel problem: new wallets per day fell from 10,700 to 2,100. Existing users behaved identically throughout.
- Concentration: top-10 wallets 26% of taker $ at launch, 14% in May, 17% in Aug; top-100 53%, 40%, 51%.
- Lifecycle: 62% of all 221k wallets appear on one sample day (14% of $); 3% appear on 10+ days and hold 39% of $.
- Retention of new wallets: 22% seen again about 6 days later, 15% at about 12 days, 9% at about 24 days.
- Bots churn too: 42% of bot wallets are seen once; 35% of wallets that start as bots end up manual (scripts switched off).
- Class stickiness: wallets with 3+ sample days spend 75% of days in their modal class; 81% of manual starters stay manual.

## 3. Personas (PM 5m, wallets seen on 2+ sample days: 83,322 wallets, 86% of taker $)

| Persona | Wallets | Share of taker $ | Fills/day | Avg order | PnL per $ | Share Feb-Apr | Share Jul-Aug |
|---|---|---|---|---|---|---|---|
| 1. Engines / HFT (300+ fills/day, or 100+ across 16h) | 3,130 | 44% | 329 | $13 | +1% | 46% | 50% |
| 2. Script runners (100-299 fills/day) | 4,780 | 13% | 140 | $13 | -1% | 12% | 13% |
| 3. Power users (30-99 fills/day, human plus tooling) | 19,987 | 27% | 49 | $18 | -1% | 26% | 23% |
| 4a. Regulars, momentum (buy the side already ahead) | 30,949 | 6% | 10 | $17 | -3% | 6% | 6% |
| 4b. Sure-thing collectors (60%+ of buys at 85c or higher) | 9,588 | 8% | 9 | $50 | 0% | 9% | 6% |
| 5. Contrarians / longshots (50%+ against the move) | 12,388 | 1% | 7 | $13 | -7% | 1% | 1% |
| 6. Hedgers / arb (both sides in 40%+ of windows) | 2,500 | 1% | 24 | $9 | +4% | 0.5% | 1% |
| (plus wallets seen once) | 138,000 | 14% | | | | | |

- Human share of taker $: 5m Apr 53%, 5m Sep 35%, 15m Apr 55%, 15m Sep 47%.
- Per $1M of Polymarket headline volume today (both legs): roughly $100k manual humans, $120k heavy or semi-automated humans, $780k bots (split approximate; the human total of about $220k is the measured figure).
- Maker legs are 72-86% bots; 39% of maker premium comes from wallets that are also top taker bots; 22% of all premium is bot-vs-bot; self-trades 0.00%.

## 4. Decoded human behaviour (models, not labels; identical across all four samples, 5m and 15m, Apr and Sep)

- **Side choice** = follow the window's current state. P(bet Up) is 32% when the Up contract is below 0.35 and 67% when above 0.65. Logit slope on current price 2.25-2.57 (pseudo-R2 0.07-0.08). 30-second momentum, the previous window's result, and the trader's own last result all have about zero effect. 69% of buy premium goes in after the window is 15c or more from 50/50.
- **Timing:** 31% of buy $ in the last 2 minutes at large moves; only 8.5% at the open.
- **Sizing:** the same wallet bets 44-66% more on the favourite (t=105); +4.6-6.3% after a loss; streak and session length about zero. No martingale.
- **Continuation:** 47-50% play the immediately next window after a loss vs 40-46% after a win.
- **Exits:** only 3-8% of positions are closed before settlement; slight loss-cutting (7.6% sell in a big loss vs 5.8% in a big gain).
- **Edge:** human entries mark out +0.7 to +1.0pp at 30-60s (the move they chased continues briefly) but -3.1% at settlement on 5m. Bots: +2.2pp at 60s, +1.6% at settlement.
- **Timing PnL (5m, Sep):** open -3.9%, mid -3.7%, 1-2 min left -1.9%, 30-60s -1.7%, last 30s -5.4%. The last-30s figure was -0.8% in April: the "sure thing" trade got crowded by sniper bots after two venue changes (per venue announcement, verified 2026-09-08 against Polymarket's changelog and developer posts): settlement moved to a Chainlink TWAP on Aug 7 (30-second window for 5m, 60-second for 15m and 4h; the 5m window was later widened to 60 seconds) and the taker delay was cut from 250ms to 50ms on Aug 17 at 11:00 UTC.
- On 15m humans are about breakeven (-1.4% Apr, -0.7% Sep) vs -3% to -5% on 5m. Same people, less toxic window.
- No skill, no learning: day-to-day return correlation 0.08. Day-1 losers return 50% (winners 66%) and bet 0.74x their previous size.

## 5. Kalshi KXBTC15M (13 days, Jul 2 to Aug 31)

No identities, so order-level only (prints within 2ms, same side and market = one order).

- Averages: 1.10M taker orders/day, 161M contracts/day ($76M premium at a 47c average), 146 contracts per order. 75% of orders have fractional contract counts, 1.2% are exact-dollar: sizes are computed (broker or API routed), not typed.
- Order-size classes (13-day averages):

| Order size (contracts) | Share of orders | Share of contracts | Taker PnL | Notes |
|---|---|---|---|---|
| 50 or fewer | 66% | 7% | -3.8% after fee | broker retail |
| 51-500 | | 31% | -3.2% after fee | |
| 501-5,000 | | 48% | +0.1% before fee, -2.0% after | professional middle |
| over 5,000 | | 14% | | 31% placed in the last 2 minutes, 50% at price extremes: MMs flattening plus late "sure thing"; only rational with reduced or waived fees |

- Taker PnL after the published fee is negative every single day (-1.3% to -3.8%).
- 37-42% of volume trades 20:00-03:00 UTC every day (US evening, Robinhood distribution).
- Volume grew 60% from July to late August (125M to 198M contracts/day) with mix, fee burden and intraday rhythm unchanged.
- Fee schedule: fee per contract = 0.07 x p x (1-p), max 1.75c at 50c, about zero at the extremes. Kalshi 15m fee revenue estimate: $40-80M/month from BTC 15m alone. Its published incentive spend is capped at $1-1,000 per market per day (open tier) and $50k per series per week (MM tier), i.e. it pays roughly 0.3-0.5% of the fee revenue those markets generate. Kalshi buys liquidity with flow, not cash. (Incentive caps per Kalshi's published program terms, not measured.)

## 6. Named counterparties

The wallet-level list of the top Polymarket takers and makers (addresses, display names, per-wallet PnL) is held internally and is not in this repository. Aggregate facts: the top 10 takers buy both Up and Down in 87-100% of the windows they touch at a pair cost near $1.00, so they are makers flattening inventory or latency shops, not directional traders; several run 500 activity records in 0.2-1.5 hours with portfolio balances of $400-47k; the single biggest LP is a pure maker with about $1.33M of maker premium over 82k fills in two days.

## 7. Channel evidence

- Polymarket builder-code attribution (data-api `/v1/builders/leaderboard`): about $46M in the first 3 days of September across 50 third-party front ends, about $450M/month run rate (about 15% of Polymarket total). Largest: betmoar $10M (262 users), Gate $7M (9 users), traderline $4.5M (181), SpreadCore $2.7M, PolyHelper $2.5M, MagicMarkets $2.3M (1 user), MetaMask $1.5M (529 users), RedotPay, Jupiter. Everything else is the Polymarket app plus un-attributed API flow. Re-checked live on 2026-09-08: the daily leaderboard shows the same names in the same order of magnitude (betmoar $3.8M/day with 171 users, Gate $2.0M with 2 users, MetaMask $1.6M, traderline $1.6M, SpreadCore $1.4M).
- Polymarket has no broker distribution; Kalshi's flow arrives through Robinhood and Webull, which is why Kalshi's 15m does 20x or more Polymarket's 15m premium with the same behaviour.

## 8. Conclusions that matter for a new venue

1. **The customer is not "educated".** Side choice is explained only by which side is already winning. No learning, no money management, negative expectancy after fees for every human class. It is a fast, capped-loss, chart-driven bet, closer to 0DTE options and retail FX than to informed trading. ESMA prohibited binary options for EU retail clients in 2018 after national regulators' studies found that most retail clients lose money (the 74-89% loss range widely quoted alongside it is the CFD risk-warning figure). Treat the legal posture as first-order.
2. **Machines are the majority and they follow flow, they do not create it.** 66-78% of Polymarket 5m volume is bots; they earn +1-2% and are funded by the roughly $75k/day that humans lose plus the reward pools. A bot-only market has no source of money.
3. **Volume follows the funnel, not the incentives.** Polymarket's decline tracks new-wallet inflow (-80%), not user behaviour. Retention is 9% at one month.
4. **15m keeps humans better than 5m** (humans about breakeven vs -3% to -5%). If human retention matters, the 15m tenor is the friendlier product; 5m is where the volume and the toxicity are.
5. **Taker cash rewards would be about 90% a bot subsidy.** Pay makers for resting depth (quote score) and for absorbing flow weighted by adverse selection; give takers points with per-address caps, never cash per trade.
6. **The feed and reprice speed are the product.** The entire bot tail's strategy is "read the public oracle, hit stale quotes". A settlement index slower than the makers' feed gets farmed on day one.
7. **Order count, not order size, is the load.** Average order is $20 for humans and bots alike on Polymarket (median $4-5); Kalshi averages 146 contracts ($70). Polymarket 5m at its peak was about 950k taker orders/day.

## 9. Artifacts in this repository

- `reports/2026-09-03-pm-btc5m-flow-wallets-deep-dive.md`: the two-day deep dives (5m and 15m, Apr and Sep), behaviour models, Kalshi order-level reconstruction. Wallet table redacted.
- `reports/2026-09-03-pm-btc5m-users-longrun-and-kalshi-13d.md`: full life of the Polymarket product, personas, Kalshi 13-day series.
- `reports/2026-09-01-recurring-crypto-products-6mo.md`: six-month product volume tables for both venues.
- `data/pm_btc5m_market_days.jsonl`: per-market, per-sample-day aggregates for Polymarket BTC 5m (9,790 rows). `data/kalshi_kxbtc15m_days.jsonl`: the 13 Kalshi sample days with size-class bins. Schemas in `data/README.md`.
- GitHub release `data-2026-09`: raw Kalshi prints for 5 of the 13 sample days (Aug 11, 16, 21, 26, 31; about 80 MB gzipped).
- Not retained: the pull and analysis scripts, the raw Polymarket fills, per-wallet-day aggregates, and the first 8 Kalshi sample days. The Polymarket side can be re-pulled from the public data API; the Kalshi July days cannot (68-day retention). Verdict's launch board, incentive plan and MM requirements referenced by the original handoff are internal documents and are not included.

## 10. Known gaps and how to extend

- Kalshi cannot be user-classified (no identities) and its trade history stops at about 68 days.
- The Polymarket long run is 1 day in 6; intra-week effects are averaged out, not measured.
- The manual/heavy boundary is a threshold choice: a heavy user with hotkeys and a small script look alike. Do not report "X% retail" without stating the rule.
- Not measured: funding-source clustering of the top bot wallets (several may be one firm), Polymarket 15m long-run history, alt-coin tenors, and whether the same wallets appear on Hyperliquid.

## 11. Verification log (2026-09-08)

- Sections 2, 3, 4 and 5 were checked line by line against the two source reports; every figure matches. Unrounded wallet counts in section 2 come from the original run and agree with the reports' rounded values.
- Section 4 venue-change dates verified against Polymarket's public changelog and developer announcements (TWAP settlement Aug 7; taker delay 250ms to 50ms on Aug 17, 11:00 UTC).
- Section 7 magnitudes re-checked live against the builders leaderboard on Sep 8.
- Not independently re-verified: the Kalshi incentive-cap figures and the $40-80M/month fee estimate (derived from the measured 1.8% fee burden on $76M/day of premium, which gives about $41M/month on the taker side alone).
- The ESMA sentence in section 8 was reworded: the original attached the 74-89% figure to binary options; that range is the CFD risk-warning statistic.
