# -*- coding: utf-8 -*-
"""DataScience_Task.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18LXCnx1Pd0082bzwS9fkFk_X8RSLcY9l
"""

pip install neo4j pandas scikit-learn numpy

from neo4j import GraphDatabase
import networkx as nx
import pandas as pd

class Neo4jConnection:
    def __init__(self, uri, username, password):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))
        print("Connected to Neo4j")

    def close(self):
        self.driver.close()
        print("Connection closed")

    def fetch_graph(self):
        with self.driver.session() as session:
            result = session.run("MATCH (n)-[r]->(m) WHERE n.nodeId IS NOT NULL AND m.nodeId IS NOT NULL RETURN n.nodeId, m.nodeId")
            G = nx.Graph()
            for record in result:
                if record['n.nodeId'] and record['m.nodeId']:
                    G.add_edge(record['n.nodeId'], record['m.nodeId'])
            return G

    def get_nodes(self): # Add a method to fetch nodes
        with self.driver.session() as session:
            result = session.run("MATCH (n) RETURN n LIMIT 10")
            for record in result:
                print(record)

# Example usage
uri = "neo4j+s://e489e4b4.databases.neo4j.io"
username = "neo4j"
password = "kQr4i6xQG-tahsSDLWNb18_YDZpm1pTmbN03IVNBt3w"
conn = Neo4jConnection(uri, username, password)

# Establish Neo4j connection and run the query
with conn.driver.session() as session:
    result = session.run("MATCH (n)-[r]->(m) RETURN n, r, m LIMIT 1000")

    # Initialize an empty list to store the data
    data = []

    # Loop through each record and extract relevant information
    for record in result:
        start_node = record["n"]
        relationship = record["r"]
        end_node = record["m"]

        # Append the data in the required format
        data.append((
            start_node.element_id,  # Start Node ID
            relationship.type,      # Relationship Type
            end_node.element_id     # End Node ID
        ))

# Create a DataFrame from the collected data
df = pd.DataFrame(data, columns=["Start Node ID", "Relationship Type", "End Node ID"])

# Print the DataFrame
print(df)

shareholding_count = df[df["Relationship Type"] == "Shareholding"].shape[0]
print(f"Number of 'Shareholding' relationships: {shareholding_count}")

import random

# Get unique node IDs from the DataFrame
nodes = list(set(df["Start Node ID"].tolist() + df["End Node ID"].tolist()))

negative_samples = []

while len(negative_samples) < len(df):
    source, target = random.sample(nodes, 2)
    if not ((df["Start Node ID"] == source) & (df["End Node ID"] == target)).any():
        negative_samples.append((source, target))

print("Negative Samples:", negative_samples)

import pandas as pd
import numpy as np
import networkx as nx  # Import networkx

# ... (Your existing code) ...

# Assuming df (positive samples) and negative_samples are already defined
positive_samples = [(row["Start Node ID"], row["End Node ID"])
                   for _, row in df.iterrows()]

# Create labels: 1 for positive samples, 0 for negative samples
labels = [1] * len(positive_samples) + [0] * len(negative_samples)

# Combine positive and negative samples
samples = positive_samples + negative_samples

# Create a NetworkX graph from the DataFrame for easy neighbor calculations
G = nx.from_pandas_edgelist(df, source="Start Node ID", target="End Node ID")
neighbors = {node: set(G.neighbors(node)) for node in G.nodes()}
node_degrees = dict(G.degree()) # Calculate node degrees

# Example feature extraction:
# Common neighbors count using the previously defined function
def common_neighbors_count(source, target, neighbors):
    if source in neighbors and target in neighbors:
        common_neighbors = neighbors[source].intersection(neighbors[target])
        return len(common_neighbors)
    return 0  # Return 0 if no common neighbors

# Create features
features = {
    "common_neighbors": [
        common_neighbors_count(source, target, neighbors)
        for source, target in samples
    ],
    "node_degrees": [
        node_degrees.get(s, 0) + node_degrees.get(t, 0) for s, t in samples
    ],  # Degree sum for each node pair
}

# Create DataFrame
data = pd.DataFrame(features)

# Add labels column
data["label"] = labels

# Preview the data
print(data.head())


def jaccard_similarity(source, target, neighbors):
    # Jaccard similarity = |A ∩ B| / |A ∪ B| for two sets A and B
    if source in neighbors and target in neighbors:
        common = len(neighbors[source].intersection(neighbors[target]))
        union = len(neighbors[source].union(neighbors[target]))
        return common / union if union != 0 else 0
    return 0


