# Spyfu (Bulk URLs) Scraper
> Spyfu (Bulk URLs) Scraper takes a list of website URLs and turns SpyFu public data into structured, actionable insights. It uncovers the most valuable keywords, top ads, domain statistics, and leading competitors for every domain you track.
> Ideal for SEO agencies, PPC teams, and growth marketers who want fast, scalable competitive intelligence with minimal setup using SpyFu bulk URL analysis.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Spyfu (Bulk URLs)</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction
Spyfu (Bulk URLs) Scraper lets you submit a batch of website URLs, select a target country, choose the insight type you want (e.g., Top Competitors, Most Valuable Keywords, Newly Ranked Keywords, Top Ads, or Domain Stats), and receive clean structured data back.

It solves the problem of manually checking SpyFu for each domain by automating the process and standardizing the output. This makes it perfect for SEO agencies, PPC specialists, growth marketers, market researchers, and data teams who need repeatable SpyFu-based insights at scale.

### Competitive SEO Intelligence at Scale
- Analyze dozens or hundreds of domains in a single run using bulk URLs.
- Pull top competitors, most valuable and newly ranked keywords, and top-performing ads per domain.
- Include domain-level statistics such as estimated traffic, organic vs paid split, and ad visibility.
- Filter by default country to align insights with your target market.
- Designed to be proxy-friendly and operate only on publicly available SpyFu data.

## Features
| Feature | Description |
|----------|-------------|
| Bulk URL input | Submit a list of website URLs in one go to analyze multiple domains efficiently. |
| Top competitors discovery | Retrieve the most relevant competing domains based on SpyFu competitive landscape. |
| Most valuable keywords | Fetch high-value keywords that drive the most estimated traffic or ad spend for each domain. |
| Most successful & newly ranked keywords | Identify top-performing keywords and those that have recently entered the rankings. |
| Top ads extraction | Get examples of the most successful ads running for each domain, including text and landing pages. |
| Domain statistics snapshot | Collect key domain metrics such as estimated traffic, paid vs organic ratio, and keyword counts. |
| Country targeting | Optionally select a default country to localize keyword and ad insights. |
| Origin tracking | Every record includes the original URL used as the starting point for full traceability. |
| Proxy support | Built to work reliably with residential or high-quality proxies to reduce blocking risk. |
| Lightweight & low-cost | Optimized requests and batching minimize data costs while maintaining speed and coverage. |

---

## What Data This Scraper Extracts
| Field Name | Field Description |
|-------------|------------------|
| origin | The original website URL submitted in the input list (the "Start URL"). |
| domain | Normalized domain or root domain extracted from the origin URL. |
| country | Target country for the analysis (e.g., `US`, `UK`, `DE`), if specified. |
| process_type | The type of process run for this record, such as `top_competitors`, `most_valuable_keywords`, `newly_ranked_keywords`, `top_ads`, or `domain_stats`. |
| top_competitors | Array of competitor domain objects with metrics such as overlap, visibility, and estimated traffic share. |
| most_valuable_keywords | Array of keyword objects with fields like `keyword`, `estimated_value`, `search_volume`, and `position`. |
| most_successful_keywords | Array capturing historically strong or best-performing keywords for the domain. |
| newly_ranked_keywords | Array of keyword objects that have recently started ranking for the domain, with rank and trend data. |
| top_ads | Array of ad objects with headline, description, ad type, and landing page URL. |
| domain_stats | Object summarizing the domain’s SpyFu metrics such as `organic_keywords`, `paid_keywords`, `estimated_monthly_clicks`, and `estimated_monthly_budget`. |
| timestamp | Unix timestamp indicating when the data was collected. |
| run_id | Unique identifier for the run, useful for debugging and tracking batches. |
| notes | Optional field for additional metadata, warnings, or comments about the specific domain result. |

---

## Example Output
Example:

    [
      {
        "origin": "https://example.com/",
        "domain": "example.com",
        "country": "US",
        "process_type": "top_competitors",
        "top_competitors": [
          {
            "domain": "competitor1.com",
            "overlap_score": 0.82,
            "estimated_monthly_clicks": 14500,
            "organic_keywords": 2350,
            "paid_keywords": 410
          },
          {
            "domain": "competitor2.com",
            "overlap_score": 0.74,
            "estimated_monthly_clicks": 9800,
            "organic_keywords": 1875,
            "paid_keywords": 260
          }
        ],
        "most_valuable_keywords": [
          {
            "keyword": "best crm software",
            "search_volume": 12100,
            "estimated_value": 5.42,
            "position": 3,
            "traffic_share": 0.12
          }
        ],
        "newly_ranked_keywords": [
          {
            "keyword": "crm for startups",
            "search_volume": 2900,
            "position": 18,
            "trend": "rising"
          }
        ],
        "top_ads": [
          {
            "headline": "All-in-One CRM for SMBs",
            "description": "Close more deals with automated workflows and analytics.",
            "ad_type": "text",
            "landing_page_url": "https://example.com/crm"
          }
        ],
        "domain_stats": {
          "organic_keywords": 3520,
          "paid_keywords": 780,
          "estimated_monthly_clicks": 23800,
          "estimated_monthly_budget": 12450.0
        },
        "timestamp": 1714651200000,
        "run_id": "spyfu-bulk-urls-2024-001",
        "notes": "All metrics derived from publicly available SpyFu data."
      }
    ]

