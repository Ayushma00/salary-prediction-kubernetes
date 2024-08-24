import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def prepare_data(data):
    X = data.YearsExperience
    Y = data.Salary
    return X, Y


def preprocess_data(X, Y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.2, random_state=123
    )
    X_train = X_train.values.reshape(-1, 1)
    X_test = X_test.values.reshape(-1, 1)
    return X_train, X_test, y_train, y_test


def create_pipeline():
    # Create a pipeline with a scaler and linear regression model
    pipeline = Pipeline(
        [("scaler", StandardScaler()), ("regressor", LinearRegression())]
    )
    return pipeline


def save_pipeline(pipeline):
    # Save the model as a pickle file
    with open("model/linear_regression_model.pkl", "wb") as model_file:
        pickle.dump(pipeline, model_file)


def evaluate_model(pipeline, X_test, y_test):
    # Make predictions on the test set
    # Make predictions
    y_pred = pipeline.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")


def main():
    # Load the data
    data = pd.read_csv("Data/Salary.csv")

    # Prepare and preprocess data
    X, Y = prepare_data(data)
    X_train, X_test, y_train, y_test = preprocess_data(X, Y)

    # create pipeline

    pipeline = create_pipeline()
    pipeline.fit(X_train, y_train)

    evaluate_model(pipeline, X_test, y_test)

    # Save the trained pipeline
    save_pipeline(pipeline)


if __name__ == "__main__":
    main()