def adamic_adar_index(source, target, neighbors, node_degrees):
    if source in neighbors and target in neighbors:
        common_neighbors = neighbors[source].intersection(neighbors[target])
        return sum(
            1 / np.log(node_degrees.get(neighbor, 1))
            for neighbor in common_neighbors)
    return 0


# Adding new features: Jaccard similarity and Adamic-Adar index
features = {
    "common_neighbors": [
        common_neighbors_count(source, target, neighbors)
        for source, target in samples
    ],
    "node_degrees": [
        node_degrees.get(s, 0) + node_degrees.get(t, 0) for s, t in samples
    ],
    "jaccard_similarity": [
        jaccard_similarity(source, target, neighbors) for source, target in samples
    ],
    "adamic_adar_index": [
        adamic_adar_index(source, target, neighbors, node_degrees)
        for source, target in samples
    ]
}

# Create DataFrame
data = pd.DataFrame(features)

# Add labels column
data["label"] = labels

# Preview the data
print(data.head())

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score, KFold  # Import KFold
from sklearn.metrics import accuracy_score

# Assuming 'data' is the DataFrame with features and labels
X = data.drop(columns=["label"])  # Features
y = data["label"]  # Labels

# Split data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the RandomForestClassifier
model = RandomForestClassifier(random_state=42)

# Hyperparameter tuning with GridSearchCV
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# GridSearchCV to find the best hyperparameters
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=KFold(n_splits=5), n_jobs=-1, verbose=2) # Use KFold
grid_search.fit(X_train, y_train)

# Best parameters from GridSearchCV
best_params = grid_search.best_params_
print("Best Hyperparameters:", best_params)

# Using the best model from GridSearchCV
best_model = grid_search.best_estimator_

# Cross-validation
cv_scores = cross_val_score(best_model, X, y, cv=5, scoring='accuracy')
print(f"Cross-validation accuracy scores: {cv_scores}")
print(f"Mean cross-validation accuracy: {cv_scores.mean():.4f}")

# Fit the best model on the training data
best_model.fit(X_train, y_train)

# Predict on the test set
y_pred = best_model.predict(X_test)

# Print accuracy score
print("Test Set Accuracy:", accuracy_score(y_test, y_pred))

# Example for getting node pairs from your DataFrame (df)
for index, row in df.iterrows():
    source_node = row["Start Node ID"]
    target_node = row["End Node ID"]
    print(f"Source Node: {source_node}, Target Node: {target_node}")

def predict_link(source, target, best_model, neighbors, node_degrees): # Added parameters
    # Extract features
    features = {
        "common_neighbors": common_neighbors_count(source, target, neighbors), # Fixed: Call common_neighbors_count
        "node_degrees": node_degrees.get(source, 0) + node_degrees.get(target, 0),  # Fixed: Use get to handle missing keys
        "jaccard_similarity": jaccard_similarity(source, target, neighbors), # Added
        "adamic_adar_index": adamic_adar_index(source, target, neighbors, node_degrees) # Added
    }

    # Create a DataFrame with the correct feature names
    input_data = pd.DataFrame([features])

    # Predict using the trained model
    return best_model.predict(input_data)[0]

# Example prediction for True
source_node = "4:8f968eb2-b3e1-4874-8050-befcbd2e05e9:0" # Uncommented and assigned a value
target_node = "4:8f968eb2-b3e1-4874-8050-befcbd2e05e9:1894" # Uncommented and assigned a value

# Pass 'neighbors' and 'node_degrees' to the function
prediction = predict_link(source_node, target_node, best_model, neighbors, node_degrees) # Modified call
print("Predicted Link:", prediction)

#Example prediction for False
source_node = "4:8f968eb2-b3e1-4874-8050-befcbd2e05e9:0" # Uncommented and assigned a value
target_node = "4:8f968eb2-b3e1-4874-8050-befcbd2e05e9:1" # Uncommented and assigned a value

# Pass 'neighbors' and 'node_degrees' to the function
prediction = predict_link(source_node, target_node, best_model, neighbors, node_degrees) # Modified call
print("Predicted Link:", prediction)

from neo4j import GraphDatabase
import networkx as nx
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score, KFold
from sklearn.metrics import accuracy_score

# Step 1: Connect to Neo4j Database
driver = GraphDatabase.driver("neo4j+s://e489e4b4.databases.neo4j.io", auth=("neo4j","kQr4i6xQG-tahsSDLWNb18_YDZpm1pTmbN03IVNBt3w"))

# Function to extract node pairs (edges) from Neo4j
def get_node_pairs():
    with driver.session() as session:
        query = """
        MATCH (n1)-[r]->(n2)
        RETURN n1.id AS source, n2.id AS target
        """
        result = session.run(query)
        return [(record["source"], record["target"]) for record in result]

