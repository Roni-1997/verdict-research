# Kalshi KXBTC15M: how much taker flow is automated? Order-shape evidence (2026-09-10)

Kalshi publishes no trader identities, so a wallet-style bot share cannot be measured. This note uses the only
origin signal in the public tape: whether a taker order's contract count is fractional (a dollar amount was typed
into Robinhood, Webull or the Kalshi app and converted) or an integer (contract count typed, or an API order).
Prints within 2 ms on the same side of the same market are one order. Three raw days from release `data-2026-09`
(Aug 16, 21, 31), 3.98M taker orders, 601M contracts. Scripts: `scripts/kalshi_order_shape_2026-09-10.py`,
`scripts/kalshi_burst_position_2026-09-10.py`.

| Order shape | Size (contracts) | Share of orders | Share of contracts | Taker PnL before fee | After fee | Placed in last 2 min | At price extremes (<=10c or >=90c) | 20:00-03:00 UTC |
|---|---|---|---|---|---|---|---|---|
| Fractional | all | 76.8% | 74.5% | -0.48% | -2.54% | 24% | 39% | 36% |
| Fractional | <=50 | 51.6% | 4.9% | -0.30% | -3.13% | 10% | 18% | 36% |
| Fractional | 51-500 | 21.1% | 21.4% | -0.52% | -3.08% | 15% | 28% | 36% |
| Fractional | 501-5,000 | 3.9% | 32.9% | -0.04% | -2.08% | 24% | 40% | 35% |
| Fractional | >5,000 | 0.2% | 15.3% | -1.34% | -2.61% | 41% | 59% | 38% |
| Integer | all | 23.2% | 25.5% | +0.22% | -1.86% | 19% | 30% | 36% |
| Integer | <=50 | 14.9% | 1.3% | +0.85% | -1.45% | 13% | 26% | 35% |
| Integer | 51-500 | 6.6% | 7.5% | -0.05% | -2.38% | 15% | 26% | 36% |
| Integer | 501-5,000 | 1.6% | 14.2% | +0.30% | -1.80% | 18% | 29% | 36% |
| Integer | >5,000 | 0.0% | 2.5% | +0.22% | -1.09% | 38% | 47% | 36% |

Fee = 0.07 x p x (1-p) per contract (Kalshi's published schedule); 26% of integer contracts are round lots of 50.

Burst test: in chains of 8 or more same-side taker orders with gaps under 1 second, integer orders are 25.8% of
contracts in the first 100 ms and 26.0% after 3 seconds. Integer-sized flow does not lead the bursts, so the
API-shaped class is not a fast-reacting population. Only one KXBTC15M window trades at a time (every 10-second
bucket of the three days contains exactly one ticker), so same-millisecond cross-market detection is not possible.

Reading. Three quarters of taker contracts are dollar-typed, which is the broker and app path. The integer quarter
is the ceiling for API-driven taker flow and it behaves like the rest: same evening rhythm, same burst timing,
0.7 points better before fees, negative after fees. No size class of either shape earns after fees, against a
Polymarket 5m bot core that earns about +1.6% at settlement. The fee schedule (1.75c at 50c) removes the latency
edge that funds Polymarket's bots. Automated taker flow on Kalshi 15m is therefore at most about a quarter of
contracts and probably well under it; the maker side is professional market makers and is automated by nature.
Compare Polymarket 5m: 60 to 69% of taker dollars from wallets with 300+ fills a day, 72 to 86% of maker legs.
