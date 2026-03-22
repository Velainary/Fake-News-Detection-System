# Fake News Detection System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey.svg)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A machine learning-powered web application that analyzes news articles to determine if they are real or fake. Built with Flask, scikit-learn, and a modern web interface.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [API Reference](#api-reference)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project implements a fake news detection system using natural language processing and machine learning. The system combines multiple classification algorithms to analyze news content and provide predictions with confidence scores. Users can input news articles via URL or direct text, and the system returns a classification along with the most influential keywords.

The application consists of:
- **Backend**: Flask web server with ML model integration
- **Frontend**: Responsive web interface with animations
- **Model**: Ensemble of classifiers trained on labeled news datasets
- **Preprocessing**: Text cleaning and feature extraction pipeline

## Features

- **Dual Input Methods**: Analyze news via URL extraction or direct text input
- **Real-time Classification**: Instant predictions using pre-trained ML models
- **Confidence Scoring**: Percentage confidence for each prediction
- **Keyword Analysis**: Top 10 words influencing the classification
- **Modern UI**: Dark theme with animated background and smooth transitions
- **Responsive Design**: Works on desktop and mobile devices
- **Web Scraping**: Automatic article extraction from URLs using Beautiful Soup

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd fake-news-detection-system
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the model** (optional, pre-trained models included):
   ```bash
   python backend/src/train_model.py
   ```

5. **Run the application**:
   ```bash
   python backend/app.py
   ```

6. **Open in browser**:
   Navigate to `http://localhost:5000`

## Usage

### Web Interface

1. Open the application in your web browser
2. Choose input method:
   - **URL**: Paste a news article URL
   - **Text**: Copy-paste article content directly
3. Click "Analyze News"
4. View results:
   - Prediction (REAL NEWS or FAKE NEWS)
   - Confidence percentage with visual bar
   - Top 10 influential keywords

### Example Input

**URL Input**: `https://example.com/news-article`

**Text Input**:
```
Breaking: Scientists discover new planet capable of supporting life. This revolutionary finding could change everything we know about the universe...
```

### Interpreting Results

- **REAL NEWS**: High confidence indicates authentic journalism
- **FAKE NEWS**: Low confidence or sensational keywords may indicate misinformation
- **Keywords**: Words with highest TF-IDF scores that influenced the prediction

## Architecture

### System Components

```
Fake News Detection System
├── Backend (Flask)
│   ├── app.py - Main application and routes
│   ├── src/
│   │   ├── predict.py - ML prediction logic
│   │   ├── preprocess.py - Data cleaning utilities
│   │   └── train_model.py - Model training pipeline
│   └── model/ - Trained models and vectorizers
├── Frontend
│   ├── templates/index.html - Main page template
│   ├── static/css/style.css - Styling and animations
│   └── static/js/script.js - Client-side interactivity
└── Dataset
    ├── Fake.csv - Fake news articles
    └── True.csv - Real news articles
```

### Data Flow

1. **Input Processing**: User submits URL or text
2. **Text Extraction**: If URL, scrape article content using Beautiful Soup
3. **Preprocessing**: Clean and normalize text
4. **Feature Extraction**: Convert text to TF-IDF vectors
5. **Prediction**: Pass vectors through trained classifier
6. **Analysis**: Extract influential keywords and confidence scores
7. **Response**: Render results in web interface

### Technology Stack

- **Backend**: Flask, joblib, Beautiful Soup
- **Machine Learning**: scikit-learn (TF-IDF, classifiers)
- **Frontend**: HTML5, CSS3, JavaScript (ES6)
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn

## API Reference

### Core Functions

#### `predict_news(text)` - [backend/src/predict.py](backend/src/predict.py)

Predicts whether news text is real or fake.

**Parameters:**
- `text` (str): News article content

**Returns:**
- `dict`: `{"prediction": "REAL NEWS"|"FAKE NEWS", "confidence": float}`

**Example:**
```python
from backend.src.predict import predict_news

result = predict_news("Breaking news: Aliens land on Earth!")
print(result)  # {"prediction": "FAKE NEWS", "confidence": 87.5}
```

#### `extract_article(url)` - [backend/app.py](backend/app.py)

Extracts article text from a URL.

**Parameters:**
- `url` (str): News article URL

**Returns:**
- `str`: Extracted article text

#### `clean_text(text)` - [backend/src/preprocess.py](backend/src/preprocess.py)

Cleans and normalizes text for processing.

**Processing steps:**
- Convert to lowercase
- Remove Reuters/location tags
- Remove URLs and numbers
- Remove punctuation
- Normalize whitespace

**Parameters:**
- `text` (str): Raw text input

**Returns:**
- `str`: Cleaned text

#### `get_top_words(text)` - [backend/app.py](backend/app.py)

Extracts top 10 influential words from text.

**Parameters:**
- `text` (str): News article content

**Returns:**
- `list`: List of top words by TF-IDF score

## Dataset

The system is trained on a dataset of news articles labeled as fake or real.

### Data Sources

- **Fake.csv**: Contains fake news articles
- **True.csv**: Contains real news articles

### Data Schema

Each CSV file contains:
- `title`: Article headline
- `text`: Full article content

### Preprocessing

Articles are combined (`title + " " + text`) and labeled:
- Fake: 0
- Real: 1

Text cleaning removes noise and normalizes content for consistent processing.

### Dataset Statistics

- Total articles: ~44,000 (approx. 22,000 fake + 22,000 real)
- File sizes: ~50MB each
- Source: Public news datasets

## Model Training

### Training Pipeline - [backend/src/train_model.py](backend/src/train_model.py)

1. **Data Loading**: Load and combine fake/real datasets
2. **Preprocessing**: Clean text and create features
3. **Feature Extraction**: TF-IDF vectorization
   - Stop words: English
   - N-grams: 1-2 words
   - Max DF: 70%
   - Min DF: 10
4. **Model Selection**: Train multiple classifiers
5. **Evaluation**: Compare accuracy scores
6. **Serialization**: Save best model and vectorizer

### Supported Models

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

### Model Artifacts

Saved in `backend/model/`:
- `fake_news_model.pkl`: Trained classifier
- `vectorizer.pkl`: Fitted TF-IDF vectorizer

### Performance

The best performing model is selected based on validation accuracy. Typical performance metrics:
- Accuracy: 90-95%
- Precision/Recall: Balanced for both classes

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest

# Format code
black .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Built with ❤️ using Flask and scikit-learn