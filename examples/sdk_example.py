"""PubMed scraper API: DataGuru Python SDK example.

Runs DataGuru's PubMed APIs and prints the JSON they return:
  - PubMed Article Details: $0.0022 per successful request ($2.20 per 1,000)
  - PubMed Article Search: $0.0012 per successful request ($1.20 per 1,000)

Setup:
    pip install -r requirements.txt
    export DATAGURU_API_KEY="your key"   # free credit at https://dashboard.dataguru.cc

Run:
    python examples/sdk_example.py            # every API below
    python examples/sdk_example.py pubmed-article-details
"""
import json
import sys
from pathlib import Path

from dataguru import DataGuru, DataGuruError

def pubmed_article_details(dg):
    """PubMed Article Details: Get a PubMed article's full record, including abstract sections, authors with affiliations and ORCID iDs, journal details, MeSH terms, keywords, chemicals, grants, references, citing articles, DOI and free full-text links."""
    return dg.call(
        "pubmed-article-details",
        article_url="https://pubmed.ncbi.nlm.nih.gov/31452104/",
    )


def pubmed_article_search(dg):
    """PubMed Article Search: Search PubMed by keyword and get matching biomedical articles with titles, authors, journal, publication date, abstract, keywords, publication types, DOI and free full-text links."""
    return dg.call(
        "pubmed-article-search",
        query="crispr gene therapy",
    )


EXAMPLES = {
    "pubmed-article-details": pubmed_article_details,
    "pubmed-article-search": pubmed_article_search,
}
DEFAULT = ['pubmed-article-details', 'pubmed-article-search']


def main(names):
    out = Path("output")
    out.mkdir(exist_ok=True)
    with DataGuru() as dg:  # reads DATAGURU_API_KEY
        for name in names:
            data = EXAMPLES[name](dg)
            (out / f"{name}.json").write_text(json.dumps(data, indent=2, ensure_ascii=False))
            print(f"{name}: saved output/{name}.json")
            print(json.dumps(data, indent=2, ensure_ascii=False)[:1500])


if __name__ == "__main__":
    names = sys.argv[1:] or DEFAULT
    unknown = [n for n in names if n not in EXAMPLES]
    if unknown:
        sys.exit(f"Unknown API {unknown}. Choose from: {', '.join(EXAMPLES)}")
    try:
        main(names)
    except DataGuruError as error:
        sys.exit(f"DataGuru error: {error}")
