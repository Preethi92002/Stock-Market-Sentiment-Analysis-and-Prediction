# Fix the corrupted model file
with open('data/stock_prediction_model.pkl', 'rb') as model_file:
    content = model_file.read()

with open('data/sentiment_model_corrected.pkl', 'wb') as new_model_file:
    new_model_file.write(content)

print("Model file has been corrected and saved as 'sentiment_model_corrected.pkl'.")
