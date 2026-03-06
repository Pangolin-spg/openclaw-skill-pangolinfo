
# Pangolinfo Scraper Skill for OpenClaw

<div align="center">

![Pangolinfo Scraper Banner](assets/banner.png)

**Give your AI Agent real-time vision.**
Scrape Amazon, Walmart, and Google Search results as clean JSON.
No CAPTCHAs. No IP bans. Just data.

[Website](https://www.pangolinfo.com) • [Documentation](https://docs.pangolinfo.com) • [Get API Key](https://tool.pangolinfo.com/)

</div>

---

## 🚀 Features

*   **⚡ Real-Time Data**: Fetch live pricing, stock status, and rankings in milliseconds.
*   **🧠 LLM-Ready**: Returns structured JSON that OpenClaw, ChatGPT, and Claude can understand instantly.
*   **🛡️ Unblockable**: Built-in residential proxy rotation and browser fingerprinting.
*   **🔌 Plug & Play**: Designed specifically as an **OpenClaw Skill**.

## 📦 Installation

This skill is designed for [OpenClaw](https://github.com/openclaw/openclaw).

1.  Clone this repository into your skills directory:
    ```bash
    git clone https://github.com/Pangolin-spg/openclaw-skill-pangolinfo.git skills/pangolinfo
    ```

2.  Install dependencies:
    ```bash
    pip install -r skills/pangolinfo/requirements.txt
    ```

3.  Configure your API Key in `.env` or via OpenClaw config:
    ```bash
    export PANGOLINFO_API_KEY="your_api_key_here"
    ```

## 🛠️ Usage

### Within OpenClaw

Just ask your agent!

> "Check the current price of Sony WH-1000XM5 on Amazon US."

> "What are the top 5 organic results for 'AI Agent' on Google?"

### Manual CLI Usage

You can also run the scraper script directly:

```bash
# Scrape an Amazon product
python scripts/scrape.py --url "https://www.amazon.com/dp/B09G9FPHY6"

# Scrape Google Search results
python scripts/scrape.py --url "https://www.google.com/search?q=best+laptops+2025" --parser google
```

## 🧩 Supported Platforms

| Platform | Features | Parser ID |
| :--- | :--- | :--- |
| **Google** | SERP, Titles, Descriptions, Rankings | `google` |
| **Amazon** | Products, Search, Reviews, BSR, BuyBox | `amazon` |
| **Walmart** | Products, Inventory, Sellers | `walmart` |

## 📄 Example Response

OpenClaw will receive clean JSON like this:

```json
{
  "title": "Sony WH-1000XM5 Wireless Noise Canceling Headphones",
  "price": {
    "current": 348.00,
    "currency": "USD"
  },
  "rating": 4.6,
  "reviews_count": 12450,
  "availability": "In Stock",
  "buybox_winner": "Amazon.com"
}
```

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

[MIT](LICENSE) © [Pangolinfo](https://www.pangolinfo.com)
