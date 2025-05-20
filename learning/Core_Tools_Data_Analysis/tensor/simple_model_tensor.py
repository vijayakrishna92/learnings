import tensorflow as tf
import numpy as np
import random
import os

def set_seed(seed=42):
    tf.random.set_seed(seed)
    np.random.seed(seed)
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)

set_seed(42)

# Sample data
features = tf.constant([[1.0], [2.0], [3.0], [4.0]])
labels = tf.constant([0, 1, 1, 0])

# Normalize features
'''Scales feature values to a 0–1 range.
Makes training faster and more stable because it prevents some features from dominating others due to scale.
Common step in preprocessing, especially for neural networks.'''
min_val = tf.reduce_min(features)
max_val = tf.reduce_max(features)
features = (features - min_val) / (max_val - min_val)

# Dataset
'''Converts raw data into a TensorFlow data pipeline.
Key operations:
    shuffle: randomizes the order to reduce learning bias.
    batch: splits data into smaller chunks to speed up training.
    repeat: allows multiple passes over the dataset.'''
dataset = tf.data.Dataset.from_tensor_slices((features, labels))
dataset = dataset.shuffle(buffer_size=4, seed=42).batch(2).repeat(10)

# Model
'''Defines a sequential neural network with:
One hidden layer (with activation function like ReLU).
One output layer (softmax for classification into two classes).
Simple architecture suitable for binary/multi-class classification.'''
model = tf.keras.Sequential([
    tf.keras.layers.Dense(4, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(2, activation='softmax')
])

# Compile model
'''Prepares the model for training:
optimizer: adjusts weights during training (Adam is adaptive and efficient).
loss: measures how wrong the model is (used to update weights).
metrics: tracks performance (accuracy in this case).'''
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train model
'''Starts the training process:
Feeds batches of data to the model.
Updates weights based on loss.
Repeats over several epochs (full dataset passes).'''
model.fit(dataset, steps_per_epoch=2, epochs=5)

# Evaluation
'''Tests the model’s performance on data it has already seen.
Gives you loss and accuracy, helping you gauge if the model learned anything meaningful.'''
eval_dataset = tf.data.Dataset.from_tensor_slices((features, labels)).batch(2)
loss, acc = model.evaluate(eval_dataset)
print("Eval Loss:", loss, "Eval Accuracy:", acc)

# Prediction
'''Lets you use the trained model to predict the class of a new input (e.g., 2.5).
Gives:
Probabilities for each class (via softmax).
Predicted class with the highest probability.'''
pred = model.predict(tf.constant([[2.5]]))
print("Prediction (probabilities):", pred)
print("Predicted class:", tf.argmax(pred, axis=1).numpy())