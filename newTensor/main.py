import pandas as pd  # Import pandas library for data manipulation
import tensorflow as tf  # Import TensorFlow library for machine learning
# import matplotlib.pyplot as plt  # Import matplotlib library for visualization

# Load data from CSV file using pandas
data = pd.read_csv('EUR_USD_D_2024_04_02T21_00_00_2020_05_27T21_00_00_1000processed.csv')

# Convert 'datetime' column to datetime type for time series analysis
data['time'] = pd.to_datetime(data['time'])

# Sort data by 'datetime' column to ensure chronological order
data = data.sort_values(by='time')

# Drop any rows with missing values (NaN) to ensure data integrity
data = data.dropna()

# Split data into features (X) and target (y)
X = data[['open', 'high', 'low', 'close', 'volume']]  # Features: open, high, low, close, volume
y = data['direction']  # Target variable: direction

# Normalize features using TensorFlow's normalization function to scale them between 0 and 1
X_normalized = tf.keras.utils.normalize(X.values)

# Split data into training and testing sets (80% training, 20% testing) for model evaluation
split = int(0.8 * len(X_normalized))  # Calculate the index to split the data
X_train, X_test = X_normalized[:split], X_normalized[split:]  # Split features into training and testing sets
y_train, y_test = y[:split], y[split:]  # Split target variable into training and testing sets

# Define the architecture of the neural network model using TensorFlow's Sequential API
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    # Input layer with 64 neurons, ReLU activation function, and input shape matching the number of features
    tf.keras.layers.Dense(32, activation='relu'),
    # Hidden layer with 32 neurons and ReLU activation function
    tf.keras.layers.Dense(1, activation='sigmoid')
    # Output layer with 1 neuron and sigmoid activation function for binary classification
])

# Compile the model, specifying the optimizer, loss function, and evaluation metric
model.compile(optimizer='adam',  # Adam optimizer, widely used for its adaptive learning rate
              loss='binary_crossentropy',  # Binary crossentropy loss for binary classification
              metrics=['accuracy'])  # Metrics to monitor during training: accuracy

# Print a summary of the model architecture, including the number of parameters
print(model.summary())

# Train the model using training data, specifying the number of epochs and batch size
history = model.fit(X_train, y_train, epochs=10, batch_size=64, validation_split=0.2)
# Train the model for 10 epochs with a batch size of 64, using 20% of the training data for validation

model.save('trained_model.keras')  # Save the trained model to a directory named 'trained_model'

# # Plot training history to visualize model performance over epochs
# plt.plot(history.history['accuracy'], label='accuracy')  # Training accuracy
# plt.plot(history.history['val_accuracy'], label='val_accuracy')  # Validation accuracy
# plt.xlabel('Epoch')  # Label for x-axis
# plt.ylabel('Accuracy')  # Label for y-axis
# plt.legend()  # Display legend
# plt.show()  # Show the plot

# Evaluate the trained model on test data to assess its performance
loss, accuracy = model.evaluate(X_test, y_test)
# Evaluate model performance on the test set, computing loss and accuracy
print(f'Test Loss: {loss}')  # Print test loss
print(f'Test Accuracy: {accuracy}')  # Print test accuracy
