import pandas as pd
import re


def load_dataset():
    """
    Loads Fake.csv and True.csv, assigns labels,
    merges them into a single shuffled dataframe.
    """

    # Load datasets
    fake = pd.read_csv("dataset/Fake.csv")
    true = pd.read_csv("dataset/True.csv")

    # Assign labels
    fake["label"] = 0
    true["label"] = 1

    # Combine title + text
    fake["content"] = fake["title"] + " " + fake["text"]
    true["content"] = true["title"] + " " + true["text"]

    # Merge datasets
    df = pd.concat([fake, true], axis=0)

    # Shuffle dataset to remove ordering bias
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    return df[["content", "label"]]


def clean_text(text):
    """
    Cleans news article text to reduce dataset bias
    and improve model learning.
    """

    # lowercase
    text = text.lower()

    # remove reuters mentions
    text = re.sub(r"reuters", "", text)

    # remove location tags like (reuters), (ap), etc
    text = re.sub(r"\(.*?\)", "", text)

    # remove urls
    text = re.sub(r"http\S+|www\S+", "", text)

    # remove numbers
    text = re.sub(r"\d+", "", text)

    # remove punctuation
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text