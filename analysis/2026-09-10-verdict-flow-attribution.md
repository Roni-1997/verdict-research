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

## 1. The claim, in plain language

Short-term crypto binaries are traded by machines. Over the 30 days to September 9, market makers and fast
trading bots were 82% of all volume on Polymarket's Bitcoin 5-minute markets (section 4c). Market makers
posted 75% of all resting orders; bots took 92% of all aggressive trades. People placing fewer than 10
trades a day were 1.2% of volume. A venue does not need a consumer funnel to get liquidity: Polymarket's
5-minute market was 46% bots on its second day.

What every such venue also needs is someone for the machines to win from. People, meaning casual bettors
plus active traders using tools, were about a fifth of volume and a third of aggressive trades, and they
lost money on every one of the 30 days while the machines made money on every one
(`data/pm_btc5m_trailing30_2026-08-11_09-09.md`). Only 30% of wallets finished the month ahead; the typical
wallet lost 5.6% of what it traded. About $44,000 a day moved from people to machines and market makers.
When Polymarket's inflow of new wallets fell 80% over the spring, bot volume fell 43% with it: machines
follow the paying flow, they do not create it.

The investor sentence: Verdict does not need its own retail app, because the machines are the liquidity
and they arrive on their own. It does need the flow that pays, and that comes from Hyperliquid's own
traders one click away, from partner front ends carrying Verdict's builder code, and from a market-maker
pool that bridges the early days. The machines are the liquidity. The front ends are the customers.

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

## 4d. Six months, 2026-03-10 to 2026-09-09: the grid over the whole period and month by month

Every trade, both legs, for 184 days: 427,091 wallets, $4,651M traded (both sides counted; $2,325M
single-counted, $12.6M a day). One cohort per wallet for the whole period, following the segmentation
repo's definitions: cadence is fills per active day across the period and maker share is the wallet's maker volume
over its total. Profit and loss is at settlement, before liquidity rewards; no fees were charged on these markets.

Over the period 29% of wallets ended ahead, the typical wallet lost 6.3% of what it traded, the top 1% of
wallets took 86% of all gains and the top 0.1% took 52%. About $104k a day moved from the
cohorts that lose to the cohorts that win.

### Month by month

| Month | Days | Volume per day, $M single-counted | Wallets | Market makers | Bots and active traders | Casual bettors | Bots (v2) | People (v2) | $k per day from people to bots and makers | Wallets profitable in the month |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| March 2026 | 22 | 21.3 | 123,671 | 41% | 57% | 1.3% | 36% | 23% | 190 | 30% |
| April 2026 | 30 | 15.8 | 145,270 | 44% | 54% | 1.8% | 31% | 25% | 136 | 31% |
| May 2026 | 31 | 11.3 | 114,946 | 40% | 59% | 1.5% | 34% | 27% | 47 | 32% |
| June 2026 | 30 | 12.3 | 100,994 | 43% | 56% | 1.4% | 32% | 25% | 104 | 33% |
| July 2026 | 31 | 11.4 | 83,807 | 42% | 57% | 1.1% | 34% | 25% | 79 | 33% |
| August 2026 | 31 | 7.8 | 61,970 | 41% | 58% | 1.2% | 34% | 24% | 57 | 32% |
| September 2026 | 9 | 7.4 | 24,604 | 38% | 60% | 1.4% | 42% | 20% | 69 | 34% |

Bots and market makers (the three fast cohorts) held between 77% and 83% of volume. Casual bettors held between 1.1% and 1.8%.
Volume per day went from 21.3M in March 2026 to 7.4M in September 2026 (range 7.4M to 21.3M). The daily transfer from people to bots and market makers went from 190k in March 2026 to 69k in September 2026 (range 47k to 190k).

### The grid over the whole period

| Who | Wallets | Share of volume | Share of resting orders | Share of aggressive trades | PnL per $ | PnL $, 184 days | Wallets profitable | Median PnL per $ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Market makers, full time (Pro-MM) | 6,166 | 38.8% | 68.8% | 7.3% | +0.39% | +7,027,551 | 33.2% | -1.2% |
| Fast bots taking liquidity (Fast-taker) | 16,518 | 20.5% | 3.5% | 38.3% | +0.46% | +4,406,113 | 34.0% | -1.1% |
| Fast bots on both sides (Hybrid-bot) | 6,155 | 19.5% | 19.0% | 20.0% | +0.79% | +7,132,119 | 35.1% | -1.0% |
| Active traders using tools (Systematic-taker) | 146,823 | 14.5% | 1.2% | 28.5% | -2.18% | -14,748,178 | 25.4% | -4.0% |
| Market makers, part time (Mid-MM) | 8,572 | 2.7% | 4.8% | 0.5% | +0.40% | +507,533 | 36.2% | -2.4% |
| Active traders, mixed (Systematic-mixed) | 16,070 | 2.7% | 2.4% | 3.0% | -0.75% | -942,943 | 31.3% | -2.4% |
| Casual bettors (Retail) | 226,787 | 1.2% | 0.2% | 2.3% | -5.84% | -3,364,951 | 29.6% | -19.9% |

