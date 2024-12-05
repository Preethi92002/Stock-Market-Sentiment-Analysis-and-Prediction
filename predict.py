import joblib
import csv

# Load the model and vectorizer
try:
    model = joblib.load('data/stock_prediction_model_corrected.joblib')
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

try:
    vectorizer = joblib.load('data/vectorizer.pkl')
    print("Vectorizer loaded successfully!")
except Exception as e:
    print(f"Error loading vectorizer: {e}")

# Sentiment mapping: 0 -> Negative, 1 -> Positive
sentiment_mapping = {0: 'Negative', 1: 'Positive'}

# List of new texts (stock market-related news or comments)
new_data = [
    "Stock market reaches new heights today!",
    "Investors are concerned about potential crashes.",
    "Tech stocks show massive growth amid innovation."
]

# Process each text in new_data
for text in new_data:
    # Transform the text to match the vectorizer's format
    transformed_data = vectorizer.transform([text])

    # Get prediction from the model
    prediction = model.predict(transformed_data)

    # Map the prediction to sentiment
    sentiment = sentiment_mapping.get(prediction[0], 'Unknown')

    # Output result
    print(f"Text: {text}")
    print(f"Predicted sentiment: {sentiment}")
    print("-" * 50)

# Save results to a CSV file
try:
    with open('data/predictions.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Text", "Sentiment"])  # Write header row
        for text in new_data:
            transformed_data = vectorizer.transform([text])
            prediction = model.predict(transformed_data)
            sentiment = sentiment_mapping.get(prediction[0], 'Unknown')
            writer.writerow([text, sentiment])  # Write prediction results
    print("Predictions saved successfully in 'data/predictions.csv'")
except Exception as e:
    print(f"Error saving predictions to CSV: {e}")
