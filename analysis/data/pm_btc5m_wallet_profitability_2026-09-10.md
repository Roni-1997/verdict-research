# What share of wallets is profitable on Polymarket BTC 5m? (2026-09-10)

Settlement PnL per wallet: a buy of an outcome pays 1 if it wins, a sell the reverse, summed over the
wallet's legs. Gross: no fees (none charged on these markets), no LP rewards, no positions carried
across days (5-minute markets settle within the day). "Profitable" = more than $0.01. Taker legs for
seven sampled days re-pulled from the data-api; both legs for Aug 30 and Sep 9. Machines and people
use the combined rule from `pm_btc5m_human_share_sensitivity_2026-09-09.md`.

## Per day, taker legs

| Day | Wallets | Profitable | Median PnL per $ | Machines profitable | People profitable | Under 10 fills | 300+ fills | Top 1% of wallets' share of all gains |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026-04-08 | 21,820 | 43.0% | -2.81% | 48.6% | 42.2% | 41.9% | 57.2% | 61% |
| 2026-05-02 | 14,870 | 43.8% | -2.99% | 48.2% | 43.2% | 44.5% | 57.4% | 57% |
| 2026-06-25 | 14,019 | 47.1% | -1.02% | 55.3% | 45.7% | 43.7% | 65.5% | 49% |
| 2026-07-31 | 10,424 | 51.0% | +0.32% | 54.4% | 50.3% | 51.8% | 57.1% | 50% |
| 2026-08-30 | 7,535 | 47.4% | -0.84% | 52.6% | 46.5% | 46.5% | 57.4% | 52% |
| 2026-09-08 | 7,316 | 46.1% | -1.28% | 52.2% | 44.9% | 44.5% | 59.6% | 54% |
| 2026-09-09 | 7,303 | 45.6% | -1.33% | 49.1% | 44.9% | 44.7% | 59.9% | 51% |

## Pooled over the seven days (60,904 wallets)

| Group | Wallets | Profitable | Median PnL per $ | Share of taker $ |
|---|---:|---:|---:|---:|
| Seen on 1 sample day | 47,618 | 41.2% | -4.25% | 35.6% |
| Seen on 2 | 8,156 | 46.0% | -0.94% | 17.7% |
| Seen on 3 to 4 | 4,092 | 52.4% | +0.32% | 21.0% |
| Seen on 5 to 7 | 1,038 | 56.0% | +0.62% | 25.8% |
| All | 60,904 | 42.9% | -2.71% | 100% |

| Total traded across the days | Wallets | Profitable | Median PnL per $ |
|---|---:|---:|---:|
| Under $100 | 35,562 | 38.7% | -9.53% |
| $100 to $1k | 17,798 | 46.5% | -0.88% |
| $1k to $10k | 6,487 | 52.6% | +0.35% |
| $10k to $100k | 979 | 58.5% | +0.75% |
| $100k and up | 78 | 79.5% | +1.68% |

## Both legs, by cohort (share of wallets profitable, median PnL per $)

| Cohort | Aug 30 | Sep 9 |
|---|---|---|
| Pro-MM | 45.1%, -0.25% | 48.1%, -0.31% |
| Fast-taker | 50.9%, +0.08% | 45.9%, -0.37% |
| Hybrid-bot | 45.8%, -0.28% | 40.4%, -0.91% |
| Systematic-taker | 46.0%, -1.07% | 43.8%, -1.70% |
| Mid-MM | 43.1%, -3.80% | 42.3%, -3.28% |
| Systematic-mixed | 54.0%, +0.66% | 53.8%, +0.72% |
| Retail | 43.9%, -9.20% | 41.3%, -14.58% |
| All | 45.6% | 43.4% |

## Reading

- By count it looks like a coin flip: 43 to 51% of wallets end a day ahead, because a five-minute
  binary is close to 50/50 and a wallet with two bets ends positive half the time. The edge shows in
  dollars, not counts: the median wallet loses 1 to 3% of what it trades, one-day wallets lose 4%, and
  the smallest wallets lose 9.5%.
- Profitability rises with persistence and size: 41% of one-day wallets are ahead against 56% of
  wallets seen on five or more sample days; 39% of wallets trading under $100 against 80% of the 78
  wallets trading over $100k.
- Gains are concentrated: the top 1% of wallets take 49 to 61% of all gross gains on a day, in line with
  Solidus's finding that 0.55% of wallets take half the profit in politics markets.
- Even market makers are not mostly profitable before rewards: 45 to 48% of Pro-MM wallets end a day
  positive, median -0.3% per dollar. Their dollar-weighted PnL is positive (+0.2 to +0.7%) because the
  large ones earn; the rest live on LP rewards, which are not in these figures.
- Retail is the worst by every measure: 41 to 44% profitable, median -9 to -15% per dollar.
