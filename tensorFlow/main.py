import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
def main():
    # Read the CSV data
    data = pd.read_csv('2021.csv')

    # Convert categorical values to numerical labels
    #data['futureDirection'] = data['futureDirection'].map({'u': 0, 'd': 1, 'e': 2})

    # Extract features and labels
    features = data[['bid', 'ask', 'volume']]
    labels = data['futureDirection']

    # Split data into training and test sets
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.2, random_state=42)

    # Build and compile the model
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(3,)),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(3, activation='softmax')  # Output layer for multiclass classification
    ])

    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    # Train the model
    model.fit(train_features, train_labels, epochs=20, batch_size=32, validation_data=(test_features, test_labels))

    # Evaluate the model
    test_loss, test_acc = model.evaluate(test_features, test_labels)
    print(f"Test accuracy: {test_acc}")

    # Use the trained model for predictions on new data
    new_data = pd.read_csv("2021.csv")
    new_data_features = new_data[['bid', 'ask', 'volume']]
    predictions = model.predict(new_data_features)

if __name__ == "__main__":
    main()
