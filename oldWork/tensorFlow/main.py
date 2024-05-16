import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split


def main():
    # Read the CSV data
    data = pd.read_csv('EUR_USD_D_2024_04_02T21_00_00_2020_05_27T21_00_00_1000processed.csv')

    # Extract features and labels from the data
    # Features are bid, ask, and volume columns
    features = data[['open', 'high', 'low', 'close', 'volume']]

    # Labels are the 'direction' column
    labels = data['direction']

    # Split the data into training and test sets
    # This helps in evaluating the model's performance
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.2,
                                                                                random_state=42)

    # Build the neural network model
    model = tf.keras.models.Sequential([
        # Input layer with 3 neurons (bid, ask, volume)
        tf.keras.layers.Dense(64, activation='relu', input_shape=(5,)),

        # Hidden layer with 32 neurons and ReLU activation function
        tf.keras.layers.Dense(32, activation='relu'),

        # Output layer with 3 neurons (for multiclass classification)
        tf.keras.layers.Dense(5, activation='softmax')
    ])

    # Compile the model
    # Use sparse categorical cross-entropy loss for multiclass classification
    # Optimizer is 'adam' which adjusts the learning rate during training
    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    # Train the model using training data
    # Specify batch size and number of epochs
    # Validation data is used to monitor model performance during training
    model.fit(train_features, train_labels, epochs=20, batch_size=32, validation_data=(test_features, test_labels))

    # Evaluate the model's performance on test data
    test_loss, test_acc = model.evaluate(test_features, test_labels)
    print(f"Test accuracy: {test_acc}")

    # Use the trained model for predictions on new data
    new_data = pd.read_csv("2022.csv")
    new_data_features = new_data[['bid', 'ask', 'volume']]
    predictions = model.predict(new_data_features)

    # Save the trained model to a directory named 'trained_model'
    model.save('trained_model')


if __name__ == "__main__":
    main()