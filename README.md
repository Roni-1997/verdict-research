# verdict-research

Measured market research for Verdict, an outcome-market venue on Hyperliquid (HIP-4).
Everything here is derived from venue APIs; units are stated in each document. Start with
`analysis/2026-09-04-who-trades-short-term-btc-binaries.md`.

| Path | What |
|---|---|
| `analysis/2026-09-04-who-trades-short-term-btc-binaries.md` | Synthesis: who trades Polymarket 5m/15m and Kalshi 15m BTC binaries, with a verification log |
| `analysis/reports/` | The underlying reports (deep dives, long-run series, six-month product tables) |
| `analysis/data/` | Derived aggregates that survived, with schemas |
| Release `data-2026-09` | Raw Kalshi KXBTC15M prints for five sample days |

Unit trap to remember: Polymarket's published volume counts both legs of a trade and is about 2x the
one-sided taker dollars used throughout these documents. Kalshi reports $1-notional contracts.

Wallet-level identities are deliberately excluded from this repository.
