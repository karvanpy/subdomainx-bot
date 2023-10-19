import httpx
from selectolax.parser import HTMLParser

def get_subdomains(url):
    """Get a list of subdomains for the given domain."""
    response = httpx.get("https://rapiddns.io/subdomain/" + url)
    parser = HTMLParser(response.text)
    results = parser.css("table#table > tbody > tr > td:nth-of-type(1)")
    results = [result.text() for result in results if not result.text().startswith("www")]
    results = set(results)
    # results = [
    #     { "url": result } for result in results
    # ]
    return results