# 🧬 Secondary Structure Prediction using Neural Networks

## 📌 Overview

This project implements a **neural network** to classify protein secondary structures into **Helix (H), Sheet (E), and Coil (C)** using PyTorch. The model is a **fully connected feedforward neural network (FCNN)** trained on structural data from the **PDB dataset**.

## 📂 Dataset

The dataset used is **2018-06-06-pdb-intersect-pisces.csv**, which contains numerical features related to protein structures.

## 🚀 Features

- **Preprocessing:** Handles missing values, numerical encoding, and train-test splitting.
- **Neural Network Model:** A simple **Multi-Layer Perceptron (MLP)** with one hidden layer.
- **Training:** Uses **CrossEntropyLoss** and **Adam optimizer**.
- **Evaluation:** Computes accuracy and confusion matrix for performance analysis.
- **Visualization:** Heatmap of predicted vs. actual secondary structures.

## 📦 Dependencies

Ensure you have the following Python libraries installed:

```bash
pip install torch numpy pandas scikit-learn matplotlib seaborn
```

## 🔧 Setup & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/secondary-structure-prediction.git
   cd secondary-structure-prediction
   ```
2. Place the dataset file (`2018-06-06-pdb-intersect-pisces.csv`) in the project directory.
3. Run the training script:
   ```bash
   python train.py
   ```

## 📜 Code Breakdown

### 1️⃣ Load and Preprocess Data

- Reads the dataset and selects only numeric columns.
- Handles missing values and converts data into NumPy arrays.
- Performs **Train-Test Split** (80-20 ratio).
- Converts data into **PyTorch tensors** for training.

### 2️⃣ Define the Neural Network Model

A simple feedforward network with:

- **Input Layer** (based on dataset features)
- **Hidden Layer** (64 neurons, ReLU activation)
- **Output Layer** (3 neurons, one for each class)

### 3️⃣ Train the Model

- Uses **CrossEntropyLoss** for classification.
- Optimized with **Adam optimizer (lr=0.01)**.
- Trained for **5 epochs** with **batch size = 32**.

### 4️⃣ Evaluate Performance

- Computes accuracy using `accuracy_score`.
- Generates a **confusion matrix** to visualize predictions.

### 5️⃣ Visualize Results

- Uses **seaborn** to create a heatmap of the confusion matrix.

## 🎯 Results

The model predicts secondary structures with an accuracy of **\~90%** (varies based on dataset size and hyperparameters).

## 🔥 Future Improvements

- Add **more hidden layers** for deeper learning.
- Experiment with **CNNs or RNNs (LSTMs)** for sequential structure learning.
- Implement **data augmentation** for better generalization.

## 🏆 Contributing

Feel free to fork this project and contribute improvements! 🚀

## 📜 License

This project is open-source and available under the **MIT License**.

---

📌 **Author:** Ankit Sharma📅 **Last Updated:** February 2025