---

## Directory Structure Tree
Assuming a complete working project, a typical structure might look like this:

    Spyfu (Bulk URLs)/
    ├── src/
    │   ├── runner.py
    │   ├── cli.py
    │   ├── services/
    │   │   ├── spyfu_client.py
    │   │   ├── proxy_manager.py
    │   │   └── request_throttler.py
    │   ├── processors/
    │   │   ├── competitors_processor.py
    │   │   ├── keywords_processor.py
    │   │   ├── ads_processor.py
    │   │   └── domain_stats_processor.py
    │   ├── parsers/
    │   │   ├── html_parser.py
    │   │   └── json_normalizer.py
    │   ├── outputs/
    │   │   ├── exporters.py
    │   │   └── schema_validator.py
    │   └── config/
    │       ├── settings.example.json
    │       └── logging.conf
    ├── data/
    │   ├── input_urls.sample.txt
    │   └── sample_output.json
    ├── tests/
    │   ├── test_competitors_processor.py
    │   ├── test_keywords_processor.py
    │   └── test_domain_stats_processor.py
    ├── docs/
    │   ├── usage.md
    │   └── api-reference.md
    ├── requirements.txt
    ├── pyproject.toml
    └── README.md

---

## Use Cases
- **SEO agencies** use it to **audit client and competitor domains in bulk**, so they can **deliver deeper, data-backed strategy recommendations faster**.
- **PPC specialists** use it to **uncover top competitors and winning ads**, so they can **refine campaigns and improve ROAS with proven angles**.
- **Growth marketers** use it to **discover most valuable and newly ranked keywords across multiple brands**, so they can **prioritize content and landing page experiments with the highest upside**.
- **Market research teams** use it to **map competitive landscapes in new markets**, so they can **quickly understand who dominates paid and organic visibility**.
- **Data analysts** use it to **pipe SpyFu-style competitive metrics into dashboards**, so they can **track trends and performance over time without manual checks**.

---

## FAQs

**Q: What input format does this scraper require?**
A: You provide a plain list of website URLs to analyze. Each line should contain a single URL (for example, `https://example.com` or `https://sub.example.com`). The scraper normalizes each URL into a domain and runs the selected SpyFu-based process for every entry.

**Q: Can I choose which type of data to fetch for each run?**
A: Yes. You can select which process to run, such as “Get Top Competitors”, “Get Most Valuable Keywords”, “Get Newly Ranked Keywords”, “Get Top Ads”, or “Get Domain Statistics”. You can focus on a single process per run or orchestrate multiple runs with different process types.

**Q: Do I need to use proxies?**
A: It is strongly recommended to use high-quality, preferably residential proxies. This helps distribute requests, avoid rate limits, and keep runs stable, especially when working with large URL lists or frequent runs.

**Q: Does this scraper access any private data?**
A: No. It only accesses publicly available data as exposed through SpyFu’s public-facing endpoints and pages. The goal is to structure and standardize this information for easier analysis, not to bypass any protections.

---

## Performance Benchmarks and Results

- **Primary Metric – Throughput:** In typical conditions, the scraper can process around 60–120 domains per minute, depending on network quality, proxy performance, and the depth of data requested (e.g., full stats vs only competitors).
- **Reliability Metric – Success Rate:** With a stable proxy pool, success rates of 95%+ per run are achievable, with automatic retries helping recover from transient failures or slow responses.
- **Efficiency Metric – Resource Usage:** Batching requests and reusing HTTP sessions keeps CPU and memory usage modest, making it suitable to run on lightweight servers or containers while still handling sizable URL lists.
- **Quality Metric – Data Completeness:** For most mainstream domains, the scraper returns high-completeness datasets, including competitors, key keywords, and ad examples. Any gaps or missing fields are logged so you can quickly spot where SpyFu exposes limited data for a given domain.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
