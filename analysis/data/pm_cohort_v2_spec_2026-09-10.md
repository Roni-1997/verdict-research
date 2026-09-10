# Cohort grid v2: same axes as polymarket-segmentation, sharper operation-mode axis, plus directionality

Proposal (2026-09-10) for the seven-cohort grid in Roni-1997/polymarket-segmentation, based on what the BTC 5m
wallet data measured today. v1 is kept and reported alongside v2 in `pm_btc5m_cohorts_2026-09.md`.

## What v1 gets wrong, with the evidence

| v1 assumption | What the data shows |
|---|---|
| Cadence is fills per active day | One order sweeping three price levels is three fills. Machines average 1.1 fills per order, people more. Cadence should count orders (wallet, market, side, second). |
| 100+ fills a day is "clearly automated" | Wallets at 100-299 fills that show a 6h+ gap trade 10 active hours, size 32-39% of buys in exact dollars, exit 30% of positions and lose 2.3 to 3.6% per dollar. That is a person with a tool. The 100-299 wallets with no gap trade 23 hours, size in shares, never exit. |
| 10-100 fills a day is one cohort (Systematic-taker) | It is two populations: sleepers (63% of the band's dollars, PnL -0.7 to -3.6%) and non-sleepers (36%, PnL +0.6%). |
| Maker share separates market makers from takers | Market-neutral stale-quote picking (both sides bought in the same window at a pair cost near $1) appears at every maker share. The top 10 takers are two-sided in 87-100% of their windows. Directional machines and neutral machines have opposite economics (Sep 9: 300+ tier +1.45%, no-sleep 100-299 directional tier -2.18%). |
| One-day gaps are noise | Bedtime consistency is weak (43% of humans within 2h day to day) but the gap itself is stable: sleeping wallets sleep the next day too (92%). |

## v2 decision tree (per wallet per active day; assign the modal cohort over a window)

1. Orders per active day under 10: **Retail**, any maker share.
2. Operation mode:
   - **unattended** = no gap of 6h+ between orders in the UTC day (wrap-around), or 16+ distinct active hours;
   - **part-day machine** = both sides bought in 40%+ of windows traded (5+ windows), or 50%+ of available windows traded over a 4h+ span with under 20% exact-dollar buys;
   - **session** = neither (a gap, sparse, dollar-typed or exiting).
   Evidence: no-sleep wallets have 5-9% exact-dollar buys and 4-8% sells; sleepers 32-42% and 26-30%. Human binges (80%+ of windows for 1.5h, 85% exact-dollar) are excluded by the span and dollar conditions. Scheduled US-hours machines are 0.5-0.7% of dollars and are caught by the two-sided or dense test, not by timing.
3. Role: maker share of touched volume 70%+ = maker role.
4. Directionality: **neutral** = both sides bought in 40%+ of windows; else **directional**.

| Maker share | Unattended or part-day machine | Session (10+ orders) |
|---|---|---|
| 70%+ | **Pro-MM** | **Part-time MM** |
| under 70%, neutral | **Neutral bot** (latency, stale-quote, inventory) | Session trader |
| under 70%, directional | **Directional bot** (momentum scripts, copy-trading engines) | **Session trader** (tool-assisted human) |

Six cohorts. Rollup: MMs (Pro-MM, Part-time MM), Machines (Neutral bot, Directional bot), People (Session trader,
Retail). v1 Systematic-mixed and Hybrid-bot dissolve into the role and directionality cells.

## Validation rule

PnL to settlement is never an input. After classification it should order as: Neutral bot and Pro-MM positive,
Directional bot near zero or negative, Session trader negative, Retail most negative. If a cohort's PnL sits on
the wrong side, the thresholds are wrong, not the wallets.

## Units and scope

Orders not fills; touched volume both sides, single-counted = half; proxy level here, owner level where Dune's
`users_address_lookup` is available (changes wallet counts in the machine cohorts, not dollar shares); assign over
a 30-day window as the modal daily cohort, with cadence per active day.
