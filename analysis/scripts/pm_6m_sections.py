"""Turn a pm_grid.py result JSON into plain-language markdown sections for the public note, the public README and
the research report. Usage: python3 pm_6m_sections.py RESULT.json LABEL   (LABEL e.g. "six months")
Writes /tmp/six_month_note_section.md and /tmp/six_month_readme_bullets.md and prints key numbers."""
import json, sys, datetime as dt
R = json.load(open(sys.argv[1])); label = sys.argv[2] if len(sys.argv) > 2 else 'the period'
P = R['period']; months = R['months']; days = R['days']; v1 = P['v1']; v2 = P['v2']
ORDER1 = ['Pro-MM', 'Fast-taker', 'Hybrid-bot', 'Systematic-taker', 'Mid-MM', 'Systematic-mixed', 'Retail']
ORDER2 = ['Pro-MM', 'Part-time MM', 'Neutral bot', 'Directional bot', 'Session trader', 'Retail']
PLAIN1 = {'Pro-MM': 'Market makers, full time (Pro-MM)', 'Fast-taker': 'Fast bots taking liquidity (Fast-taker)', 'Hybrid-bot': 'Fast bots on both sides (Hybrid-bot)',
          'Systematic-taker': 'Active traders using tools (Systematic-taker)', 'Mid-MM': 'Market makers, part time (Mid-MM)',
          'Systematic-mixed': 'Active traders, mixed (Systematic-mixed)', 'Retail': 'Casual bettors (Retail)'}
PLAIN2 = {'Pro-MM': 'Market makers, full time', 'Part-time MM': 'Market makers, part time', 'Neutral bot': 'Bots trading both sides',
          'Directional bot': 'Bots betting a direction', 'Session trader': 'Active traders using tools', 'Retail': 'Casual bettors'}
def roll(v, cs): rs = [v[c] for c in cs if c in v]; return (sum(r['touched'] for r in rs), sum(r['maker'] for r in rs), sum(r['taker'] for r in rs), sum(r['pnl_usd'] for r in rs), sum(r['wallets'] for r in rs))
def mname(m): return dt.date.fromisoformat(m + '-01').strftime('%B %Y')
fast = sum(v1[c]['touched'] for c in ('Pro-MM', 'Fast-taker', 'Hybrid-bot') if c in v1)
mm, ba, rt = roll(v1, ['Pro-MM', 'Mid-MM']), roll(v1, ['Fast-taker', 'Hybrid-bot', 'Systematic-taker', 'Systematic-mixed']), roll(v1, ['Retail'])
m2, ma, pe = roll(v2, ['Pro-MM', 'Part-time MM']), roll(v2, ['Neutral bot', 'Directional bot']), roll(v2, ['Session trader', 'Retail'])
nd = P['days']; losers = sum(r['pnl_usd'] for r in v1.values() if r['pnl_usd'] < 0); perday = -losers / nd
first, last = sorted(months)[0], sorted(months)[-1]
def mrow(m):
    g = months[m]; gv1, gv2 = g['v1'], g['v2']
    mmm, mba, mrt = roll(gv1, ['Pro-MM', 'Mid-MM']), roll(gv1, ['Fast-taker', 'Hybrid-bot', 'Systematic-taker', 'Systematic-mixed']), roll(gv1, ['Retail'])
    mma, mpe = roll(gv2, ['Neutral bot', 'Directional bot']), roll(gv2, ['Session trader', 'Retail'])
    mach_pnl = 100 * sum(gv2[c]['pnl_usd'] for c in ('Neutral bot', 'Directional bot') if c in gv2) / max(sum(gv2[c]['pnl_usd'] / (gv2[c]['pnl'] / 100) for c in ('Neutral bot', 'Directional bot') if c in gv2 and gv2[c]['pnl']), 1)
    return (f"| {mname(m)} | {g['days']} | {g['touched']/g['days']/2e6:.1f} | {g['wallets']:,} | {mmm[0]:.0f}% | {mba[0]:.0f}% | {mrt[0]:.1f}% | "
            f"{mma[0]:.0f}% | {mpe[0]:.0f}% | {-mpe[3]/g['days']/1e3:,.0f} | {g['profitable_pct']:.0f}% |")
