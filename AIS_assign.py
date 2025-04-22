import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Simulated dataset
# Columns: [feature1, feature2, ..., featureN], last col: 0 (healthy), 1 (damaged)
# Replace this with real sensor data
# data = np.array([
#     [0.2, 0.1, 0.3, 0],
#     [0.25, 0.15, 0.35, 0],
#     [0.6, 0.7, 0.8, 1],
#     [0.65, 0.75, 0.85, 1],
#     [0.3, 0.2, 0.4, 0],
#     [0.7, 0.8, 0.9, 1],
#     [0.1, 0.05, 0.2, 0]
# ])

# Generate more data
healthy = np.random.normal(loc=0.2, scale=0.05, size=(20, 3))
damaged = np.random.normal(loc=0.7, scale=0.05, size=(20, 3))

# Label them
healthy = np.hstack((healthy, np.zeros((20, 1))))
damaged = np.hstack((damaged, np.ones((20, 1))))

# Combine
data = np.vstack((healthy, damaged))


# Split features and labels
X = data[:, :-1]
y = data[:, -1]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Simple Negative Selection Algorithm (NSA)
# Self = healthy (label 0), Non-self = damaged (label 1)
# Memory detectors = patterns that match damaged structure signatures
def train_nsa(X_train, y_train):
    detectors = []
    for x, y in zip(X_train, y_train):
        if y == 1:  # learn non-self patterns only
            detectors.append(x)
    return detectors

# Check if input matches any detector (i.e., is "damaged")
def classify_nsa(x, detectors, threshold=0.2):
    for d in detectors:
        if np.linalg.norm(x - d) < threshold:
            return 1  # classified as damaged
    return 0  # classified as healthy

# Train phase
detectors = train_nsa(X_train, y_train)

# Predict phase
y_pred = np.array([classify_nsa(x, detectors) for x in X_test])

# Accuracy
print("Predicted:", y_pred)
print("Actual:   ", y_test.astype(int))
print("Accuracy:", accuracy_score(y_test, y_pred))
