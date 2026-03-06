# Amazon Competitor Analysis Example

Using the `PangolinfoScraper` skill, OpenClaw can generate reports like this:

## Request
> "Compare the price and rating of the top 3 results for 'Gaming Mouse' on Amazon."

## Agent Process
1.  **Search**: `scrape("https://www.amazon.com/s?k=Gaming+Mouse", parser="amazon")`
2.  **Extract**: Identify ASINs `B07W4D1L`, `B08N5WRWNW`, `B07G3ZNK4Y`.
3.  **Analyze**:

| Product | Price | Rating | Reviews |
| :--- | :--- | :--- | :--- |
| Logitech G502 HERO | $39.99 | 4.7 ⭐ | 52,400 |
| Razer DeathAdder V2 | $34.99 | 4.6 ⭐ | 21,300 |
| SteelSeries Rival 3 | $29.99 | 4.5 ⭐ | 15,800 |

## Conclusion
"The **SteelSeries Rival 3** is the budget winner at $29.99, but **Logitech G502** dominates in user satisfaction with 4.7 stars. If you need wireless, consider..."
