import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import shap

def train_model(data_path, target_column):
    # Load data
    data = pd.read_csv(data_path)

    # Feature selection
    features = data.drop(columns=[target_column])
    target = data[target_column]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Initialize model
    model = RandomForestClassifier(random_state=42)

    # Define parameter grid
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10]
    }

    # Initialize GridSearchCV
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)

    # Fit GridSearchCV
    grid_search.fit(X_train, y_train)

    # Best model
    best_model = grid_search.best_estimator_

    # Predict
    predictions = best_model.predict(X_test)

    # Evaluate
    accuracy = accuracy_score(y_test, predictions)
    print(f'Model Accuracy: {accuracy}')

    # SHAP values
    explainer = shap.TreeExplainer(best_model)
    shap_values = explainer.shap_values(X_test)

    # Plot SHAP values
    shap.summary_plot(shap_values, X_test)

if __name__ == "__main__":
    train_model('path/to/data.csv', 'moneyline_outcome')
