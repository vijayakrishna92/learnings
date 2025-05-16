import tensorflow as tf

tensors = tf.constant([[1, 2, 3], [4, 5, 6]]) # 2D tensor
# constant() creates a constant tensor
# Create a 2D tensor with shape (2, 3) and data type int32
print(tensors)
print(tensors.shape)
print(tensors.dtype)

# variable can be modified while training. It stores and updates parameters during training, like weights and biases in neural networks.
b = tf.Variable([1, 2, 3])
b.assign_add([1, 1, 1])  # In-place addition
print("Variable b after adding 1s:", b)

size = tf.size(tensors) # Get the size of the tensor
print(size) # Get the size of the tensor

# dimension of the tensor 2,3
dim1 = tf.shape(tensors)[0] # Get the first dimension of the tensor
print(dim1) # Get the first dimension of the tensor
dim2 = tf.shape(tensors)[1] # Get the second dimension of the tensor
print(dim2) # Get the second dimension of the tensor

# slicer lets you grab specific sections of your data
tensors = tf.constant([1,2,3, 4,5,6])
slicer = tf.slice(tensors , begin=[0], size=[3])
print(slicer)

tensors = tf.constant([[1,2,3],[4,5,6]])
slicer = tf.slice(tensors, [0,0], [1,1]) # [0,0]- first row first column, Take 1 row, 1 columns
print(slicer) # tf.Tensor([[1]], shape=(1, 1), dtype=int32)

# gather = lets you grab specific elements or chunks of your data
tensors = tf.constant([1,2,3,4,5,6])
fav = tf.gather(tensors, indices=[1,2,3,4])
print(fav)
print(fav.numpy())


tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Indexing
print("First row:", tensor[0])

# Slicing
print("Second column:", tensor[:, 1])