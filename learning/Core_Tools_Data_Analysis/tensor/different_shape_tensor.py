#Tensor rank, also known as the tensor's number of dimensions, is a fundamental concept in TensorFlow. It indicates the number of dimensions present in a tensor.
import tensorflow as tf

scalar = tf.constant(5)  # 0D tensor
print("Scalar:", scalar)
scalar_rank = tf.rank(scalar)  # Get the rank of the tensor
print("Rank of scalar:", scalar_rank)

vector = tf.constant([1, 2, 3])  # 1D tensor
print("Vector:", vector)
vector_rank = tf.rank(vector)  # Get the rank of the tensor
print("Rank of vector:", vector_rank)

matrix = tf.constant([[1, 2], [3, 4]])  # 2D tensor
print("Matrix:", matrix)
matrix_rank = tf.rank(matrix)  # Get the rank of the tensor
print("Rank of matrix:", matrix_rank)

tensor3d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # 3D tensor
print("3D Tensor:", tensor3d)
tensor3d_rank = tf.rank(tensor3d)  # Get the rank of the tensor
print("Rank of 3D tensor:", tensor3d_rank)