# Step 2: Extract Node Pairs (Positive Samples)
node_pairs = get_node_pairs()

# Step 3: Generate Negative Samples (Random node pairs not in the graph)
def generate_negative_samples(node_pairs, nodes):
    negative_samples = []
    while len(negative_samples) < len(node_pairs):
        source, target = np.random.choice(nodes, 2, replace=False)
        if (source, target) not in node_pairs and (target, source) not in node_pairs:
            negative_samples.append((source, target))
    return negative_samples

# Assuming that the set of nodes is known or extracted from Neo4j
nodes = set([node for pair in node_pairs for node in pair])
negative_samples = generate_negative_samples(node_pairs, nodes)

# Step 4: Create Features for Link Prediction
def common_neighbors_count(source, target, neighbors):
    if source in neighbors and target in neighbors:
        return len(neighbors[source].intersection(neighbors[target]))
    return 0

def jaccard_similarity(source, target, neighbors):
    if source in neighbors and target in neighbors:
        common = len(neighbors[source].intersection(neighbors[target]))
        union = len(neighbors[source].union(neighbors[target]))
        return common / union if union != 0 else 0
    return 0

def adamic_adar_index(source, target, neighbors, node_degrees):
    if source in neighbors and target in neighbors:
        common_neighbors = neighbors[source].intersection(neighbors[target])
        return sum(1 / np.log(node_degrees.get(neighbor, 1)) for neighbor in common_neighbors)
    return 0

# Step 5: Create DataFrame for Model Training
# Create NetworkX graph from node pairs
G = nx.Graph()
G.add_edges_from(node_pairs)

# Get neighbors and degrees of nodes
neighbors = {node: set(G.neighbors(node)) for node in G.nodes()}
node_degrees = dict(G.degree())

# Prepare positive and negative samples with features
samples = node_pairs + negative_samples
labels = [1] * len(node_pairs) + [0] * len(negative_samples)

features = {
    "common_neighbors": [
        common_neighbors_count(source, target, neighbors) for source, target in samples
    ],
    "jaccard_similarity": [
        jaccard_similarity(source, target, neighbors) for source, target in samples
    ],
    "adamic_adar_index": [
        adamic_adar_index(source, target, neighbors, node_degrees) for source, target in samples
    ],
    "node_degrees": [
        node_degrees.get(source, 0) + node_degrees.get(target, 0) for source, target in samples
    ]
}

# Create a DataFrame
data = pd.DataFrame(features)
data["label"] = labels

# Step 6: Train the Model (Random Forest)
X = data.drop(columns=["label"])  # Features
y = data["label"]  # Labels

# Split data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the RandomForestClassifier
model = RandomForestClassifier(random_state=42)

# Hyperparameter tuning with GridSearchCV
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# GridSearchCV to find the best hyperparameters
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=KFold(n_splits=5), n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

# Best parameters from GridSearchCV
best_params = grid_search.best_params_
print("Best Hyperparameters:", best_params)

# Using the best model from GridSearchCV
best_model = grid_search.best_estimator_

# Cross-validation
cv_scores = cross_val_score(best_model, X, y, cv=5, scoring='accuracy')
print(f"Cross-validation accuracy scores: {cv_scores}")
print(f"Mean cross-validation accuracy: {cv_scores.mean():.4f}")

# Fit the best model on the training data
best_model.fit(X_train, y_train)

# Predict on the test set
y_pred = best_model.predict(X_test)

# Print accuracy score
print("Test Set Accuracy:", accuracy_score(y_test, y_pred))

# Step 7: Make Predictions on New Links
def predict_link(source, target, best_model, neighbors, node_degrees):
    features = {
        "common_neighbors": common_neighbors_count(source, target, neighbors),
        "node_degrees": node_degrees.get(source, 0) + node_degrees.get(target, 0),
        "jaccard_similarity": jaccard_similarity(source, target, neighbors),
        "adamic_adar_index": adamic_adar_index(source, target, neighbors, node_degrees)
    }
    input_data = pd.DataFrame([features])
    return best_model.predict(input_data)[0]

# Example prediction for a new pair of nodes
source_node = "4:8f968eb2-b3e1-4874-8050-befcbd2e05e9:0"
target_node = "4:8f968eb2-b3e1-4874-8050-befcbd2e05e9:1894"
prediction = predict_link(source_node, target_node, best_model, neighbors, node_degrees)
print(f"Predicted Link for ({source_node}, {target_node}):", prediction)

!pip install neo4j