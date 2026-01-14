#!/usr/bin/env python3

import re
import sys
from urllib.parse import urlparse

SAFE_DOMAINS = [
    "google.com","youtube.com","facebook.com","instagram.com","paypal.com",
    "amazon.com","microsoft.com","apple.com","github.com","linkedin.com",
    "twitter.com","x.com","whatsapp.com","telegram.org","netflix.com",
    "spotify.com","discord.com","reddit.com","amazon.in","sbi.co.in",
    "hdfcbank.com","icicibank.com","axisbank.com"
]

def banner():
    print("""
🦅  EAGLE-EYE PHISHING DETECTOR
--------------------------------
Created by SANJAY.KS
""")

def extract_domain(url):
    try:
        if not url.startswith("http"):
            url = "http://" + url
        parsed = urlparse(url)
        return parsed.hostname.lower()
    except:
        return ""

def check_phishing(url):
    domain = extract_domain(url)

    if not domain:
        return "Invalid URL ❌"

    for safe in SAFE_DOMAINS:
        if safe in domain and not domain.endswith(safe):
            return "⚠️  PHISHING (Fake subdomain detected)"

    if domain in SAFE_DOMAINS:
        return "✅ SAFE WEBSITE"

    return "⚠️  SUSPICIOUS / POSSIBLE PHISHING"

def main():
    banner()
    url = input("Enter URL to scan: ").strip()
    result = check_phishing(url)
    print("\nResult:", result)

if __name__ == "__main__":
    main()
