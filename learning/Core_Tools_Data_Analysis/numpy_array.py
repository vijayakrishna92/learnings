#numpy array
import numpy as np

np_array = np.array([1, 2, 3, 4, 5]) # Create a numpy array with values from 1 to 5
print(np_array) # Print the numpy array
print(np_array.shape) # Print the shape of the numpy array
print(np_array.dtype) # Print the data type of the numpy array
print(np_array.ndim) # Print the number of dimensions of the numpy array
print(np_array[0]) # Print the first element of the numpy array
np_array[0] = 10 # Change the first element of the numpy array to 10
print(np_array) # Print the modified numpy array

np_array_2d = np.array([[1, 2, 3], [4, 5, 6]]) # Create a 2D numpy array
print(np_array_2d) # Print the 2D numpy array
print(np_array_2d.shape) # Print the shape of the 2D numpy array
print(np_array_2d.dtype) # Print the data type of the 2D numpy array
print(np_array_2d.ndim) # Print the number of dimensions of the 2D numpy array
print(np_array_2d[0, 1]) # Print the element at row 0, column 1 of the 2D numpy array
np_array_2d[0, 1] = 10 # Change the element at row 0, column 1 of the 2D numpy array to 10
print(np_array_2d) # Print the modified 2D numpy array

np_array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) # Create a 3D numpy array
print(np_array_3d) # Print the 3D numpy array
print(np_array_3d.shape) # Print the shape of the 3D numpy array
print(np_array_3d.dtype) # Print the data type of the 3D numpy array
print(np_array_3d.ndim) # Print the number of dimensions of the 3D numpy array
print(np_array_3d[0, 1, 0]) # Print the element at index [0, 1, 0] of the 3D numpy array
np_array_3d[0, 1, 0] = 10 # Change the element at index [0, 1, 0] of the 3D numpy array to 10
print(np_array_3d) # Print the modified 3D numpy array

np_array_zero = np.zeros((2)) # Create a 1D numpy array filled with zeros
print(np_array_zero) # Print the 1D numpy array filled with zeros

np_array_ones = np.ones((2)) # Create a 1D numpy array filled with ones
print(np_array_ones) # Print the 1D numpy array filled with ones

np_array_arange = np.arange(1, 10, 2) # Create a numpy array with values from 1 to 10 with a step of 2
print(np_array_arange) # Print the numpy array with values from 1 to 10 with a step of 2

np_array_linspace = np.linspace(1, 10, 5) # Create a numpy array with 5 values evenly spaced between 1 and 10
print(np_array_linspace) # Print the numpy array with 5 values evenly spaced between 1 and 10

np_array_random = np.random.rand(2, 3) # Create a 2D numpy array with random values between 0 and 1
print(np_array_random) # Print the 2D numpy array with random values between 0 and 1

np_array_random_int = np.random.randint(1, 10, (2, 3)) # Create a 2D numpy array with random integers between 1 and 10
print(np_array_random_int) # Print the 2D numpy array with random integers between 1 and 10

np_array_random_randn = np.random.randn(2, 3) # Create a 2D numpy array with random values from the standard normal distribution
print(np_array_random_randn) # Print the 2D numpy array with random values from the standard normal distribution

np_array_random_choice = np.random.choice([1, 2, 3, 4, 5], size=(2, 3)) # Create a 2D numpy array with random choices from the list
print(np_array_random_choice) # Print the 2D numpy array with random choices from the list

#reshape
np_array_reshaped = np_array.reshape((5, 1)) # Reshape the numpy array to a 2D array with 5 rows and 1 column
print(np_array_reshaped) # Print the reshaped numpy array

#operations
np_array_sum = np_array + np_array_reshaped # Add the numpy array and the reshaped numpy array  # Element-wise addition
print(np_array_sum) # Print the result of the addition
#+ - * / % ** //
print(np_array.sum) # Print the result of the addition
print(np_array.sum()) # Print the sum of the numpy array

print(np_array.mean()) # Print the mean of the numpy array
print(np_array.std()) # Print the standard deviation of the numpy array
print(np_array.var()) # Print the variance of the numpy array
print(np_array.min()) # Print the minimum value of the numpy array
print(np_array.max()) # Print the maximum value of the numpy array
print(np_array.argmin()) # Print the index of the minimum value of the numpy array
print(np_array.argmax()) # Print the index of the maximum value of the numpy array
print(np.dot(np_array,np_array)) # Print the dot product of the numpy array with itself
print(np.transpose(np_array)) # Print the transpose of the numpy array

print(np.unique(np_array)) # Print the unique values in the numpy array
print(np.sort(np_array)) # Print the sorted numpy array
print(np.concatenate((np_array, np_array))) # Print the concatenated numpy array