from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

from src.predict import predict_news
from src.predict import vectorizer

app = Flask(__name__)


def extract_article(url):
    """
    Fetch article text from a news URL
    """

    try:
        headers = {"User-Agent": "Mozilla/5.0"}

        r = requests.get(url, headers=headers, timeout=10)

        soup = BeautifulSoup(r.text, "html.parser")

        paragraphs = soup.find_all("p")

        text = " ".join([p.get_text() for p in paragraphs])

        return text

    except Exception as e:
        print("Extraction error:", e)
        return None


def get_top_words(text):
    """
    Returns important words influencing prediction
    """

    vector = vectorizer.transform([text])

    feature_names = vectorizer.get_feature_names_out()

    dense = vector.todense().tolist()[0]

    word_scores = list(zip(feature_names, dense))

    word_scores = sorted(word_scores, key=lambda x: x[1], reverse=True)

    top_words = [w[0] for w in word_scores[:10]]

    return top_words


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    confidence = None
    keywords = None
    article_text = None

    if request.method == "POST":

        text = request.form.get("news_text")
        url = request.form.get("news_url")

        if url:
            article_text = extract_article(url)
        else:
            article_text = text

        if article_text:

            prediction, confidence = predict_news(article_text)

            keywords = get_top_words(article_text)

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        keywords=keywords
    )


if __name__ == "__main__":
    app.run(debug=True)