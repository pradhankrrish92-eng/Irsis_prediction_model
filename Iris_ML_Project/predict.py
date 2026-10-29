
import joblib

# Load the saved model and species names
model = joblib.load("iris_model.pkl")
flower_names = joblib.load("flower_names.pkl")

print("Iris Flower Species Predictor")

sepal_length = float(input("Sepal length (cm): "))
sepal_width = float(input("Sepal width (cm): "))
petal_length = float(input("Petal length (cm): "))
petal_width = float(input("Petal width (cm): "))

# Predict the flower species
features = [[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]]

prediction = model.predict(features)[0]
probabilities = model.predict_proba(features)[0]

print("\nPredicted species:", flower_names[prediction])
print(f"Model probability for this class: {probabilities[prediction]:.2%}")
5.