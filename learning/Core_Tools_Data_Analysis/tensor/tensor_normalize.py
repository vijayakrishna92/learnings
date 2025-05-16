'''
normalized= x−min(x)/(max(x)−min(x))
Scales data (e.g., 0–255 → 0–1)
 Helps model train faster and converge better.
'''
import tensorflow as tf

features = tf.constant([[1.0], [2.0], [3.0], [4.0]])
labels = tf.constant([0, 1, 1, 0])

# Min and Max
min_val = tf.reduce_min(features)
max_val = tf.reduce_max(features)

# Normalize
normalized_features = (features - min_val) / (max_val - min_val)

print("Normalized features:\n", normalized_features.numpy())