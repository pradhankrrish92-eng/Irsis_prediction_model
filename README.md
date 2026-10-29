# 🌸 Iris Flower Classification using Random Forest

A beginner-friendly Machine Learning project that predicts iris flower species using the Random Forest Classification algorithm in Python.

## 📌 Project Overview

This project uses supervised Machine Learning to classify iris flowers into three species based on their physical measurements. The model is trained using the Iris dataset available through Scikit-learn.

The three species are:
- Iris Setosa
- Iris Versicolor
- Iris Virginica

## 🛠️ Technologies Used

- **Python** – Programming language
- **Scikit-learn** – Machine Learning library
- **Random Forest Classifier** – Classification algorithm
- **Joblib** – Saving and loading the trained model
- **Visual Studio Code** – Development environment

## 📂 Project Structure

```text
Iris_ML_Project/
│
├── train_model.py
├── predict.py
├── requirements.txt
├── iris_model.pkl
├── flower_names.pkl
└── README.md
```

## 📊 Dataset

The project uses the Iris dataset, which contains 150 samples and four input features:

- Sepal length (cm)
- Sepal width (cm)
- Petal length (cm)
- Petal width (cm)

The dataset contains three flower classes and is available directly through Scikit-learn, so no separate dataset download is required.

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Iris_ML_Project
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

**2. Install the dependencies**

```bash
python -m pip install -r requirements.txt
```

**3. Train the model**

```bash
python train_model.py
```

This trains the Random Forest classifier, evaluates its performance, and saves the model files.

**4. Make predictions**

```bash
python predict.py
```

Enter the four flower measurements when prompted to receive a predicted species.

## 🧠 Machine Learning Workflow

1. Load the Iris dataset.
2. Split the data into 80% training and 20% testing.
3. Train a Random Forest classifier with 100 decision trees.
4. Evaluate the model using accuracy, precision, recall, and F1-score.
5. Save the trained model using Joblib.
6. Predict flower species from user-provided measurements.

## 📈 Model Evaluation

The model reports its test accuracy and classification metrics when `train_model.py` runs. Actual performance depends on the dataset split and model configuration.

## 🎯 Learning Outcomes

- Understanding supervised Machine Learning
- Implementing a classification algorithm
- Training and testing a model
- Evaluating prediction performance
- Saving and reusing trained models

## 🚀 Future Improvements

- Build a web interface using Streamlit.
- Compare Random Forest with Logistic Regression and Decision Trees.
- Visualize dataset features and model performance.
- Deploy the model as a web application.

## 👨‍💻 Author

Created as a beginner Machine Learning project to gain practical experience with Python and classification algorithms.

## 📄 License

This project is available for educational and learning purposes.
