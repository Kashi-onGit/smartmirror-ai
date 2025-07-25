import feedparser

def get_top_news():
    feed_url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(feed_url)

    headlines = []
    for entry in feed.entries[:4]:
        headlines.append("• " + entry.title)

    return headlines
