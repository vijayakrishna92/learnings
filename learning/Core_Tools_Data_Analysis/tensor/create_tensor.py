import tensorflow as tf

tensors = tf.constant([[1, 2, 3], [4, 5, 6]]) # 2D tensor
# constant() creates a constant tensor
# Create a 2D tensor with shape (2, 3) and data type int32
print(tensors)
print(tensors.shape)
print(tensors.dtype)

size = tf.size(tensors) # Get the size of the tensor
print(size) # Get the size of the tensor

# dimension of the tensor 2,3
dim1 = tf.shape(tensors)[0] # Get the first dimension of the tensor
print(dim1) # Get the first dimension of the tensor
dim2 = tf.shape(tensors)[1] # Get the second dimension of the tensor
print(dim2) # Get the second dimension of the tensor
