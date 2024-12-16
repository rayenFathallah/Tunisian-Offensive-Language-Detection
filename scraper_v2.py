from apify_client import ApifyClient
import os
from dotenv import load_dotenv


def extract_comments_v2(post_url) : 
    load_dotenv()
    api_key = os.getenv("apify_api_key")
    client = ApifyClient(api_key)

    run_input = {
        "startUrls": [{ "url": post_url }],
        "resultsLimit": 50,
    }

    run = client.actor("apify/facebook-comments-scraper").call(run_input=run_input)

    items = client.dataset(run["defaultDatasetId"]).iterate_items() 
    comments = [item["text"] for item in items if item.get("text","")]
    return comments
