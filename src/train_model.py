import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

from sklearn.metrics import accuracy_score

from preprocess import load_dataset, clean_text


print("Loading dataset...")

df = load_dataset()

df["content"] = df["content"].apply(clean_text)

X = df["content"]
y = df["label"]

print("Vectorizing text...")

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_df=0.7,
    min_df=10,
    ngram_range=(1,2)
)

X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

models = {

    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "Gradient Boosting": GradientBoostingClassifier()
}

best_model = None
best_score = 0

for name, model in models.items():

    print("\nTraining:", name)

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    score = accuracy_score(y_test, pred)

    print("Accuracy:", score)

    if score > best_score:
        best_score = score
        best_model = model


print("\nBest Model Accuracy:", best_score)

joblib.dump(best_model, "model/fake_news_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Model saved.")