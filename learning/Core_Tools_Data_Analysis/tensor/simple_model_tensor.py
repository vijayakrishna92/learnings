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
min_val = tf.reduce_min(features)
max_val = tf.reduce_max(features)
features = (features - min_val) / (max_val - min_val)

# Dataset
dataset = tf.data.Dataset.from_tensor_slices((features, labels))
dataset = dataset.shuffle(buffer_size=4, seed=42).batch(2).repeat(10)

# Model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(4, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(2, activation='softmax')
])

# Compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train model
model.fit(dataset, steps_per_epoch=2, epochs=5)

# Evaluation
eval_dataset = tf.data.Dataset.from_tensor_slices((features, labels)).batch(2)
loss, acc = model.evaluate(eval_dataset)
print("Eval Loss:", loss, "Eval Accuracy:", acc)

# Prediction
pred = model.predict(tf.constant([[2.5]]))
print("Prediction (probabilities):", pred)
print("Predicted class:", tf.argmax(pred, axis=1).numpy())