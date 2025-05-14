import tensorflow as tf

tensors = tf.constant([[1, 2, 3], [4, 5, 6]]) # 2D tensor
# Create a 2D tensor with shape (2, 3) and data type int32
print(tensors)
print(tensors.shape)
print(tensors.dtype)