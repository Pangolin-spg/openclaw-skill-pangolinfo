import argparse
import os
import json
import sys
import requests
from typing import Optional

# Configuration
API_ENDPOINT = "https://scrapeapi.pangolinfo.com/api/v1/scrape"  # Update if different
API_KEY_ENV = "PANGOLINFO_API_KEY"

def get_api_key() -> str:
    """Retrieve API key from environment."""
    key = os.getenv(API_KEY_ENV)
    if not key:
        print(f"Error: {API_KEY_ENV} not found in environment variables.", file=sys.stderr)
        print(f"Please sign up at https://tool.pangolinfo.com/ to get your key.", file=sys.stderr)
        sys.exit(1)
    return key

def scrape(url: str, parser: str = None, country: str = "us") -> dict:
    """
    Execute scrape request to Pangolinfo AI Mode API.
    """
    api_key = get_api_key()
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    payload = {
        "url": url,
        "country": country
    }
    
    # Parser is optional; API often auto-detects
    if parser:
        payload["parserName"] = parser
        
    try:
        response = requests.post(API_ENDPOINT, json=payload, headers=headers, timeout=60)
        response.raise_for_status()
        
        data = response.json()
        
        # Check for API-level errors (structure depends on specific API response format)
        if data.get("code", 0) != 0 and data.get("success") is False:
             print(f"API Error: {data.get('message', 'Unknown error')}", file=sys.stderr)
             sys.exit(1)
             
        return data.get("data", data)
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Scrape data using Pangolinfo API")
    parser.add_argument("--url", required=True, help="Target URL (Amazon, Google, Walmart, etc.)")
    parser.add_argument("--parser", help="Specific parser (e.g., google, amazon)")
    parser.add_argument("--country", default="us", help="Geo-location country code (default: us)")
    parser.add_argument("--output", help="Save result to JSON file")
    
    args = parser.parse_args()
    
    print(f"Scraping {args.url}...", file=sys.stderr)
    result = scrape(args.url, args.parser, args.country)
    
    # Output handling
    json_output = json.dumps(result, indent=2, ensure_ascii=False)
    
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(json_output)
        print(f"Saved to {args.output}", file=sys.stderr)
    else:
        # Print to stdout for OpenClaw to read
        print(json_output)

if __name__ == "__main__":
    main()
