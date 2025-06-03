# news_fetcher.py
import feedparser

def fetch_rss_news(feed_url, limit=10):
    feed = feedparser.parse(feed_url)
    return [{"title": entry.title, "link": entry.link} for entry in feed.entries[:limit]]

def fetch_latest_news():
    return {
        "Dawn News": fetch_rss_news("https://www.dawn.com/feeds/latest-news"),
        "The News": fetch_rss_news("https://thenews.com.pk/rss/1/1"),
        "Al Jazeera": fetch_rss_news("https://www.aljazeera.com/xml/rss/all.xml"),
        "BBC News": fetch_rss_news("https://feeds.bbci.co.uk/news/world/rss.xml")
    }
