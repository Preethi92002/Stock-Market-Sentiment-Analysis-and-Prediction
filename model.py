import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load sentiment data
data_path = 'data/sentiment_analysis.csv'  # Adjust the path if needed
data = pd.read_csv(data_path)

# Preprocess data
# Assuming 'Message' is the text column and 'Sentiment Score' is the feature
data.dropna(subset=['Message'], inplace=True)  # Drop rows with missing messages

# Binarize Sentiment Scores (for classification task: positive/negative)
data['Sentiment Label'] = data['Sentiment Score'].apply(lambda x: 1 if x > 0 else 0)

# Split data into features (X) and target (y)
X = data['Message']
y = data['Sentiment Label']

# Convert text into numerical features using CountVectorizer
vectorizer = CountVectorizer(max_features=5000)  # Adjust max_features if needed
X_vectorized = vectorizer.fit_transform(X)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Build and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save the model (Optional)
import joblib
model_path = 'data/stock_prediction_model.pkl'
joblib.dump(model, model_path)
print(f"Model saved to {model_path}")
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Save the vectorizer
with open('data/vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)
print("Vectorizer saved successfully!")
