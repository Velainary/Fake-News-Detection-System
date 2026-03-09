import joblib

model = joblib.load("model/fake_news_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

while True:

    title = input("Enter headline: ")
    text = input("Enter article text: ")

    content = title + " " + text

    if text.lower() == "quit":
        break

    vector = vectorizer.transform([content])

    prediction = model.predict(vector)

    if prediction[0] == 1:
        print("Prediction: REAL NEWS")
    else:
        print("Prediction: FAKE NEWS")