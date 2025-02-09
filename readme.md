# eGet-Crawler-for-ai: Enhanced Web Scraping for AI

**This project is a fork of the [eGet](https://github.com/vishwajeetdabholkar/eGet-Crawler-for-ai) project, with modifications and save markdown format's xero api docs in [Xero folder](./xero/)**



## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Chrome/Chromium browser

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/eGet-Crawler-for-ai.git
cd eGet-Crawler-for-ai
```

2. Create and activate virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate on Linux/macOS
source venv/bin/activate

# Activate on Windows
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the API server:
```bash
uvicorn api:app --reload
```

The API will be accessible at `http://localhost:8000`.

### API Usage Examples

Scraping a list of Xero API pages
```terminal
python xero.py
```


## 🔍 Monitoring

The API exposes Prometheus metrics at `/metrics`:

- `scraper_requests_total`: Total scrape requests
- `scraper_errors_total`: Error count
- `scraper_duration_seconds`: Scraping duration

Access Prometheus dashboard at `http://localhost:9090`

## 📄 License

This project is licensed under the Apache License - see the LICENSE file for details.

## 🙏 Acknowledgments

- FastAPI for the amazing web framework
- Selenium team for browser automation
- Beautiful Soup for HTML parsing
- Original eGet project creators
