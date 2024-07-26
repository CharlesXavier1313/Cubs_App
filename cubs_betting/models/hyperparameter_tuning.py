import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# Load data
data = pd.read_csv('path/to/data.csv')

# Feature selection
features = data[['feature1', 'feature2', 'feature3']]
target = data['moneyline_outcome']

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

# Best parameters
print(f'Best parameters: {grid_search.best_params_}')

# Best model
best_model = grid_search.best_estimator_

# Predict
predictions = best_model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, predictions)
print(f'Moneyline Model Accuracy after Tuning: {accuracy}')
