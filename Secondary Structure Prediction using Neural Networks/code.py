# Import libraries
import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix
from torch.utils.data import DataLoader, TensorDataset

# ===========================
# 📌 1. Load and Preprocess Data
# ===========================
file_path = "/content/2018-06-06-pdb-intersect-pisces.csv"

df = pd.read_csv(file_path)

# ✅ Limit dataset size for speed
df = df.head(1000)

# ✅ Select numeric columns
df = df.select_dtypes(include=[np.number])

# ✅ Drop NaNs
df = df.dropna()

# ✅ Convert to NumPy arrays
X = df.iloc[:, :-1].values  # Features
y = df.iloc[:, -1].values   # Target

# ✅ Encode labels if categorical
if isinstance(y[0], str):
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)

# ✅ Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Convert to PyTorch tensors
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.long)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.long)

# ✅ Use DataLoader for speed
batch_size = 32
train_loader = DataLoader(TensorDataset(X_train_tensor, y_train_tensor), batch_size=batch_size, shuffle=True)

# ===========================
# 📌 2. Define Simplified Model
# ===========================
class FastStructureNet(nn.Module):
    def __init__(self):
        super(FastStructureNet, self).__init__()
        self.fc1 = nn.Linear(X_train.shape[1], 64)
        self.fc2 = nn.Linear(64, 3)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# ✅ Use GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = FastStructureNet().to(device)

# ===========================
# 📌 3. Train the Model
# ===========================
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# ✅ Reduce epochs for speed
epochs = 5

for epoch in range(epochs):
    for batch_X, batch_y in train_loader:
        batch_X, batch_y = batch_X.to(device), batch_y.to(device)
        optimizer.zero_grad()
        outputs = model(batch_X)
        loss = criterion(outputs, batch_y)
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item()}")

# ===========================
# 📌 4. Evaluate Model
# ===========================
with torch.no_grad():
    X_test_tensor = X_test_tensor.to(device)
    y_pred = model(X_test_tensor).argmax(dim=1).cpu().numpy()

# ✅ Accuracy Calculation
# Ensure y_test is integer type
y_test = y_test.astype(int)

# Ensure y_pred is integer
y_pred = y_pred.astype(int)

# Now compute accuracy
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.4f}")


# ===========================
# 📌 5. Visualize Results
# ===========================
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", xticklabels=["H", "E", "C"], yticklabels=["H", "E", "C"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Secondary Structure Prediction (Prototype)")
plt.show()
