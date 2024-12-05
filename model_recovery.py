from joblib import dump, load

# Attempt to load as joblib (in case it was saved incorrectly)
try:
    model = load('data/stock_prediction_model.pkl')
    print("Loaded using joblib!")
    dump(model, 'data/stock_prediction_model_corrected.joblib')
    print("Model saved as corrected .joblib!")
except Exception as e:
    print(f"Error loading model with joblib: {e}")

# Attempt to read and re-save the file in binary mode
try:
    with open('data/stock_prediction_model.pkl', 'rb') as corrupted_file:
        content = corrupted_file.read()
    with open('data/stock_prediction_model_corrected.pkl', 'wb') as corrected_file:
        corrected_file.write(content)
    print("Corrupted file re-encoded and saved!")
except Exception as e:
    print(f"Error re-encoding file: {e}")
