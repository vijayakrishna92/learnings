#pytorch
# It is a powerful library that provides a flexible and efficient way to work with tensors and perform computations on GPUs.
# It is widely used in the field of computer vision, natural language processing, and other areas of artificial intelligence.
# It is known for its dynamic computation graph, which allows for easy debugging and experimentation.
# It is also used for building and training deep learning models, and it provides a wide range of pre-trained models and tools for transfer learning.

# fundamentals of pytorch
# tensor creation
import torch

t = torch.tensor([[1, 2], [3, 4]])
print(t)
print(t.shape)  # shape of the tensor
print(t.dtype)  # data type of the tensor
print(t.device)  # device of the tensor (CPU or GPU)
print(t[0,0]) # access the first element of the tensor
# we can even apply slicing to access the elements of the tensor
print(t[0, :])  # access the first row of the tensor

mask = t > 2  # create a mask for values greater than 2
print(mask)  # print the mask
print(t[mask])  # print the values greater than 2 using the mask

print(t.view(4))  # view the tensor as a 1D tensor reshaping it

t = torch.arange(0,10)
print(t.view(2,5))  # view the tensor as a 2D tensor reshaping it

t_transpose = t.mT  # transpose the tensor
print(t_transpose)  # print the transposed tensor

zeroes = torch.zeros((2, 3))  # create a tensor of zeros
print(zeroes)
ones = torch.ones((2, 3))  # create a tensor of ones
print(ones)
random = torch.rand((2, 3))  # create a tensor of random values
print(random)
randn = torch.randn((2, 3))  # create a tensor of random values from a normal distribution
print(randn)

eye = torch.eye(3)  # create a tensor of identity matrix
print(eye)

ar = torch.arange(0, 10, 2)  # create a tensor of arange values with step size 2
# arange is similar to numpy's arange function
print(ar)
lin = torch.linspace(0, 1, 5)  # create a tensor of linspace values with 5 values between 0 and 1
# linspace is similar to numpy's linspace function
print(lin)

# arithmetic operations
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])
print(a+b)  # tensor addition
print(a-b)  # tensor subtraction
print(a*b)  # tensor multiplication
print(a/b)  # tensor division
print(a@b)  # tensor matrix multiplication
print(a.matmul(b))  # tensor matrix multiplication using matmul function
print(torch.matmul(a, b))  # tensor matrix multiplication using matmul function
print(a.T)  # tensor transpose
print(a.sum())  # tensor sum

a = torch.tensor([[1., 2.], [3., 4.]])
print(a.mean())  # tensor mean
print(a.std())  # tensor standard deviation
print(a.var())  # tensor variance