month_table = ("| Month | Days | Volume per day, $M single-counted | Wallets | Market makers | Bots and active traders | Casual bettors | Bots (v2) | People (v2) | $k per day from people to bots and makers | Wallets profitable in the month |\n"
               "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n" + "\n".join(mrow(m) for m in sorted(months)))
rt_by_m = [roll(months[m]['v1'], ['Retail'])[0] for m in sorted(months)]
fast_by_m = [sum(months[m]['v1'][c]['touched'] for c in ('Pro-MM', 'Fast-taker', 'Hybrid-bot') if c in months[m]['v1']) for m in sorted(months)]
pe_by_m = [-roll(months[m]['v2'], ['Session trader', 'Retail'])[3] / months[m]['days'] for m in sorted(months)]
vol_by_m = [months[m]['touched'] / months[m]['days'] / 2e6 for m in sorted(months)]
def trend(vals, unit='%', dec=0):
    a, b = vals[0], vals[-1]; lo, hi = min(vals), max(vals)
    f = (lambda x: f"{x:.{dec}f}{unit}")
    if abs(b - a) < 0.15 * max(abs(a), 1e-9): return f"held between {f(lo)} and {f(hi)}"
    return f"went from {f(a)} in {mname(first)} to {f(b)} in {mname(last)} (range {f(lo)} to {f(hi)})"
t1 = "| Who | Wallets | Share of volume | Share of resting orders | Share of aggressive trades | PnL per $ | PnL $, {n} days | Wallets profitable | Median PnL per $ |\n|---|---:|---:|---:|---:|---:|---:|---:|---:|\n".format(n=nd)
t1 += "\n".join(f"| {PLAIN1[c]} | {v1[c]['wallets']:,} | {v1[c]['touched']:.1f}% | {v1[c]['maker']:.1f}% | {v1[c]['taker']:.1f}% | {v1[c]['pnl']:+.2f}% | {v1[c]['pnl_usd']:+,.0f} | {v1[c]['profitable']:.1f}% | {v1[c]['median']:+.1f}% |" for c in ORDER1 if c in v1)
r1 = ("| Persona | Wallets | Share of volume | Share of resting orders | Share of aggressive trades | PnL $ | Venue-wide share, May 2026 |\n|---|---:|---:|---:|---:|---:|---:|\n"
      f"| Market makers | {mm[4]:,} | {mm[0]:.1f}% | {mm[1]:.1f}% | {mm[2]:.1f}% | {mm[3]:+,.0f} | 38.4% |\n"
      f"| Bots and active traders | {ba[4]:,} | {ba[0]:.1f}% | {ba[1]:.1f}% | {ba[2]:.1f}% | {ba[3]:+,.0f} | 56.3% |\n"
      f"| Casual bettors | {rt[4]:,} | {rt[0]:.1f}% | {rt[1]:.1f}% | {rt[2]:.1f}% | {rt[3]:+,.0f} | 5.3% |")
t2 = "| Who (v2) | Wallets | Share of volume | Share of resting orders | Share of aggressive trades | PnL per $ | PnL $ | Wallets profitable |\n|---|---:|---:|---:|---:|---:|---:|---:|\n"
t2 += "\n".join(f"| {PLAIN2[c]} | {v2[c]['wallets']:,} | {v2[c]['touched']:.1f}% | {v2[c]['maker']:.1f}% | {v2[c]['taker']:.1f}% | {v2[c]['pnl']:+.2f}% | {v2[c]['pnl_usd']:+,.0f} | {v2[c]['profitable']:.1f}% |" for c in ORDER2 if c in v2)
pers = [(k, P[k]) for k in ('persist_d1', 'persist_d2_4', 'persist_d5_9', 'persist_d10_19', 'persist_d20p') if k in P]
PL = {'persist_d1': '1 day', 'persist_d2_4': '2 to 4 days', 'persist_d5_9': '5 to 9 days', 'persist_d10_19': '10 to 19 days', 'persist_d20p': '20 or more days'}
t3 = ("| Active days in the period | Wallets | Share of volume | Wallets profitable | Median PnL per $ |\n|---|---:|---:|---:|---:|\n" +
      "\n".join(f"| {PL[k]} | {r['wallets']:,} | {r['share']:.1f}% | {r['profitable']:.1f}% | {r['median']:+.1f}% |" for k, r in pers)) if pers else ''
