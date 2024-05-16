import pandas as pd
import numpy as np
import tensorflow as tf

# Load data (including the data you want to predict)
data = pd.read_csv('newData2.csv')

# Convert datetime column to datetime type
data['time'] = pd.to_datetime(data['time'])

# Sort data by datetime
data = data.sort_values(by='time')

# Drop any NaN values
data = data.dropna()

# Extract features (X) excluding the direction column for the data you want to predict
X_to_predict = data[['open', 'high', 'low', 'close', 'volume']]

# Normalize features
X_to_predict_normalized = tf.keras.utils.normalize(X_to_predict.values)

# Load the trained model from disk
loaded_model = tf.keras.models.load_model('trained_model.keras')

# Perform inference with the loaded model to predict the direction
predicted_probabilities = loaded_model.predict(X_to_predict_normalized)

# Apply threshold to classify predictions
predicted_directions = (predicted_probabilities > 0.5).astype(int)  # Assuming threshold of 0.5

# Add the predicted direction to the DataFrame
data['predicted_direction'] = predicted_directions

# Extract features (X) for the last row to predict
X_last_row = X_to_predict.iloc[[-1]]

# Normalize features for the last row
X_last_row_normalized = tf.keras.utils.normalize(X_last_row.values)

# Predict direction for the last row
predicted_direction_last_row = loaded_model.predict_step(X_last_row_normalized)

# Append the predicted direction to the DataFrame
data.loc[len(data)] = [np.nan] * (len(data.columns) - 1) + [predicted_direction_last_row[0]]

# Print the DataFrame with the predicted direction
print(data)