| Persona | Wallets | Share of volume | Share of resting orders | Share of aggressive trades | PnL $ | Venue-wide share, May 2026 |
|---|---:|---:|---:|---:|---:|---:|
| Market makers | 14,738 | 41.5% | 73.6% | 7.9% | +7,535,084 | 38.4% |
| Bots and active traders | 185,566 | 57.2% | 26.1% | 89.8% | -4,152,890 | 56.3% |
| Casual bettors | 226,787 | 1.2% | 0.2% | 2.3% | -3,364,951 | 5.3% |

Market makers and fast bots together are 79% of volume. Market makers post 74% of resting orders; bots and
active traders take 90% of aggressive trades. Casual bettors are 1.2% of volume and 53% of wallets.

### The proposed v2 split over the whole period

| Who (v2) | Wallets | Share of volume | Share of resting orders | Share of aggressive trades | PnL per $ | PnL $ | Wallets profitable |
|---|---:|---:|---:|---:|---:|---:|---:|
| Market makers, full time | 6,909 | 37.4% | 65.5% | 8.0% | +0.41% | +7,086,794 | 30.8% |
| Market makers, part time | 4,871 | 4.1% | 6.8% | 1.3% | +0.49% | +944,817 | 37.1% |
| Bots trading both sides | 13,323 | 18.1% | 10.4% | 26.2% | +1.13% | +9,472,900 | 26.4% |
| Bots betting a direction | 14,514 | 13.9% | 7.1% | 21.1% | +0.02% | +153,583 | 35.4% |
| Active traders using tools | 120,886 | 19.7% | 6.3% | 33.8% | -1.20% | -10,978,920 | 25.2% |
| Casual bettors | 266,588 | 6.7% | 4.0% | 9.6% | -2.13% | -6,661,932 | 29.8% |

Rollup: market makers 41.6% of volume (+8,031,611), bots 32.0% (+9,626,484), people 26.4% (-17,640,853).

The v2 label over a long window is the wallet's most common daily class, so a wallet that ran as a bot on its busy
days but traded by hand on most days is counted as a person for the whole period, and its bot-day volume goes with
it. That is why bots read lower and people higher here than in any single month; the month-by-month table above is
the better read for the v2 split, and the v1 grid (cadence per active day, maker share over the window) does not
have this problem.

### Who is still standing after six months

| Active days in the period | Wallets | Share of volume | Wallets profitable | Median PnL per $ |
|---|---:|---:|---:|---:|
| 1 day | 167,025 | 1.0% | 28.5% | -23.0% |
| 2 to 4 days | 137,247 | 3.4% | 25.6% | -8.1% |
| 5 to 9 days | 56,673 | 5.3% | 29.7% | -3.2% |
| 10 to 19 days | 33,423 | 10.5% | 32.5% | -1.8% |
| 20 or more days | 32,723 | 79.7% | 36.9% | -0.8% |

Result file with per-month, per-day and persistence tables: `data/pm_btc5m_cohorts_6m_2026-03-10_09-09.json`.

## 5. Kalshi

Kalshi's public tape has prices, sizes, timestamps and taker side, no identities and no channel. The
API accepts fractional contract counts (fixed-point strings, fractional trading on for every market since
2026-07-09), so order shape does not identify broker or app customers. No cohort grid can be built on it
and no automation share follows. What it does show, over 13 sampled days: every taker size class is
negative after Kalshi's fee of 0.07 x p x (1-p), so a Polymarket-style profitable taker-machine population
cannot exist there. Use Kalshi as the fee-model comparison, not as evidence about who trades.

## 6. What this means for Verdict

- **Liquidity is not the scarce input; paying flow is.** Market makers and bots come within days if the
  price feed, cancels and settlement are reliable. The flow that pays has to be planned for: Hyperliquid's
  own directional traders, partner front ends routing through Verdict's builder code (Polymarket gets
  about 15% of its volume through 50 third-party front ends), and a market-maker pool as a bridge, not as
  the business.
- **No buy-both-sides arbitrage on Verdict.** On HIP-4 a market is one order book: buying YES is the same
  as selling NO, so the "YES plus NO for less than a dollar" trade that Polymarket bots run cannot exist
  here. Do not pitch it.
- **Polymarket's bots are not coming.** None of its 100 largest wallets is active on HIP-4 (segmentation
  repo, cross-venue check). The traders arriving on HIP-4 come from Hyperliquid perps.
- **Fees decide which bots you host.** With no taker fee, the bots that earn are the ones picking off
  stale quotes, about 1.4 cents per dollar, paid by market makers and people; Kalshi's fee of 1.75 cents
  at even odds removes that edge. Verdict launches with fees off and no maker rebates on outcome markets,
  so the settlement design (a 60-second CF Benchmarks average, a dead band, a second price source) is what
  protects the market makers until a fee exists.
- **Check that contracts match before counting on cross-venue traders.** A 60-second CF Benchmarks
  average is not the same instrument as a Chainlink 60-second average or a Hyperliquid mark price. Write
  the equivalence down before projecting arbitrage demand.
- **Recruit market makers and traders together, then judge after incentives step down.** Run a paired
  pilot on a few contracts, record every order and fill, and track use through a full week and one cut in
  rewards. Scorecard: repeat fee-paying traders, depth at agreed sizes, market makers profitable after
  hedges and rewards, venue revenue after incentives, rejected orders and settlement failures,
  concentration by firm.

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
