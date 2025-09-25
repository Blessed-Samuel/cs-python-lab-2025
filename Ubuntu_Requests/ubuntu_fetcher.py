import os
from urllib.parse import urlparse

import requests


def fetch_image(url, saved_files):
    try:
        # Fetch image with timeout
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Check content type header
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped {url} (not an image, got {content_type})")
            return

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"

        # Prevent duplicates
        if filename in saved_files:
            print(f"✗ Skipped {filename} (duplicate)")
            return

        # Save file
        filepath = os.path.join("Fetched_Images", filename)
        with open(filepath, "wb") as f:
            f.write(response.content)

        saved_files.add(filename)
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error fetching {url}: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls = input("Please enter image URLs (separated by spaces): ").split()

    os.makedirs("Fetched_Images", exist_ok=True)
    saved_files = set()

    for url in urls:
        fetch_image(url, saved_files)

    print("\nConnection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
