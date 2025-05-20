import tensorflow as tf
import numpy as np

# 1. Set seed for reproducibility
tf.random.set_seed(42)
np.random.seed(42)

# 2. Sample normalized data
features = tf.constant([[1.0], [2.0], [3.0], [4.0]])
labels = tf.constant([[0.0], [1.0], [1.0], [0.0]])

# Normalize features
features = (features - tf.reduce_min(features)) / (tf.reduce_max(features) - tf.reduce_min(features))
print("Normalized features:\n", features.numpy())

# 3. Define a custom model by subclassing
class MyModel(tf.keras.Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.dense1 = tf.keras.layers.Dense(4, activation='relu')
        self.dense2 = tf.keras.layers.Dense(1, activation='sigmoid')  # Binary output

    def call(self, inputs):
        x = self.dense1(inputs)
        return self.dense2(x)

# 4. Instantiate model, loss, optimizer
model = MyModel()
loss_fn = tf.keras.losses.BinaryCrossentropy()
optimizer = tf.keras.optimizers.Adam()

# 5. Custom training loop
EPOCHS = 5
for epoch in range(EPOCHS):
    with tf.GradientTape() as tape:
        predictions = model(features)
        loss = loss_fn(labels, predictions)
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))
    print(f"Epoch {epoch+1}, Loss: {loss.numpy():.4f}")

# 6. Save the model weights
model.save_weights("my_model_weights.weights.h5")

# 7. Load weights into a new instance
new_model = MyModel()
# Explicitly build the new_model before loading weights
# Provide the expected input shape (batch_size, number_of_features)
# The batch_size is None as it can vary.
new_model.build(input_shape=(None, 1))
new_model.load_weights("my_model_weights.weights.h5")

# 8. Make predictions with the loaded model
preds = new_model(features)
print("\nPredictions after loading weights:\n", preds.numpy())