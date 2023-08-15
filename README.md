# PBJ

link to data: https://drive.google.com/drive/folders/102zj3t7cxEiH1rAkVY_Qx5ehUcKy9Y_Y?usp=sharing

# Needs to be fixed:
getting the last pieces of takes prices from the bottom initially instead of at the top. a better solution would be to start running from the 20th price.


# Links
https://pypi.org/project/oandapyV20/
https://pypi.org/project/backtrader/
https://pypi.org/project/stock-indicators/

# To Do
1. Jack to add stop loss to ema crossover
2. Jack - Make stop loss work with conditions
3. add emas to T.F
4. Pet recreate ema strat in meta trader to backtrade
5. Pet create strat in live trader -aim to strat it on monday 

# Indicator Ideas
Code up the Very Wet Ass Pussy  
Create bollinger bands that are 1 standard deviation away from the VWAP that act as support and resistance levels 
Combine this with  EMA to show when trending down or  up from the bollinger 

Need some logic like:
- if hit top bollinger last and ST EMA cross below LT EMA then Sell order
- combine with trailing stop
- if hit bottom bollinger last and ST EMA cross above LT EMA then Buy order
- 
https://medium.com/@nusfintech.ml/fx-algorithmic-trading-with-machine-learning-models-7d6821fa7e67


# chatgpt tf improvments

Your code is a good starting point, but there are several improvements and best practices you can consider to make it more robust and maintainable. Here are some suggestions:

    Modularize and Functions:
    Break down your code into smaller functions. This makes the code easier to read, test, and maintain. Each function should have a clear purpose and responsibilities.

    Data Preprocessing Function:
    Create a function specifically for data preprocessing. This will ensure consistency and make it easier to apply the same preprocessing steps to new data.

    Parameterization:
    Use variables or constants for parameters like batch size, number of epochs, and file paths. This makes it easier to adjust these values without changing them throughout the code.

    Validation Split:
    When splitting the data, consider having a separate validation set in addition to the test set. The validation set is used during training for early stopping and hyperparameter tuning, while the test set is used for final evaluation.

    Early Stopping:
    Implement early stopping to prevent overfitting. Monitor a validation metric (e.g., validation loss) and stop training if it doesn't improve for a certain number of epochs.

    Model Architecture and Hyperparameter Tuning:
    Experiment with different model architectures, layer sizes, and activation functions. You can also use techniques like grid search or random search for hyperparameter tuning.

    Model Evaluation Metrics:
    Consider using additional evaluation metrics such as precision, recall, F1-score, or confusion matrix to better understand the model's performance.

    Logging and Printing:
    Use logging libraries to output information instead of using print(). This allows for better control over logging levels and formatting.

    Error Handling:
    Implement error handling to gracefully handle exceptions, file not found errors, and other potential issues that may arise during execution.

    Documentation:
    Include comments and docstrings to explain the purpose of each function, parameter, and step. This will help you and others understand the code later.

    Separate Files:
    If the code becomes more complex, consider organizing it into separate files, such as one for data preprocessing, one for model building, and another for training and evaluation.
