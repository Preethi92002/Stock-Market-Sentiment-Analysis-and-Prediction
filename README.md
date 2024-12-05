# Stock-Market-Sentiment-Analysis-and-Prediction

## **Project Description**
This project involves scraping stock market-related data from Telegram channels, performing sentiment analysis using machine learning models, and visualizing the sentiment distribution. It helps in analyzing the sentiment trends in stock market discussions.

---

## **Features**
- Scrape messages from public Telegram channels using the Telethon API.
- Perform sentiment analysis using a trained Random Forest classifier.
- Predict whether sentiments are positive or negative based on stock market-related texts.
- Save predictions in a CSV file for further analysis.
- Visualize sentiment distribution using matplotlib and seaborn.

---

## **Setup Instructions**

### **Requirements**
1. Clone the repository:
   ```bash
   git clone <repository-url>
2.Navigate to the project folder:

cd Stock-Market-Sentiment-Analysis
3.Install the dependencies:

pip install -r requirements.txt

# Ensure you have the following files:

telegram_scraper.py: For scraping Telegram data.
sentiment_analysis.py: For performing sentiment analysis.
model.py: For training and saving the machine learning model.
predict.py: For loading the model and predicting sentiment.
data folder with necessary .pkl files and text data.

# Run the scripts step-by-step:

Scrape data: telegram_scraper.py
Perform sentiment analysis: sentiment_analysis.py
Train and save the model: model.py
Predict and visualize: predict.py
Technologies Used
Python
Telethon for Telegram data scraping
NLTK for sentiment analysis
Joblib for saving/loading models
Matplotlib and Seaborn for data visualization

# Contact
Developed by Konakondla Preethi
For queries, reach out at [preethi.konakondla@gmail.com]













