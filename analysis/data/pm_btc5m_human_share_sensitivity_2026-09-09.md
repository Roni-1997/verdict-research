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
| Dollar-denominated orders only (40%+ of buy orders exact-dollar, 3+ buys; labelled "website signature" until 2026-09-10, see addendum) | 36.3% |
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

## Addendum 2026-09-10: wallet contract type does not separate humans from bots

Every one of the 7,303 taker wallets was typed from its on-chain bytecode (eth_getCode on Polygon) and the
implementation behind it (Blockscout verified sources). Script: `scripts/pm_wallet_type_2026-09-10.py`.

| Wallet type | How it is created | Wallets | Taker $ | Wallets active 16+ hours |
|---|---|---|---|---|
| Polymarket DepositWallet, beacon proxy (passkey and session-signer build, source verified 2026-07-28) | current Polymarket web/app onboarding | 3,067 (42%) | 31.0% | 10% |
| Polymarket DepositWallet, ERC-1967 proxy (build verified 2026-05-01) | Polymarket web onboarding, May to Jul 2026 | 1,334 (18%) | 17.2% | 13% |
| Polymarket ProxyWallet (legacy Magic-link clone, implementation 0x44e9...eB4f) | email login before 2026 | 1,557 (21%) | 28.0% | 11% |
| Gnosis Safe proxy | browser-wallet login | 1,210 (17%) | 19.4% | 16% |
| Bare EOA | API only; the site never trades from a bare key | 73 (1%) | 2.5% | 22% |
| EIP-7702 delegated EOA (MetaMask delegator and others) | API or smart-account users | 62 (1%) | 2.0% | 26% |

The bot core (300+ fills/day, 232 wallets, 49% of taker $) sits on every Polymarket-created wallet type: 45 legacy
ProxyWallets carry 15.2% of all taker $, 63 Safes 9.1%, 113 DepositWallets 21.3%. Only 11 of the 232 are bare or
7702 EOAs. Two conclusions. Wallet type is not a bot detector: bots reuse accounts that were created through the
site and then drive them over the API (exported key or session signer). The "bare EOA means API" test is true by
construction but covers 2.5% of dollars.

Exact-dollar sizing is not a website exclusive either. Bare-EOA wallets, which cannot have used the site, still
place 13 to 28% exact-dollar buys, because the API market-order helper also takes a dollar amount. The signature
keeps some power (39 to 40% exact-dollar buys in the sub-100-fill tiers against 18% in the 300+ tier) but it
measures order denomination, not the client. Public trade records carry no client, API-key or builder field, so
the only clean origin evidence available to an outsider is behavioural: fills per day, hours active, same-second
orders across markets, two-sided activity in one window, and reaction latency to the reference price (which needs
a live millisecond capture of the CLOB websocket; the public trade timestamps are whole seconds).

## Revised classifier: the sleep gap (2026-09-10)

Objection tested: "a human does not make 50 fills a day; the heavy band is bots". Signal: the longest gap between a
wallet's orders inside the UTC day, wrap-around included. A person trading in sessions leaves a gap of several
hours; a script does not. Script: `scripts/pm_reclassify_sleep_gap_2026-09-10.py`.

| Fills/day tier | Share of taker $ | $ from wallets with a gap of 8h+ | 6-8h | 3-6h | under 3h | Median windows | Median orders | Median active hours |
|---|---|---|---|---|---|---|---|---|
| under 30 | 12.2% | 85% | 4% | 11% | 0% | 4 | 5 | 2 |
| 30-99 | 19.5% | 55% | 8% | 14% | 22% | 32 | 48 | 10 |
| 100-299 | 19.5% | 34% | 9% | 15% | 42% | 76 | 141 | 16 |
| 300+ | 48.8% | 6% | 4% | 12% | 78% | 162 | 460 | 24 |

The heavy band is two populations:

| Band | Sleeps (gap 6h+) | Wallets | Share of band $ | Median active hours | Median windows | Exact-dollar buys | Sells | Modal order size share | PnL to settlement |
|---|---|---|---|---|---|---|---|---|---|
| 30-99 | yes | 927 | 63% | 7 | 26 | 41% | 26% | 9% | -0.7% |
| 30-99 | no | 431 | 36% | 19 | 43 | 5% | 4% | 20% | +0.6% |
| 100-299 | yes | 293 | 42% | 10 | 55 | 32% | 30% | 6% | -3.6% |
| 100-299 | no | 253 | 57% | 23 | 106 | 9% | 8% | 13% | -2.2% |

