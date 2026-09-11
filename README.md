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

## Contents

| Document | What it covers |
|---|---|
| [analysis/2026-09-10-verdict-flow-attribution.md](analysis/2026-09-10-verdict-flow-attribution.md) | Who trades Polymarket BTC 5-minute markets, in the seven-cohort framework of [polymarket-segmentation](https://github.com/Roni-1997/polymarket-segmentation); PnL by cohort; what it means for Verdict |
| [analysis/2026-09-04-who-trades-short-term-btc-binaries.md](analysis/2026-09-04-who-trades-short-term-btc-binaries.md) | Seven months of Polymarket BTC 5m and 15m and 13 days of Kalshi BTC 15m: product life cycle, personas, behaviour, channel evidence |
| [analysis/data/pm_btc5m_trailing30_2026-08-11_09-09.md](analysis/data/pm_btc5m_trailing30_2026-08-11_09-09.md) | Every taker fill for 30 consecutive days: machine share day by day, profitability by persistence, size and cadence |
| [analysis/data/](analysis/data/) | Derived datasets, sensitivity notes, cohort tables, Kalshi order-shape evidence |
| [analysis/reports/](analysis/reports/) | The three source reports behind the September analysis |
| [analysis/scripts/](analysis/scripts/) | Pull and classification scripts (Polymarket data-api, gamma, Kalshi) |

Raw Kalshi prints for five sampled days are attached to the `data-2026-09` release. Wallet identities are never published.
