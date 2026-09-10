# How much of Polymarket BTC 5m taker volume is human? Sensitivity to the classifier

Re-measured on 2026-09-10 from every taker fill on all 288 BTC 5-minute markets of 2026-09-09 UTC:
476,247 fills, 7,303 taker wallets, $7.48M taker premium. Orders = one wallet, one market, one side,
one second. "Website signature" = buy orders whose premium is an exact dollar amount (the web app takes
dollar amounts, the API takes share counts); "API signature" = under 15% of buy orders exact-dollar.

| Rule for "human" | Human share of taker $ |
|---|---|
| Report rule: under 300 fills/day and not 100+ fills across 16+ hours | 40.0% |
| Under 100 fills/day (drops the 100-299 tier) | 31.7% |
| Under 100 fills/day and not two-sided in 40%+ of its markets | 30.8% |
| Website signature only (40%+ of buy orders exact-dollar, 3+ buys) | 36.3% |
| Manual only (under 30 fills/day) | 12.2% |

Where the disputed tiers sit:

| Fills per day | Wallets | Share of taker $ | Website-signature share of that $ | API-signature share | Two-sided (40%+ of markets) |
|---|---|---|---|---|---|
| 30-99 | 1,337 | 19.5% | 62% | 32% | 3% |
| 100-299 | 542 | 19.5% | 55% | 31% | 7% |
| 300+ | 232 | 48.8% | n/a | n/a | 63% |

Reading: the unambiguous human floor is 12% (manual wallets). The 30-99 tier is mostly website-driven
by signature. The 100-299 tier, which the long-run report labels "script runners", is still majority
website-signature by dollars, so it is not cleanly bots either; about a third of both tiers is
API-shaped. The 300+ tier is the bot core, and 63% of its dollars are two-sided market making or
latency trading. Defensible statement: roughly 31 to 40% of 5-minute taker volume is human, the
central estimate about a third; the previously published 35% (Sep 1-2) sits inside that range.
A bot submitting exact-dollar sizes over the API would be counted as website; partial fills can make a
human order look non-round, so the signature test if anything undercounts humans.

Source: Polymarket data API `/trades` per market (taker legs) and gamma `/events?series_id=10684`.
