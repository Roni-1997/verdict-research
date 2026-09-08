# Data

Derived aggregates that survived the analysis sessions. Raw pulls are large and live in the
`data-2026-09` GitHub release (Kalshi, 5 of the 13 sample days) or are gone (Polymarket raw fills
were not retained; re-pull from `data-api.polymarket.com/trades` per market if needed).

## pm_btc5m_market_days.jsonl (9,790 rows)
One row per Polymarket BTC 5-minute market on each of the 34 sample days (Feb 13 to Aug 30 2026,
one day every 6 days). Fields: `day` (UTC sample day), `cid` (condition id), `end` (window end,
unix seconds), `headline_vol` (Polymarket's reported volume, both legs), `taker_prem` (one-sided
taker dollars, shares x price, measured from fills), `fills` (taker fills), `wallets` (unique taker
wallets in that market).

## kalshi_kxbtc15m_days.jsonl (13 rows)
One row per Kalshi KXBTC15M sample day (Jul 2 to Aug 31 2026, every 5th day, all 96 windows).
Fields: `day`, `markets`, `trades` (prints), `orders` (reconstructed taker orders: prints within 2 ms
on the same side of the same market), `contracts`, `premium` (USD), `frac_orders` (share of orders
with fractional contract counts), `round_dollar_orders`, `bins` keyed by order size (`<=50`,
`51-500`, `501-5000`, `>5000`) with `orders`, `contracts_share`, `avg_px`, `pnl_pre`, `pnl_post`
(taker PnL to settlement per premium dollar before/after the published fee), `late2m` (share placed
in the last 2 minutes), `mid` (35-65c), `ext` (<10c or >=90c); plus hour-of-day shares.

## Release asset: kalshi raw prints (`data-2026-09`)
`2026-08-11.jsonl.gz` ... `2026-08-31.jsonl.gz`, one JSON array per print:
`[ticker, created_time (unix s), taker_side, count (contracts), yes_price ($), market_close (unix s), result]`
(field meaning inferred from values; verify against Kalshi `/markets/trades` before relying on it).
The other 8 sample days (Jul 2 to Aug 6) were not retained. Kalshi serves trades only for markets
settled within roughly the last 68 days, so the July days can no longer be re-pulled.
