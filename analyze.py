
from textblob import TextBlob

def analyze_data(data):
    sentiments = []
    topics = []

    for item in data:
        text = item["title"]
        blob = TextBlob(text)
        sentiments.append(blob.sentiment.polarity)
        topics.extend([word.lower() for word in text.split() if len(word) > 4])

    avg_sentiment = sum(sentiments) / len(sentiments)
    summary = "Positive" if avg_sentiment > 0.1 else "Neutral" if avg_sentiment > -0.1 else "Negative"

    top_topics = list(set(topics))[:5]

    return {
        "summary": summary,
        "top_topics": top_topics,
        "raw": data
    }
