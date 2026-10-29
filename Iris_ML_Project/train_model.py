
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the free Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create and train the Random Forest model
model = RandomForestClassifier(
    n_estimators=100, random_state=42
)
model.fit(X_train, y_train)

# Evaluate the model on unseen test data
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Iris Flower Classification Model")
print("--------------------------------")
print(f"Dataset size: {len(X)}")
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")
print(f"Accuracy: {accuracy:.2%}")
print("\nClassification Report:")
print(classification_report(
    y_test, predictions, target_names=iris.target_names
))

# Save the trained model
joblib.dump(model, "iris_model.pkl")
joblib.dump(iris.target_names, "flower_names.pkl")

print("Model saved successfully!")
