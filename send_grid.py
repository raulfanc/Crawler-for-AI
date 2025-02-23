import requests
import os
import re
import urllib.parse

def scrape_page(url):
    """Scrapes a single page and returns the markdown content."""
    payload = {
        "url": url,
        "formats": ["markdown"],
        "onlyMainContent": True,
        "includeScreenshot": False,
        "includeRawHtml": False,
        "includeTags": ["article", "section"],
        "excludeTags": ["nav", "footer"],
    }

    try:
        response = requests.post("http://localhost:8000/api/v1/scrape", json=payload)
        response.raise_for_status()
        result = response.json()

        if result["success"]:
            return result["data"]["markdown"]
        else:
            print(f"Failed to scrape {url}")
            print(f"Server response: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def extract_links(markdown_content, base_url):
    """Extracts and filters links from the markdown content."""
    links = re.findall(r'\[.*?\]\((.*?)\)', markdown_content)
    absolute_links = [urllib.parse.urljoin(base_url, link) for link in links]
    # Keep only links within the SendGrid documentation
    sendgrid_links = [link for link in absolute_links if link.startswith(base_url)]
    return list(set(sendgrid_links)) # Remove duplicates


def main():
    """Crawls the SendGrid documentation, starting from the base URL."""
    base_url = "https://www.twilio.com/docs/sendgrid/for-developers/parsing-email/inbound-email"
    urls_to_scrape = [base_url]
    scraped_urls = set()
    output_dir = "send_grid"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    while urls_to_scrape:
        current_url = urls_to_scrape.pop()
        scraped_urls.add(current_url)

        print(f"Scraping: {current_url}")
        markdown_content = scrape_page(current_url)

        if markdown_content:
            filename = current_url.split("/")[-1] + ".md"
            if not filename:
                filename = "index.md"
            filepath = os.path.join(output_dir, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(markdown_content)
            print(f"Saved to {filepath}")

            new_links = extract_links(markdown_content, base_url)
            for link in new_links:
                if link not in scraped_urls and link not in urls_to_scrape:
                    urls_to_scrape.append(link)

if __name__ == "__main__":
    main()