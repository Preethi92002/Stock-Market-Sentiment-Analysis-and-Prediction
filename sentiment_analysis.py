import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

# Load the data (messages saved in 'telegram_data.txt')
with open('data/telegram_data.txt', 'r', encoding='utf-8') as file:
    messages = file.readlines()

# Initialize SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(text):
    sentiment_score = sia.polarity_scores(text)
    return sentiment_score['compound']  # Compound score is a good indicator of overall sentiment

# Create a DataFrame to store messages and sentiment scores
data = pd.DataFrame({
    'Message': messages,
    'Sentiment Score': [analyze_sentiment(msg) for msg in messages]
})

# Save the DataFrame to a new CSV file
data.to_csv('data/sentiment_analysis.csv', index=False)

# Show the first few rows of the DataFrame
print(data.head())
