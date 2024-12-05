import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the predictions from the CSV file
predictions_df = pd.read_csv('data/predictions.csv')

# Count the sentiment distribution
sentiment_counts = predictions_df['Sentiment'].value_counts()

# Plotting the sentiment distribution
plt.figure(figsize=(8, 6))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="Blues_d")
plt.title('Sentiment Distribution of Stock Market News')
plt.xlabel('Sentiment')
plt.ylabel('Number of Messages')
plt.show()