sec = f'''## {label[0].upper() + label[1:]}, {days[0]} to {days[-1]}: the grid over the whole period and month by month

Every trade, both legs, for {nd} days: {P['wallets']:,} wallets, ${P['touched']/1e6:,.0f}M traded (both sides counted; ${P['touched']/2e6:,.0f}M
single-counted, ${P['touched']/nd/2e6:.1f}M a day). One cohort per wallet for the whole period, following the segmentation
repo's definitions: cadence is fills per active day across the period and maker share is the wallet's maker volume
over its total. Profit and loss is at settlement, before liquidity rewards; no fees were charged on these markets.

Over the period {P['profitable_pct']:.0f}% of wallets ended ahead, the typical wallet lost {-P['median_pnl']:.1f}% of what it traded, the top 1% of
wallets took {P['top1pct_gain_share']:.0f}% of all gains and the top 0.1% took {P.get('top01pct_gain_share', 0):.0f}%. About ${perday/1e3:,.0f}k a day moved from the
cohorts that lose to the cohorts that win.

### Month by month

{month_table}

Bots and market makers (the three fast cohorts) {trend(fast_by_m)} of volume. Casual bettors {trend(rt_by_m, dec=1)}.
Volume per day {trend(vol_by_m, unit='M', dec=1)}. The daily transfer from people to bots and market makers {trend([x/1e3 for x in pe_by_m], unit='k', dec=0)}.

### The grid over the whole period

{t1}

{r1}

Market makers and fast bots together are {fast:.0f}% of volume. Market makers post {mm[1]:.0f}% of resting orders; bots and
active traders take {ba[2]:.0f}% of aggressive trades. Casual bettors are {rt[0]:.1f}% of volume and {100*rt[4]/P['wallets']:.0f}% of wallets.

### The proposed v2 split over the whole period

{t2}

Rollup: market makers {m2[0]:.1f}% of volume ({m2[3]:+,.0f}), bots {ma[0]:.1f}% ({ma[3]:+,.0f}), people {pe[0]:.1f}% ({pe[3]:+,.0f}).

### Who is still standing after {label}

{t3}

Result file with per-month, per-day and persistence tables: `RESULT_FILE`.
'''
open('/tmp/six_month_note_section.md', 'w').write(sec)
bul = (f"- Over {label} ({mname(first)} to {mname(last)}), the picture did not change: bots and market makers were {fast:.0f}% of volume,\n"
       f"  casual bettors {rt[0]:.1f}%. About ${perday/1e3:,.0f}k a day moved from the people who lose to the bots and market makers who win.\n"
       f"  Only {P['profitable_pct']:.0f}% of the {P['wallets']:,} wallets that traded ended the period ahead; the top 0.1% of wallets took {P.get('top01pct_gain_share', 0):.0f}% of all gains.\n")
open('/tmp/six_month_readme_bullets.md', 'w').write(bul)
print(f"days {nd}, touched ${P['touched']/1e6:.0f}M, wallets {P['wallets']:,}; fast {fast:.1f}%, MMs {mm[0]:.1f}/{mm[1]:.1f}m/{mm[2]:.1f}t, B+A {ba[0]:.1f}/{ba[1]:.1f}/{ba[2]:.1f}, Retail {rt[0]:.1f}; per day ${perday:,.0f}; profitable {P['profitable_pct']:.1f}%, median {P['median_pnl']:+.2f}%, top1 {P['top1pct_gain_share']:.0f}%")
print('months:', {m: round(roll(months[m]['v1'], ['Retail'])[0], 2) for m in sorted(months)})
