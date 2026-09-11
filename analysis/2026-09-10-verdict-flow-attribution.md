# Verdict flow attribution: who trades short-term crypto binaries, in the seven-cohort framework

Date: 2026-09-10. Scope: Polymarket BTC 5-minute up/down markets (series 10684), all 288 windows of
2026-09-09 UTC, both legs of every fill (1,383,413 records: 476,400 taker legs, 907,013 maker legs, 8,328
wallets, $14.28M touched, $7.14M single-counted). Aug 30 and Sep 8 were pulled the same way; the three-day
tables are in section 4b. Classification follows [Roni-1997/polymarket-segmentation](https://github.com/Roni-1997/polymarket-segmentation):
maker share of touched volume (70%+ high, 30-70% mid, under 30% low) by cadence (100+ fills fast, 10-100
systematic, under 10 discretionary), Retail at any maker share under 10 fills. Proxy-wallet level, single
day, so cadence is fills that day. Labels are behavioural, not identity. This document supersedes the
2026-09-10 Codex report "Verdict Flow Attribution" for the participant analysis; its evidence-boundary and
GTM sections are condensed in sections 6 and 7. Scripts: `scripts/pm_pull_btc5m_both_legs.py`,
`scripts/pm_cohorts_v1_v2_2026-09-10.py`. Results: `data/pm_btc5m_cohorts_v1_2026-09-09.json`, `_v2_`.

## 1. The claim, in the form that survives diligence

Volume and depth on short-term crypto binaries are machines. Pro-MM, Fast-taker and Hybrid-bot are 82% of
touched volume on Polymarket BTC 5m over the 30 days to Sep 9; market makers provide 75% of the maker side and
Bots plus Algo consume 92% of the taker side under the segmentation grid (section 4c). Strict Retail, under 10 fills a day, is 1.2% of touched volume over the 30 days. A venue does not need a consumer
funnel to get liquidity: the 5m product opened at full size on its second day with 46% bot share.

What every such venue also has is a minority of paying flow. People, meaning Retail plus tool-assisted
session traders, are 17% of touched volume and 29% of the taker side, and they lose about $76k a day on
$7M of taker premium. Over the continuous 30 days to Sep 9 (`data/pm_btc5m_trailing30_2026-08-11_09-09.md`)
machines were 67.5% of taker dollars, positive on all 30 days, people negative on all 30; 31.9% of wallets
ended the month ahead and the median wallet lost 5.7%. Machines net about $42k and market makers about $33k. Machine-against-machine
trading is zero-sum before costs. When Polymarket's new-wallet inflow fell 80%, bot dollars fell 43%.

So the investor sentence is: we do not need our own retail app, because the machines are the liquidity
and they arrive on their own; we do need paying flow, and ours comes from HL-native traders one click
away, partner frontends carrying our builder code, and a maker pool that bridges the gap. The machines
are the liquidity. The frontends are the customers.

## 2. Polymarket BTC 5m in the seven-cohort grid (2026-09-09; superseded by the 30-day window in 4c)

| Cohort | Wallets | % touched | % maker side | % taker side | $ per fill | PnL to settlement per $ | PnL $ |
|---|---|---|---|---|---|---|---|
| Pro-MM | 545 | 35.5% | 71.8% | 2.7% | 7 | +0.66% | +33,254 |
| Fast-taker | 711 | 34.6% | 6.6% | 59.9% | 14 | +0.32% | +15,806 |
| Hybrid-bot | 171 | 15.1% | 17.4% | 13.1% | 12 | -0.11% | -2,439 |
| Systematic-taker | 2,742 | 11.3% | 0.6% | 20.9% | 17 | -2.01% | -32,274 |
| Mid-MM | 435 | 1.2% | 2.4% | 0.2% | 10 | -0.56% | -983 |
| Systematic-mixed | 301 | 1.0% | 1.0% | 1.0% | 13 | -0.61% | -879 |
| Retail | 3,423 | 1.3% | 0.3% | 2.2% | 15 | -6.85% | -12,485 |

Rollup, against the segmentation repo's published figures (venue-wide and crypto category, May 2026):

| Persona | BTC 5m Sep 9, % touched | % maker side | % taker side | PnL $ | Repo venue-wide May | Repo crypto May |
|---|---|---|---|---|---|---|
| MMs (Pro-MM, Mid-MM) | 36.7% | 74.2% | 2.9% | +32,271 | 38.4% | 38% |
| Bots plus Algo | 62.0% | 25.6% | 94.9% | -19,786 | 56.3% | 58% |
| Retail | 1.3% | 0.3% | 2.2% | -12,485 | 5.3% | 5% |

The BTC 5m product is the venue's fingerprint with the retail share squeezed further. Maker side is
Pro-MM 72% here against 59% for crypto venue-wide; taker side is Fast-taker 60% against 49%.

## 3. Who pays whom: PnL by cohort

PnL to settlement is computed per leg: a buy of an outcome pays 1 if that outcome wins, a sell the
reverse; summed over both legs it is zero by construction, so the table shows transfers between cohorts
before fees and rewards. Polymarket charged no taker fee on these markets. Rewards are not included.

The transfer runs from Systematic-taker (-$32k) and Retail (-$12k) to Pro-MM (+$33k) and Fast-taker
(+$16k). The Bots plus Algo persona nets negative as a whole because it contains both the payers
(Systematic-taker) and the earners (Fast-taker). That is the segmentation repo's open question from its
caveat 7 and its trend section, answered for this product: the systematic-taker cohort is uninformed
flow by result, and it is where most of the money is lost.

## 4. Where the grid is blunt, and the v2 split

The v1 axes put humans with tools and part-day machines in the same cells. A sharper operation-mode axis
(unattended: no 6h gap or 16+ active hours; part-day machine: two-sided in 40%+ of windows or a dense
share-typed run of 4h+; session: neither) and a directionality axis (neutral = both sides bought in 40%+ of
windows) give six cohorts. Specification with evidence: `data/pm_cohort_v2_spec_2026-09-10.md`.

| v2 cohort | Wallets | % touched | % maker side | % taker side | PnL per $ | PnL $ | Exact-dollar buys | Sells | Active hours |
|---|---|---|---|---|---|---|---|---|---|
| Pro-MM | 687 | 34.3% | 69.7% | 2.3% | +0.77% | +37,830 | 3% | 8% | 20 |
| Part-time MM | 240 | 2.4% | 4.4% | 0.5% | -1.31% | -4,390 | 4% | 7% | 6 |
| Neutral bot | 376 | 25.0% | 14.3% | 34.7% | +1.38% | +49,480 | 10% | 6% | 9 |
| Directional bot | 1,107 | 21.5% | 8.1% | 33.6% | -0.23% | -7,158 | 6% | 7% | 18 |
| Session trader | 2,374 | 15.3% | 3.1% | 26.3% | -2.76% | -60,356 | 41% | 27% | 5 |
| Retail | 3,544 | 1.5% | 0.4% | 2.5% | -7.16% | -15,406 | 0% | 19% | 1 |

Rollup: MMs 36.7% of touched (+$33k), Machines 46.5% (+$42k), People 16.8% (-$76k). The validation rule
holds on this day: Neutral bot and Pro-MM positive, Directional bot near zero, Session trader negative,
Retail most negative. The behavioural columns separate cleanly: session traders and retail size in
dollars and exit positions, machines size in shares and hold.

Crosswalk, share of each v1 cohort's touched dollars:

| v1 cohort | Goes to |
|---|---|
| Pro-MM (35.5%) | Pro-MM 95%, Part-time MM 5% |
| Fast-taker (34.6%) | Neutral bot 46%, Directional bot 39%, Session trader 15% |
| Hybrid-bot (15.1%) | Neutral bot 57%, Directional bot 34%, Session trader 10% |
| Systematic-taker (11.3%) | Session trader 71%, Directional bot 24%, Neutral bot 3% |
| Mid-MM (1.2%) | Part-time MM 56%, Pro-MM 42% |
| Systematic-mixed (1.0%) | Session trader 66%, Directional bot 24% |
| Retail (1.3%) | Retail 100% |

Fast-taker is the cell that most needed splitting: 46% of its dollars are market-neutral machines that
earn, 39% directional machines that do not, 15% people.

## 4b. Three days: Aug 30, Sep 8 and Sep 9, 2026 (superseded by 4c)

Same method on three days, 4,283,811 records and $42.0M touched ($14.0M a day). Shares are the
mean of the daily shares; PnL dollars are summed. Two markets a day hit the pagination limit and are truncated.

| Cohort | Wallets per day | % touched | % maker side | % taker side | PnL per $ | PnL $, three days | % touched by day (Aug 30, Sep 8, Sep 9) |
|---|---:|---:|---:|---:|---:|---:|---|
| Pro-MM | 518 | 35.4% | 69.1% | 3.2% | +0.53% | +80,943 | 35.8, 34.8, 35.5 |
| Fast-taker | 727 | 31.8% | 5.3% | 57.1% | +0.31% | +44,692 | 25.7, 35.2, 34.6 |
| Hybrid-bot | 192 | 18.0% | 19.7% | 16.4% | +0.10% | +8,427 | 22.7, 16.2, 15.1 |
| Systematic-taker | 2,673 | 10.3% | 0.5% | 19.8% | -2.09% | -94,766 | 9.6, 10.2, 11.3 |
| Mid-MM | 438 | 2.1% | 4.1% | 0.2% | -1.12% | -8,914 | 3.7, 1.4, 1.2 |
| Systematic-mixed | 311 | 1.1% | 1.0% | 1.1% | -0.33% | -1,400 | 1.1, 1.2, 1.0 |
| Retail | 3,533 | 1.3% | 0.3% | 2.2% | -5.53% | -29,025 | 1.4, 1.1, 1.3 |

| Persona | % touched | % maker side | % taker side | PnL $, three days | May 2026 venue-wide |
|---|---:|---:|---:|---:|---:|
| MMs (Pro-MM, Mid-MM) | 37.5% | 73.2% | 3.4% | +72,029 | 38.4% |
| Bots and algo | 61.3% | 26.5% | 94.4% | -43,046 | 56.3% |
| Retail | 1.3% | 0.3% | 2.2% | -29,025 | 5.3% |

Pro-MM, Fast-taker and Hybrid-bot together are 85% of touched volume. Market makers provide 73% of the
maker side; bots and algo consume 94% of the taker side. Retail is 1.3%. Settlement PnL moves about
$41k a day from Systematic-taker and Retail to Pro-MM and Fast-taker.

The proposed v2 split on the same three days:

| v2 cohort | Wallets per day | % touched | % maker side | % taker side | PnL per $ | PnL $, three days | PnL per $ by day |
|---|---:|---:|---:|---:|---:|---:|---|
| Pro-MM | 647 | 35.3% | 69.2% | 3.0% | +0.60% | +90,120 | +0.32%, +0.71%, +0.77% |
| Part-time MM | 253 | 2.1% | 3.9% | 0.4% | -1.98% | -16,845 | -2.53%, -2.12%, -1.31% |
| Neutral bot | 409 | 25.4% | 14.5% | 35.9% | +1.20% | +130,826 | +0.89%, +1.33%, +1.38% |
| Directional bot | 1,068 | 20.5% | 8.5% | 31.9% | +0.30% | +21,671 | +1.15%, +0.00%, -0.23% |
| Session trader | 2,361 | 15.1% | 3.4% | 26.3% | -2.88% | -182,139 | -3.02%, -2.84%, -2.76% |
| Retail | 3,653 | 1.5% | 0.5% | 2.6% | -6.93% | -43,676 | -2.62%, -11.00%, -7.16% |

| Rollup | % touched | % maker side | % taker side | PnL $, three days |
|---|---:|---:|---:|---:|
| MMs | 37.4% | 73.0% | 3.4% | +73,275 |
| Machines | 45.9% | 23.0% | 67.8% | +152,497 |
| People | 16.7% | 3.9% | 28.8% | -225,815 |

The v2 validation rule (Neutral bot and Pro-MM positive, Directional bot near zero, Session trader
negative, Retail most negative) holds on Sep 8 and Sep 9. On Aug 30 the directional machines earned
+1.15%, more than the neutral ones, so the rule holds in two days of three. Session traders lose 2.8 to
3.0% per dollar on every day and are the largest single source of the money that the machines and the
makers earn: $182k over three days against $44k from Retail.

## 4c. Trailing 30 days, both legs: the grid over the full window (2026-08-11 to 2026-09-09)

Every fill, both legs, for 30 consecutive UTC days: 57,300 proxy wallets, $458.4M touched
($15.28M a day, $7.64M single-counted). One cohort per wallet for the whole window, as the
segmentation repo defines it: cadence is fills per active day across the window and maker share is the wallet's
maker touched volume over its total. Settlement PnL is gross of fees (none charged) and LP rewards. Over the
month 30.3% of wallets ended ahead, the median wallet lost 5.6% of what it traded, and the top 1%
of wallets took 82% of gross gains. This section supersedes the one-day and three-day tables above.

| Cohort | Wallets | % touched | % maker side | % taker side | PnL per $ | PnL $, 30 days | Wallets profitable | Median PnL per $ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Pro-MM | 1,418 | 38.4% | 69.9% | 5.8% | +0.16% | +282,587 | 28.8% | -1.7% |
| Fast-taker | 2,379 | 21.9% | 3.1% | 41.5% | +0.38% | +377,546 | 37.2% | -0.7% |
| Hybrid-bot | 763 | 21.9% | 19.8% | 24.2% | +0.66% | +663,317 | 29.5% | -1.4% |
| Systematic-taker | 18,301 | 12.4% | 0.8% | 24.4% | -1.58% | -895,313 | 29.1% | -3.2% |
| Mid-MM | 1,478 | 2.6% | 4.7% | 0.3% | -0.04% | -5,208 | 32.5% | -3.1% |
| Systematic-mixed | 2,002 | 1.6% | 1.5% | 1.7% | -1.79% | -132,496 | 31.8% | -2.4% |
| Retail | 30,959 | 1.2% | 0.2% | 2.1% | -5.37% | -290,434 | 30.4% | -20.5% |

| Persona | Wallets | % touched | % maker side | % taker side | PnL $, 30 days | May 2026 venue-wide |
|---|---:|---:|---:|---:|---:|---:|
| MMs (Pro-MM, Mid-MM) | 2,896 | 41.0% | 74.6% | 6.2% | +277,379 | 38.4% |
| Bots and algo | 23,445 | 57.8% | 25.1% | 91.7% | +13,055 | 56.3% |
| Retail | 30,959 | 1.2% | 0.2% | 2.1% | -290,434 | 5.3% |

Pro-MM, Fast-taker and Hybrid-bot together are 82.3% of touched volume (daily range 82% to 88%). Market makers
provide 74.6% of the maker side; bots and algo consume 91.7% of the taker side. Retail is 1.2% of touched volume.
Over the month $1.32M, about $44k a day, moved from Systematic-taker, Systematic-mixed and Retail to Pro-MM,
Fast-taker and Hybrid-bot. Note that Pro-MM wallets are only 29% profitable before LP rewards, with a median
of -1.7% per dollar: a few large makers earn, the rest live on rewards.

The proposed v2 split over the same window (modal daily cohort per wallet):

| v2 cohort | Wallets | % touched | % maker side | % taker side | PnL per $ | PnL $, 30 days | Wallets profitable |
|---|---:|---:|---:|---:|---:|---:|---:|
| Pro-MM | 1,693 | 37.5% | 68.2% | 5.6% | +0.18% | +305,421 | 28.4% |
| Part-time MM | 835 | 2.8% | 4.6% | 1.0% | -0.38% | -49,337 | 34.5% |
| Neutral bot | 2,035 | 22.7% | 12.8% | 33.0% | +1.50% | +1,557,025 | 29.4% |
| Directional bot | 2,327 | 15.6% | 8.1% | 23.3% | +0.12% | +88,002 | 39.8% |
| Session trader | 15,384 | 17.8% | 4.8% | 31.2% | -1.74% | -1,420,280 | 28.1% |
| Retail | 35,026 | 3.7% | 1.5% | 5.9% | -2.86% | -480,830 | 30.7% |

Rollup: MMs 40.3% of touched (+256,084), Machines 38.3% (+1,645,027), People 21.4% (-1,901,110). Neutral machines
earn +1.50% per dollar and took $1.56M; session traders lost $1.42M, three times what Retail lost.
The v2 ordering (Neutral bot and Pro-MM positive, Directional bot near zero, Session trader negative, Retail most
negative) holds over the full window. Result file: `data/pm_btc5m_cohorts30_2026-08-11_09-09.json` (per-month and
per-day tables included).

## 5. Kalshi

Kalshi's public tape has prices, sizes, timestamps and taker side, no identities and no channel. The
API accepts fractional contract counts (fixed-point strings, fractional trading on for every market since
2026-07-09), so order shape does not identify broker or app customers. No cohort grid can be built on it
and no automation share follows. What it does show, over 13 sampled days: every taker size class is
negative after Kalshi's fee of 0.07 x p x (1-p), so a Polymarket-style profitable taker-machine population
cannot exist there. Use Kalshi as the fee-model comparison, not as evidence about who trades.

## 6. What this means for Verdict

- **Liquidity is not the scarce input; paying flow is.** Recruit market makers and neutral machines with
  a reliable feed, cancels and settlement, and expect them within days. Plan the paying flow explicitly:
  HL-native directional traders, partner frontends via builder codes (Polymarket routes about 15% of its
  volume through 50 third-party frontends), and the maker pool as a bridge, not a business model.
- **No complete-set arbitrage on Verdict.** HIP-4 outcome markets are mirror books: buying YES is selling NO
  on the same book. The A plus B under 1 persona does not exist here. Do not pitch it.
- **Polymarket's machines are not migrating.** Zero of the top 100 Polymarket wallets are active on HIP-4
  (segmentation repo, cross-venue check). The observed path is HL perps traders into HIP-4.
- **Fees decide which machines you host.** Zero taker fee invites the neutral stale-quote machines that
  earn +1.4% per dollar off makers and people; Kalshi's 1.75c at even odds removes that edge. Verdict launches
  at fee scale 0 with no maker rebates on outcome markets, so settlement design (60-second CF average, dead
  band, second source) is what protects makers until a fee exists.
- **Contract compatibility before cross-venue volume.** A CF Benchmarks 60-second average is not the same
  instrument as a Chainlink 60-second TWAP or a Hyperliquid mark. Write the equivalence spec before
  projecting arbitrage demand.
- **Recruit makers and takers together, then measure after incentives.** Paired pilot on a small contract
  set, signed orders and fills recorded end to end, continued use tracked through at least one full weekly
  cycle and one incentive step-down. Scorecard: repeat fee-paying strategies, depth at agreed sizes, LP
  profitability after hedges and rewards, venue revenue after incentives, rejected orders and settlement
  failures, concentration by firm.

## 7. Evidence boundaries

- Cohorts are behaviour over one UTC day at proxy-wallet level. Owner aggregation (Dune
  `users_address_lookup`) would merge multi-proxy firms and lower the machine wallet counts; dollar shares
  would not move much. Multi-day assignment (modal cohort) is the right unit once Aug 30 and Sep 8 land.
- Two of 288 markets hit the data-api pagination limit at 11,000 records and are truncated.
- PnL is gross settlement markout per leg, no fees (none charged), no rewards, no positions carried in or
  out of the day, no external hedges. It measures transfer between cohorts on the venue, not firm profit.
- No identities. "Session trader" and "Retail" are inferred from sleep gap, dollar-typed sizing and
  early exits; "Neutral bot" from two-sided buying. Reaction latency, the decisive test for machines,
  needs a millisecond capture of the CLOB websocket; public timestamps are whole seconds.
- Historical tables in `2026-09-04-who-trades-short-term-btc-binaries.md` use the older
  bot/heavy/manual labels; the mapping is in its section 0.

Sources: Polymarket data-api `/trades` (takerOnly true and false) and gamma `/events?series_id=10684`;
Roni-1997/polymarket-segmentation README and findings (May 2026); Kalshi API fixed-point documentation;
Hyperliquid HIP-4 documentation (mirror books); Verdict launch board (fee scale, maker pool).
