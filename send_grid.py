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

def main():
    """Scrapes a list of URLs and saves them to separate markdown files."""
    urls = [
        "https://www.twilio.com/docs/sendgrid/for-developers",
        "https://www.twilio.com/docs/sendgrid/for-developers/sending-email/quickstart-python",
        "https://www.twilio.com/docs/sendgrid/for-developers/partners/microsoft-azure-2021",
        "https://www.twilio.com/docs/sendgrid/for-developers/tracking-events/getting-started-event-webhook",
        "https://www.twilio.com/docs/sendgrid/for-developers/tracking-events/event",
        "https://www.twilio.com/docs/sendgrid/api-reference/sendgrid-engagement-quality-api",
        "https://www.twilio.com/docs/sendgrid/for-developers/parsing-email/setting-up-the-inbound-parse-webhook",
        "https://www.twilio.com/docs/sendgrid/api-reference/settings-inbound-parse",
    ]

    output_dir = "send_grid"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for url in urls:
        print(f"Scraping: {url}")
        markdown_content = scrape_page(url)

        if markdown_content:
            filename = url.split("/")[-1] + ".md"
            if not filename:
                filename = "index.md"
            filepath = os.path.join(output_dir, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(markdown_content)
            print(f"Saved to {filepath}")

if __name__ == "__main__":
    main()