Sleepers size in dollars, exit a quarter of the time, trade 26-55 windows over a 7-10 hour session and lose like
retail. Non-sleepers run 19-23 hours, size in shares, repeat sizes, never exit, and the 30-99 group earns. The
100-299 non-sleepers lose 2.2%: machines, but unprofitable ones (retail-run scripts). The 45 wallets in the 300+
tier that do show a gap of 8h+ are machines that ran part of the day (median 366 orders, 1.1 fills per order, 50%
two-sided).

Revised rule: bot = 300+ fills, or 30+ fills with no gap of 6h+, or two-sided buying in 40%+ of windows (5+
windows). Sep 9: bots 68.9% of taker $ (1,111 wallets, PnL +0.74%), humans 31.1% (PnL -2.76%): manual 12.0%,
session traders 30-99 fills 12.0%, session traders 100-299 fills 7.2%. Sensitivity: gap under 4h gives 65.3% bots,
under 8h 71.9%. Report rule for comparison: 60.0% bots (+0.86%), 40.0% humans (-2.15%). PnL is an independent
check: it was not used to build either rule, and both rules separate a class that earns from a class that loses.

Bias to note: a bot that started or stopped mid-day shows a long gap and is counted as a sleeper, so the revised
share is a floor on machines, not a ceiling.

## Can the fills threshold go? Sleep alone, sleep plus density, and the scheduled-bot objection (2026-09-10)

Objection tested: "drop the fills filter and use the sleep gap alone", with the counter-objection that a bot run only
during US stock hours also sleeps. Density = windows traded divided by 5-minute windows available inside the wallet's
waking span. Scripts: `scripts/pm_features_and_rules_2026-09-10.py`, `scripts/pm_pull_btc5m_day.py`.

| Rule | Sep 9 bot share of taker $ | Sep 9 bot PnL / human PnL | Aug 30 bot share | Aug 30 bot PnL / human PnL |
|---|---|---|---|---|
| Report: 300+ fills, or 100+ across 16h | 59.9% | +0.86% / -2.15% | 59.2% | +1.54% / -2.12% |
| Sleep-gap: 300+, or 30+ with no 6h gap, or two-sided | 68.9% | +0.74% / -2.76% | 67.9% | +1.27% / -2.56% |
| Pure sleep, no fills filter: bot = no 6h gap | 63.2% | +0.84% / -2.39% | 57.3% | +1.97% / -2.55% |
| Sleep plus density, no fills filter: no 6h gap, or dense 4h+ span in share sizes, or two-sided | 67.2% | +0.78% / -2.65% | 64.1% | +1.56% / -2.66% |
| Combined: sleep-gap rule plus dense scheduled sleepers | 69.4% | +0.74% / -2.82% | 68.2% | +1.25% / -2.56% |
| Whole heavy band = bots (30+ fills) | 87.8% | +0.17% / -4.07% | 89.2% | +0.17% / -1.06% |

Findings.
- Sleep alone lands within 6 to 11 points of the full rule and keeps the PnL separation, so the fills count is not
  doing the work; the sleep gap is. What sleep alone misses: sleeping machines. 317 wallets (7.5% of Sep 9 $) show a
  6h+ gap but are two-sided in 45% of their windows, size in shares (15% exact-dollar) and trade half the windows of an
  8.8h span; a bot that ran part of the day looks asleep for the rest of it.
- The US-stock-hours bot population is small. Sleepers with 30+ fills whose waking span sits inside 13:00-21:00 UTC are
  5.0% (Sep 9) and 6.5% (Aug 30) of taker $, and 58 to 68% of their buy orders are exact dollars: US day traders, not
  scripts. The dense share-typed subset, the actual scheduled bots, is 0.5 to 0.7% of taker $. Sleep start times are
  spread flat across all 24 UTC hours when weighted by dollars, so there is no single bedtime cluster to exploit.
- Density is the right complement to sleep but needs a span condition: 63 wallets (1.2% of $) trade 80%+ of the
  windows in a 1.5-hour session with 85% exact-dollar orders and 44% sells. Those are human binges. The scheduled-bot
  clause therefore requires a 4h+ span and share-typed sizes; it adds 0.5% of $.
- Calling the whole heavy band bots (87 to 89%) is refuted by PnL: the bot class's edge collapses to +0.17% because
  it absorbs the losing session traders.
Working rule from here: combined. Bot = 300+ fills, or 30+ fills with no 6h gap, or two-sided buying in 40%+ of
windows, or a dense (50%+ of windows) share-typed run of 4h+ that then stops. Bots 68 to 69% of taker $ on both days.

