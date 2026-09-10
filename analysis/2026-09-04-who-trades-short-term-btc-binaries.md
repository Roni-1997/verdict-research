# Who trades short-term BTC binaries (Polymarket 5m/15m, Kalshi 15m)

Analysis run 2026-09-01 to 09-04 for Verdict (HIP-4 outcome-market venue on Hyperliquid), with later
updates identified below. The historical tables are API-derived analysis; externally reported facts
and economic interpretations are labelled separately. Cross-checked against the source reports in
`reports/` on 2026-09-08; matching those reports is not an independent validation of their methodology.

Interpretation updated 2026-09-10: the executive takeaway and section 8 supersede the earlier claim
that automated markets necessarily depend on retail losses. Historical "bot", "human" and "retail"
labels below are behavioural proxies, not verified identities. Historical settlement markouts are
not complete wallet profitability: fees, rebates, other positions and external hedges can change the
result. This update does not re-run the historical datasets.

## Executive takeaway: professional flow does not require "dumb money"

**Deribit's CEO has described approximately 80-85% of its business as institutional, including
volume and open interest.** This is a management estimate from an earlier public interview, not a
current audited customer census, and it does not mean "85% bots". Source chain: CEO Luuk Strijers
speaking in the interview clip and transcript published by [Kemet Trading](https://www.linkedin.com/posts/kemettrading_derivativesdecoded-podcast-cryptoinvesting-activity-7336840655530315776-DLxC).
Confidence is high that this is the CEO's reported estimate; the exact measurement period and
underlying classification data were not published with the clip.

### Why this can work

A professional venue sells execution and risk transfer, not just opportunities to beat uninformed
traders. Its customers can have different objectives:

- A fund buys protection for an existing portfolio.
- An option seller accepts risk in exchange for a premium.
- A dealer hedges exposure created by a client's trade elsewhere.
- Market makers and arbitrageurs price, redistribute and hedge that exposure across instruments.

**Simple illustration, not a measured Deribit trade:** a fund holding BTC buys downside protection.
If BTC rises, that option may expire worthless, but the fund's BTC appreciates. The premium bought
protection; losing money on that one option does not make the fund irrational. Another professional
can earn a premium for bearing risk, and the venue can earn fees for matching them. This is the
standard distinction between hedgers transferring risk and speculators accepting it, described by
[CME](https://www.cmegroup.com/education/courses/introduction-to-futures/understanding-the-role-of-hedgers).

There is also a concrete Deribit example: a [2022 OrBit Markets article published by Paradigm](https://www.paradigm.co/blog/paradigm-defi-options-vaults)
describes option vaults selling contracts to professional market makers, with Deribit contracts used
to hedge those flows. The visible exchange trade can therefore be professional-to-professional while
the originating investment demand sits elsewhere. This is a historical mechanism, not a current
estimate of vaults' share of Deribit volume.

### What the retail/noise-flow argument gets wrong

**Retail is an identity, automation is an execution method, and risk transfer is a reason to trade.**
They are not interchangeable. A professional can submit an automated hedge that is not trying to
predict the next price change. Conversely, a retail trader can be informed or run a bot. Less
information-driven flow can help market makers, but it need not come from an unsophisticated person.

One customer exposure can also lead to multiple genuine hedge and rebalance trades. A high automated
share therefore does not establish that economic demand is absent. Nor does Deribit's institutional
share independently validate our Polymarket behavioural classifier: the definitions and denominators
are different.

**The important limit:** this does not mean a closed loop of arbitrage bots creates unlimited profit.
Trading gains and losses offset before costs; participants can nevertheless gain economically from
reduced risk or useful exposure. A durable venue needs recurring reasons to pay trading costs and
liquidity providers that can cover adverse selection, inventory risk and operating costs. Those
reasons may be entirely professional, or may reach the venue through brokers and dealers.

**Implication for Verdict:** professional-first is a credible model, not proof of demand for our
five-minute contracts. We must establish who wants those exact expiries, strikes and settlement
rules, and show repeat fee-paying activity with sustainable liquidity. The question is not "where
are the dumb retail traders?" It is **"who needs this exposure or execution, and why will they keep
paying for it?"**

## 0. Vocabulary (most published numbers get this wrong)

- **Taker volume** = one-sided dollars takers actually paid (shares x price). All numbers below use it unless labelled otherwise.
- **Headline volume** (what Polymarket publishes) counts both legs, about 2x taker volume.
- **Order** = one wallet, one market, one side, one second (fills aggregated). **Fill** = one matched print.
- **Framework (adopted 2026-09-10).** Participant classes follow the seven-cohort grid of [Roni-1997/polymarket-segmentation](https://github.com/Roni-1997/polymarket-segmentation): maker share of touched volume (70%+ high, 30-70% mid, under 30% low) by cadence in fills per active day (100+ fast, 10-100 systematic, under 10 discretionary). Cohorts: Pro-MM, Mid-MM, Hybrid-bot, Systematic-mixed, Fast-taker, Systematic-taker, Retail (any maker share, under 10 fills a day); rollup MMs / Bots+Algo / Retail. Touched volume counts both sides of every fill; single-counted notional is half of it. Cohort tables for the measured BTC 5m days are in `data/pm_btc5m_cohorts_2026-09.md` (both legs re-pulled with transaction hashes). The historical tables below predate the adoption and use the older labels; the mapping is: bot core (300+ fills) = Fast-taker, Hybrid-bot and Pro-MM taking; heavy (30-299 fills) = Systematic-taker and Systematic-mixed, with the sleep-gap test as a sub-split into tool-assisted humans and part-day machines; manual (under 30 fills) = Retail plus the lower end of Systematic-taker. Labels are behavioural, not identity, in both frameworks.
- **Wallet classes** are behavioural, per wallet per day. **Report rule, used for every historical table below:** bot = 300+ fills/day, or 100+ fills spread across 16+ hours; heavy = 30-299 fills/day; manual = under 30. **Revised rule (2026-09-10, primary going forward):** bot = 300+ fills/day, or 30+ fills/day with no gap of 6 or more hours between the wallet's orders in the UTC day (it never sleeps), or buying both sides in 40%+ of the windows it trades (5+ windows); everyone else is human, split into manual (under 30 fills) and session traders (30+ fills with a sleep gap). The revised rule moves the never-sleeping part of the heavy band to bots: 36% of the 30-99 band's dollars and 57% of the 100-299 band's. Sep 9 2026: report rule 60% bots, revised rule 69%. Evidence in `data/pm_btc5m_human_share_sensitivity_2026-09-09.md`.
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

## 1b. Six-month product volume series (Mar to Aug 2026, both venues): the market this sits in

Separate pull (2026-09-01) covering every recurring crypto product on both venues, monthly, from the
Kalshi settled-market tape (3.4M markets via `/markets` and `/historical/markets`) and Polymarket gamma
events by series. Units differ by venue: Kalshi = $1-notional contracts settled per day (multiply by
about 0.276 for a premium-dollar equivalent, tape-measured); Polymarket = premium $/day as reported.

Kalshi, contracts per day (top products):

| Product | Mar | Apr | May | Jun | Jul | Aug | Aug vs Mar |
|---|---|---|---|---|---|---|---|
| BTC 15m up/down | $16.4M | $21.4M | $34.6M | $78.8M | $136.6M | $177.1M | +983% |
| BTC hourly above/below ladder | $15.8M | $18.5M | $25.1M | $43.1M | $44.9M | $39.1M | +148% |
| ETH 15m | $1.70M | $1.75M | $1.76M | $3.51M | $7.49M | $8.75M | +415% |
| XRP 15m | $0.74M | $0.41M | $0.48M | $1.26M | $2.16M | $3.74M | +404% |
| SOL 15m | $0.81M | $0.52M | $0.65M | $1.16M | $2.21M | $2.92M | +262% |
| HYPE 15m | $0.14M | $0.26M | $0.37M | $1.62M | $2.59M | $2.59M | +1759% |
| DOGE 15m | $0.11M | $0.22M | $0.26M | $0.91M | $2.00M | $2.37M | +2012% |
| BNB 15m | $0.04M | $0.14M | $0.21M | $0.76M | $1.40M | $1.70M | +3936% |
| ETH hourly ladder | $0.65M | $0.49M | $0.33M | $0.81M | $1.52M | $1.73M | +167% |

Polymarket, premium $ per day (top products):

| Product | Mar | Apr | May | Jun | Jul | Aug | Aug vs Mar |
|---|---|---|---|---|---|---|---|
| BTC 5m up/down | $13.4M | $31.1M | $22.2M | $24.0M | $21.6M | $14.4M | +7% |
| BTC 15m up/down | $3.48M | $6.13M | $4.17M | $3.65M | $2.83M | $2.47M | -29% |
| BTC daily close ladder | $1.97M | $4.55M | $3.08M | $2.89M | $1.83M | $1.49M | -24% |
| ETH 5m | $1.50M | $3.12M | $2.16M | $1.93M | $1.97M | $1.01M | -33% |
| BTC monthly touch ladder | $3.91M | $3.32M | $1.85M | $1.41M | $1.13M | $0.81M | -79% |
| BTC hourly up/down | $1.59M | $2.13M | $1.10M | $0.96M | $0.83M | $0.74M | -54% |
| ETH 15m | $0.79M | $1.45M | $0.85M | $0.73M | $0.65M | $0.48M | -39% |
| SOL 5m | $0.69M | $1.34M | $0.70M | $0.74M | $0.78M | $0.32M | -54% |

Read: Kalshi's 15m franchise is the only product on either venue with sustained month-on-month growth
(BTC 10.8x in six months, every alt 15m 3 to 40x, all inflecting in June when broker distribution
stepped up). Kalshi's hourly ladder plateaued in June. Every Polymarket crypto product peaked in April
and has declined since; only Polymarket daily up/down and 4h grew, both under $0.3M/day. Cross-venue:
Kalshi sub-hour crypto is about 12x Polymarket's in contract terms (about 3x in premium terms) and the
ratio widens monthly. Full tables (17 Kalshi products, 51 Polymarket products) in
`reports/2026-09-01-recurring-crypto-products-6mo.md`; monthly CSVs and raw JSON in `data/`.

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
- Bot share over the life of the product (report rule: 300+ fills/day or 100+ across 16 hours). Taker $ by sample day: Feb 13 46%, Mar 3 58%, Apr 8 44%, Apr 14-15 48%, May 2 43%, Jun 25 57%, Jul 31 51%, Aug 30 59%, Sep 1-2 66%, Sep 9 60% (69% under the strict rule). Weighting each month's taker $ (from the 34 sample days) by its period bot share (Feb-Apr 49%, May-Jun 52%, Jul-Aug 54%, Sep 63%) gives about 51% of all taker $ from Feb 13 to Sep 9 (roughly $1.4B of $2.7B one-sided). Maker legs: 78% bots in April, 86% in September (the two measured samples), so about 80% over the period. Headline volume, both legs: about 65% bots over the product's life, 63% at the April peak, 76 to 78% in September.
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

- Human share of taker $: 5m Apr 53%, 5m Sep 35%, 15m Apr 55%, 15m Sep 47%. These use the report rule (human = under 300 fills/day). Re-measured on Sep 9 under stricter rules the 5m figure spans 31 to 40%, so treat it as "about a third", not a point estimate. Under the revised sleep-gap rule the Sep 9 human share is 31% (manual 12%, session traders with 30-99 fills 12%, session traders with 100-299 fills 7%); see `data/pm_btc5m_human_share_sensitivity_2026-09-09.md`.
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
- 37-42% of volume trades 20:00-03:00 UTC every day (US evening). Attributing this to Robinhood distribution is an inference from timing and from Robinhood's public statements about its share of Kalshi volume overall, not a measurement: the Kalshi tape carries no identities and no channel, and the human-versus-automated split of this flow is not measurable (see `data/kalshi_kxbtc15m_order_shape_2026-09-10.md`).
- Volume grew 60% from July to late August (125M to 198M contracts/day) with mix, fee burden and intraday rhythm unchanged.
- Fee schedule: fee per contract = 0.07 x p x (1-p), max 1.75c at 50c, about zero at the extremes. Kalshi 15m fee revenue estimate: $40-80M/month from BTC 15m alone. Its published incentive spend is capped at $1-1,000 per market per day (open tier) and $50k per series per week (MM tier), i.e. it pays roughly 0.3-0.5% of the fee revenue those markets generate. Kalshi buys liquidity with flow, not cash. (Incentive caps per Kalshi's published program terms, not measured.)

## 6. Named counterparties

The wallet-level list of the top Polymarket takers and makers (addresses, display names, per-wallet PnL) is held internally and is not in this repository. Aggregate facts: the top 10 takers buy both Up and Down in 87-100% of the windows they touch at a pair cost near $1.00, so they are makers flattening inventory or latency shops, not directional traders; several run 500 activity records in 0.2-1.5 hours with portfolio balances of $400-47k; the single biggest LP is a pure maker with about $1.33M of maker premium over 82k fills in two days.

## 7. Channel evidence

- Polymarket builder-code attribution (data-api `/v1/builders/leaderboard`): about $46M in the first 3 days of September across 50 third-party front ends, about $450M/month run rate (about 15% of Polymarket total). Largest: betmoar $10M (262 users), Gate $7M (9 users), traderline $4.5M (181), SpreadCore $2.7M, PolyHelper $2.5M, MagicMarkets $2.3M (1 user), MetaMask $1.5M (529 users), RedotPay, Jupiter. Everything else is the Polymarket app plus un-attributed API flow. Re-checked live on 2026-09-08: the daily leaderboard shows the same names in the same order of magnitude (betmoar $3.8M/day with 171 users, Gate $2.0M with 2 users, MetaMask $1.6M, traderline $1.6M, SpreadCore $1.4M).
- Polymarket has no broker distribution; Kalshi has Robinhood and Webull as channels. How much of KXBTC15M flow arrives through them, and how much of it is human, is not measurable from public data. Broker distribution is a plausible, unproven, large part of why Kalshi's 15m does roughly 8x (against Polymarket's 5m and 15m combined) to 20x (against its 15m alone) the premium with the same behaviour; US access, in-app placement, deeper market-maker books and the absence of a cannibalising 5m product on Kalshi contribute too.

## 8. Conclusions that matter for a new venue

These are research implications and recommendations, not additional measured findings.

1. **A professional-heavy venue can be viable.** Deribit's management-reported 80-85% institutional share is a concrete precedent. It does not prove a no-retail ecosystem or demand for five-minute binaries. The relevant customer distinction is who originates demand, who intermediates risk, and how each executes - not simply "humans versus bots".
2. **Retail losses are not the only possible source of trading revenue.** Funds can pay to hedge, dealers to offset client exposures, and investors to take or sell risk. Market makers need flow they can price and manage profitably, not necessarily uninformed retail counterparties. Neither trade-frequency labels nor standalone settlement markouts identify everyone's motives or complete economic returns.
3. **Distribution and retention still matter.** The sampled Polymarket decline coincides with weaker new-wallet inflow; that does not establish a single cause. Professional-first distribution can mean funds, dealers, brokers and other frontends. We should measure repeat usage rather than assume incentives or a consumer funnel alone will sustain volume.
4. **Choose the tenor by demand and execution quality.** The sampled lower-frequency cohorts had less-negative settlement markouts in 15m than 5m, but that is not proof of better retention or net profitability. For Verdict, test exact contract demand, spread, depth, slippage and repeat trading for each tenor. Legal and access requirements remain a separate launch condition; deterministic settlement alone does not establish legality.
5. **Judge liquidity and venue economics after incentives.** Proposed success measures: repeat fee-paying customers; depth and spreads at usable sizes; LP profitability after hedges, fees and rewards; and venue revenue after rebates, incentives and operating costs. Arbitrage volume is useful only if the surrounding economics are sustainable, not merely subsidised turnover.
6. **Protect execution and settlement quality.** Latency arbitrage is a real risk, but the observed behaviour does not prove it is every automated trader's strategy. Deribit explicitly describes options speed bumps intended to protect passive LPs from latency arbitrage in its [Starbase infrastructure update](https://insights.deribit.com/exchange-updates/starbase-a-new-era-of-high-performance-trading-on-deribit/). Professional participation and protection against toxic execution are compatible.
7. **Capacity planning must include messages, not just dollars.** Measure peak order submissions, cancellations, replacements, fills and market-data fan-out. The historical fill counts describe executed activity, not the full infrastructure load.

## 9. Artifacts in this repository

- `reports/2026-09-03-pm-btc5m-flow-wallets-deep-dive.md`: the two-day deep dives (5m and 15m, Apr and Sep), behaviour models, Kalshi order-level reconstruction. Wallet table redacted.
- `reports/2026-09-03-pm-btc5m-users-longrun-and-kalshi-13d.md`: full life of the Polymarket product, personas, Kalshi 13-day series.
- `reports/2026-09-01-recurring-crypto-products-6mo.md`: six-month product volume tables for both venues.
- `data/pm_btc5m_market_days.jsonl`: per-market, per-sample-day aggregates for Polymarket BTC 5m (9,790 rows). `data/kalshi_kxbtc15m_days.jsonl`: the 13 Kalshi sample days with size-class bins. Schemas in `data/README.md`.
- GitHub release `data-2026-09`: raw Kalshi prints for 5 of the 13 sample days (Aug 11, 16, 21, 26, 31; about 80 MB gzipped).
- `data/verdict_recurring_{kalshi,polymarket}_monthly.csv` and `_monthly_raw.json`: the six-month monthly totals behind section 1b.
- `data/pm_builder_attribution_2026-09-10.md` and `pm_btc5m_human_share_sensitivity_2026-09-09.md`: later snapshots that extend sections 7 and 3.
- Not retained: the pull and analysis scripts, the raw Polymarket fills, per-wallet-day aggregates, and the first 8 Kalshi sample days. To rebuild: Polymarket, gamma `GET /events?series_id=<id>&end_date_min/max` (5m = 10684, 15m = 10192) to list markets per day, then data-api `GET /trades?market=<conditionId>&limit=1000&offset=` for taker legs and the same with `takerOnly=false` for both legs (a maker leg is one whose (tx, wallet) is not in the taker set); offsets cap out around 10k per market; aggregate per wallet per day and classify with the section 0 rules. Kalshi, `GET /trade-api/v2/markets?series_ticker=KXBTC15M&status=settled` then `GET /markets/trades?ticker=&cursor=` per window; reconstruct parent orders by grouping prints within 2 ms on the same side of the same market. The Polymarket side can be re-pulled from the public data API; the Kalshi July days cannot (68-day retention). Verdict's launch board, incentive plan and MM requirements referenced by the original handoff are internal documents and are not included.

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

### Interpretation and source update (2026-09-10)

- Added the Deribit institutional-share estimate from the CEO's own interview clip/transcript, with management-estimate status and measurement-period limitations. This is external evidence, not a result from our trade dataset.
- Added the historical OrBit/Paradigm vault-to-dealer-to-Deribit hedging example and CME's explanation of hedgers' objectives. Economic illustrations are explicitly separate from measured participant shares.
- Replaced section 8's categorical dependence-on-retail-losses argument and unsupported identity, causal, strategy and subsidy claims with qualified conclusions. Deribit is a market-structure analogy, not a cross-validation of the Polymarket classifier or proof of Verdict demand.
- No historical tables, raw datasets or classifiers were re-run in this update. Source reports remain historical inputs; this synthesis's updated interpretation takes precedence over their earlier conclusions.
