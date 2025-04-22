import numpy as np
import tensorflow as tf
from tensorflow import keras
from geneticalgorithm import geneticalgorithm as ga  # Install using: pip install geneticalgorithm

# Simulated dataset (features: temperature, airflow, feed rate | target: drying efficiency)
np.random.seed(42)
X = np.random.rand(100, 3)  # Features: 100 samples, 3 parameters
y = np.random.rand(100, 1)  # Target: drying efficiency

# Define a simple neural network model
def create_model(learning_rate, neurons):
    model = keras.Sequential([
        keras.layers.Dense(int(neurons), activation='relu', input_shape=(3,)),
        keras.layers.Dense(1, activation='linear')
    ])
    model.compile(optimizer=keras.optimizers.Adam(learning_rate), loss='mse')
    return model

# Objective function for Genetic Algorithm (minimizing loss)
def objective_function(params):
    lr, neurons = params
    model = create_model(lr, neurons)
    model.fit(X, y, epochs=10, verbose=0, batch_size=5)  # Train model
    loss = model.evaluate(X, y, verbose=0)
    return loss

# GA parameter bounds
var_bounds = np.array([[0.001, 0.1],  # Learning rate range
                        [5, 100]])     # Neurons in the hidden layer

# Run Genetic Algorithm for optimization
algorithm_param = {'max_num_iteration': 50, 'population_size': 10}
model_ga = ga(function=objective_function, dimension=2, variable_type='real', variable_boundaries=var_bounds, algorithm_parameters=algorithm_param)

model_ga.run()

# Best Parameters
best_params = model_ga.output_dict['variable']
print("Optimized Learning Rate:", best_params[0])
print("Optimized Number of Neurons:", int(best_params[1]))
