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
