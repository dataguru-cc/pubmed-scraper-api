# PubMed Scraper API

Scrape PubMed with a JSON API. This repo has working Python examples for DataGuru's PubMed scraper APIs: PubMed Article Details and PubMed Article Search.

[DataGuru](https://dataguru.cc) runs the scraping, proxies, retries and parsing, and returns clean JSON. You pay only for successful requests, from $0.0012 per request, out of a prepaid balance: no subscription. New accounts get $1.00 of free credit.

## PubMed APIs

| API | What it returns | Price | Page |
| --- | --- | --- | --- |
| [PubMed Article Details](#pubmed-article-details) | Get a PubMed article's full record, including abstract sections, authors with affiliations and ORCID iDs, journal details, MeSH terms, keywords, chemicals, grants, references, citing articles, DOI and free full-text links. | $0.0022 | [https://dataguru.cc/apis/pubmed-article-details/](https://dataguru.cc/apis/pubmed-article-details/) |
| [PubMed Article Search](#pubmed-article-search) | Search PubMed by keyword and get matching biomedical articles with titles, authors, journal, publication date, abstract, keywords, publication types, DOI and free full-text links. | $0.0012 | [https://dataguru.cc/apis/pubmed-article-search/](https://dataguru.cc/apis/pubmed-article-search/) |

## Quick start

1. Create a free account and an API key at [dashboard.dataguru.cc](https://dashboard.dataguru.cc).
2. Install and run:

```bash
git clone https://github.com/dataguru-cc/pubmed-scraper-api.git
cd pubmed-scraper-api
pip install -r requirements.txt
export DATAGURU_API_KEY="your key"
python examples/sdk_example.py pubmed-article-details
```

## Examples

Every example covers all 2 PubMed APIs. Pass an API name to run just one; with no name each script runs them all, and each call is billed at the price above.

| File | Style | Run |
| --- | --- | --- |
| [`examples/sdk_example.py`](examples/sdk_example.py) | [DataGuru Python SDK](https://github.com/dataguru-cc/dataguru-python) (`pip install dataguru-sdk`), one function per API, saves JSON to `output/` | `python examples/sdk_example.py` |
| [`examples/requests_example.py`](examples/requests_example.py) | Plain `requests`, synchronous | `python examples/requests_example.py` |
| [`examples/async_example.py`](examples/async_example.py) | `asyncio` + `httpx`, concurrent with a limit | `python examples/async_example.py` |
| [`examples/scrapy_spider.py`](examples/scrapy_spider.py) | Scrapy spider, items to JSON/CSV | `scrapy runspider examples/scrapy_spider.py -O pubmed.json` |

All requests use the header `Authorization: Api-Key YOUR_API_KEY`. Errors return `{"success": false, "error": {"code", "message", "request_id"}}`, with HTTP 402 when the balance runs out and 429 (with `Retry-After`) when rate limited. Failed requests are not charged.

## API reference

### PubMed Article Details

Get a PubMed article's full record, including abstract sections, authors with affiliations and ORCID iDs, journal details, MeSH terms, keywords, chemicals, grants, references, citing articles, DOI and free full-text links.

- Endpoint: `POST https://api.dataguru.cc/api/v1/pubmed/articles/details`
- Price: $0.0022 per successful request ($2.20 per 1,000)
- Rate limit: 60 requests/minute
- Page and live playground: https://dataguru.cc/apis/pubmed-article-details/
- Documentation: https://dataguru.cc/documentation/pubmed-article-details/

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `article_url` | string | yes | PubMed article URL (e.g. https://pubmed.ncbi.nlm.nih.gov/31452104/) or the numeric PMID. |

**Response fields:** `pmid`, `title`, `abstract`, `abstract_sections`, `copyright`, `authors`, `journal`, `volume`, `issue`, `pages`, `pub_date`, `pub_date_iso`, `year`, `electronic_pub_date`, `doi`, `pmcid`, `pii`, `publication_types`, `language`, `keywords`, `mesh_terms`, `chemicals`, `grants`, `publication_status`, `history`, `references`, `references_count`, `cited_by_count`, `cited_by`, `url`, `doi_url`, `pmc_url`, `error`, plus `_metadata`

```bash
curl -X POST "https://api.dataguru.cc/api/v1/pubmed/articles/details" \
  -H "Authorization: Api-Key $DATAGURU_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"article_url": "https://pubmed.ncbi.nlm.nih.gov/31452104/"}'
```

<details><summary>Response schema</summary>

Values are type placeholders from the API's published schema, not real data.

```json
{
  "pmid": "1234567890",
  "title": "string",
  "abstract": "string",
  "abstract_sections": [
    {
      "label": "string",
      "text": "string"
    }
  ],
  "copyright": "string",
  "authors": [
    {
      "name": "string",
      "last_name": "string",
      "fore_name": "string",
      "initials": "string",
      "suffix": "string",
      "is_collective": false,
      "affiliations": [
        "string"
      ],
      "orcid": "1234567890"
    }
  ],
  "journal": {
    "title": "string",
    "iso_abbreviation": "string",
    "medline_abbreviation": "string",
    "issn_print": "string",
    "issn_electronic": "string",
    "country": "string",
    "nlm_id": "1234567890"
  },
  "volume": "string",
  "issue": "string",
  "pages": "string",
  "pub_date": "2026-01-01T12:00:00Z",
  "pub_date_iso": "string",
  "year": 0,
  "electronic_pub_date": "2026-01-01T12:00:00Z",
  "doi": "string",
  "pmcid": "1234567890",
  "pii": "string",
  "publication_types": [
    "string"
  ],
  "language": [
    "string"
  ],
  "keywords": [
    "string"
  ],
  "mesh_terms": [
    {
      "descriptor": "string",
      "ui": "string",
      "major_topic": false,
      "qualifiers": [
        "string"
      ]
    }
  ],
  "chemicals": [
    "string"
  ],
  "grants": [
    {
      "grant_id": "1234567890",
      "agency": "string",
      "country": "string"
    }
  ],
  "publication_status": "string",
  "history": {},
  "references": [
    {
      "citation": "string",
      "pmid": "1234567890",
      "doi": "string",
      "pmcid": "1234567890"
    }
  ],
  "references_count": 0,
  "cited_by_count": 0,
  "cited_by": [
    "string"
  ],
  "url": "https://example.com/...",
  "doi_url": "https://example.com/...",
  "pmc_url": "https://example.com/...",
  "error": "string",
  "_metadata": {
    "request_id": "3f6c1a2e-8b4d-4c1e-9a7f-2d5e6b7c8d9e",
    "execution_time_ms": 842,
    "endpoint": "PubMed Article Details",
    "mode": "live",
    "format": "json",
    "timestamp": "2026-01-01T12:00:00+00:00"
  }
}
```

</details>

### PubMed Article Search

Search PubMed by keyword and get matching biomedical articles with titles, authors, journal, publication date, abstract, keywords, publication types, DOI and free full-text links.

- Endpoint: `POST https://api.dataguru.cc/api/v1/pubmed/articles/search`
- Price: $0.0012 per successful request ($1.20 per 1,000)
- Rate limit: 60 requests/minute
- Page and live playground: https://dataguru.cc/apis/pubmed-article-search/
- Documentation: https://dataguru.cc/documentation/pubmed-article-search/

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | no | Maximum number of results to return (1-100). Default: `20`. |
| `page` | integer | no | Results page (each page holds up to `limit` results). Default: `1`. |
| `query` | string | yes | Search keywords or a PubMed query, e.g. "crispr gene therapy" or "covid-19[ti] AND vaccine". |
| `sort` | string | no | Result order - relevance (best match first) or date (newest first). Default: `relevance`. Allowed: `relevance`, `date`. |
| `year_from` | integer | no | Only return articles published in or after this year, e.g. 2020. |
| `year_to` | integer | no | Only return articles published in or before this year, e.g. 2024. |

**Response fields:** `query`, `query_translation`, `sort`, `page`, `total_results`, `returned_results`, `results`, `error`, plus `_metadata`

```bash
curl -X POST "https://api.dataguru.cc/api/v1/pubmed/articles/search" \
  -H "Authorization: Api-Key $DATAGURU_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "crispr gene therapy"}'
```

<details><summary>Response schema</summary>

Values are type placeholders from the API's published schema, not real data.

```json
{
  "query": "string",
  "query_translation": "string",
  "sort": "relevance",
  "page": 0,
  "total_results": 0,
  "returned_results": 0,
  "results": [
    {
      "pmid": "1234567890",
      "title": "string",
      "abstract": "string",
      "authors": [
        "string"
      ],
      "journal": "string",
      "journal_abbreviation": "string",
      "volume": "string",
      "issue": "string",
      "pages": "string",
      "pub_date": "2026-01-01T12:00:00Z",
      "pub_date_iso": "string",
      "year": 0,
      "doi": "string",
      "pmcid": "1234567890",
      "publication_types": [
        "string"
      ],
      "language": [
        "string"
      ],
      "keywords": [
        "string"
      ],
      "url": "https://example.com/...",
      "doi_url": "https://example.com/...",
      "pmc_url": "https://example.com/..."
    }
  ],
  "error": "string",
  "_metadata": {
    "request_id": "3f6c1a2e-8b4d-4c1e-9a7f-2d5e6b7c8d9e",
    "execution_time_ms": 842,
    "endpoint": "PubMed Article Search",
    "mode": "live",
    "format": "json",
    "timestamp": "2026-01-01T12:00:00+00:00"
  }
}
```

</details>

## More

- Python SDK and examples for all DataGuru APIs: [github.com/dataguru-cc/dataguru-python](https://github.com/dataguru-cc/dataguru-python) ([docs](https://dataguru-python.readthedocs.io/))
- Every API, with a live playground: [https://dataguru.cc/apis/](https://dataguru.cc/apis/)
- Use DataGuru from Claude, ChatGPT or Cursor through the MCP server: [https://dataguru.cc/mcp/](https://dataguru.cc/mcp/)
- Run thousands of inputs from a CSV at half price with batch jobs: [https://dataguru.cc/documentation/](https://dataguru.cc/documentation/)
- Other scraper APIs: [1688](https://github.com/dataguru-cc/1688-scraper-api), [Airbnb](https://github.com/dataguru-cc/airbnb-scraper-api), [Alibaba](https://github.com/dataguru-cc/alibaba-scraper-api), [AliExpress](https://github.com/dataguru-cc/aliexpress-scraper-api), [Amazon](https://github.com/dataguru-cc/amazon-scraper-api), [arXiv](https://github.com/dataguru-cc/arxiv-scraper-api), [ASOS](https://github.com/dataguru-cc/asos-scraper-api), [Best Buy](https://github.com/dataguru-cc/best-buy-scraper-api), [Booking.com](https://github.com/dataguru-cc/booking-scraper-api), [Brave Search](https://github.com/dataguru-cc/brave-search-scraper-api), [CA State Bar](https://github.com/dataguru-cc/california-state-bar-scraper-api), [Capterra](https://github.com/dataguru-cc/capterra-scraper-api), [CoinGecko](https://github.com/dataguru-cc/coingecko-scraper-api), [CoinMarketCap](https://github.com/dataguru-cc/coinmarketcap-scraper-api), [Companies House](https://github.com/dataguru-cc/companies-house-scraper-api), [Costco](https://github.com/dataguru-cc/costco-scraper-api), [CourtListener](https://github.com/dataguru-cc/courtlistener-scraper-api), [Crunchbase](https://github.com/dataguru-cc/crunchbase-scraper-api), [Discord](https://github.com/dataguru-cc/discord-scraper-api), [DoorDash](https://github.com/dataguru-cc/doordash-scraper-api), [eBay](https://github.com/dataguru-cc/ebay-scraper-api), [Etsy](https://github.com/dataguru-cc/etsy-scraper-api), [Expedia](https://github.com/dataguru-cc/expedia-scraper-api), [Fiverr](https://github.com/dataguru-cc/fiverr-scraper-api), [Flipkart](https://github.com/dataguru-cc/flipkart-scraper-api), [Glassdoor](https://github.com/dataguru-cc/glassdoor-scraper-api), [Google Flights](https://github.com/dataguru-cc/google-flights-scraper-api), [Google Patents](https://github.com/dataguru-cc/google-patents-scraper-api), [Google Scholar](https://github.com/dataguru-cc/google-scholar-scraper-api), [Google Search](https://github.com/dataguru-cc/google-search-scraper-api), [Grubhub](https://github.com/dataguru-cc/grubhub-scraper-api), [Home Depot](https://github.com/dataguru-cc/home-depot-scraper-api), [Instagram](https://github.com/dataguru-cc/instagram-scraper-api), [Investing.com](https://github.com/dataguru-cc/investing-com-scraper-api), [Justia](https://github.com/dataguru-cc/justia-scraper-api), [Kayak](https://github.com/dataguru-cc/kayak-scraper-api), [Kick](https://github.com/dataguru-cc/kick-scraper-api), [Lazada](https://github.com/dataguru-cc/lazada-scraper-api), [MarketWatch](https://github.com/dataguru-cc/marketwatch-scraper-api), [Mercado Libre](https://github.com/dataguru-cc/mercado-libre-scraper-api), [Monster](https://github.com/dataguru-cc/monster-scraper-api), [OpenCorporates](https://github.com/dataguru-cc/opencorporates-scraper-api), [OpenTable](https://github.com/dataguru-cc/opentable-scraper-api), [PACER](https://github.com/dataguru-cc/pacer-scraper-api), [PitchBook](https://github.com/dataguru-cc/pitchbook-scraper-api), [Reddit](https://github.com/dataguru-cc/reddit-scraper-api), [Redfin](https://github.com/dataguru-cc/redfin-scraper-api), [Resy](https://github.com/dataguru-cc/resy-scraper-api), [Rightmove](https://github.com/dataguru-cc/rightmove-scraper-api), [SEC EDGAR](https://github.com/dataguru-cc/sec-edgar-scraper-api), [Seeking Alpha](https://github.com/dataguru-cc/seeking-alpha-scraper-api), [Shopee](https://github.com/dataguru-cc/shopee-scraper-api), [Skyscanner](https://github.com/dataguru-cc/skyscanner-scraper-api), [Target](https://github.com/dataguru-cc/target-scraper-api), [TikTok](https://github.com/dataguru-cc/tiktok-scraper-api), [TradingView](https://github.com/dataguru-cc/tradingview-scraper-api), [TripAdvisor](https://github.com/dataguru-cc/tripadvisor-scraper-api), [Trulia](https://github.com/dataguru-cc/trulia-scraper-api), [TrustRadius](https://github.com/dataguru-cc/trustradius-scraper-api), [Twitch](https://github.com/dataguru-cc/twitch-scraper-api), [Uber Eats](https://github.com/dataguru-cc/uber-eats-scraper-api), [Upwork](https://github.com/dataguru-cc/upwork-scraper-api), [Vrbo](https://github.com/dataguru-cc/vrbo-scraper-api), [Walmart](https://github.com/dataguru-cc/walmart-scraper-api), [Wayfair](https://github.com/dataguru-cc/wayfair-scraper-api), [X (Twitter)](https://github.com/dataguru-cc/twitter-scraper-api), [Yahoo Finance](https://github.com/dataguru-cc/yahoo-finance-scraper-api), [YouTube](https://github.com/dataguru-cc/youtube-scraper-api), [Zillow](https://github.com/dataguru-cc/zillow-scraper-api), [ZoomInfo](https://github.com/dataguru-cc/zoominfo-scraper-api), [Zoopla](https://github.com/dataguru-cc/zoopla-scraper-api)

## License

The example code is MIT licensed. Use of the DataGuru API is subject to the [terms of service](https://dataguru.cc/terms/).
