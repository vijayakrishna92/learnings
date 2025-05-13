#pytorch
# It is a powerful library that provides a flexible and efficient way to work with tensors and perform computations on GPUs.
# It is widely used in the field of computer vision, natural language processing, and other areas of artificial intelligence.
# It is known for its dynamic computation graph, which allows for easy debugging and experimentation.
# It is also used for building and training deep learning models, and it provides a wide range of pre-trained models and tools for transfer learning.

# fundamentals of pytorch
# tensor creation
import torch
import random
import numpy as np

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
print(a.min())  # tensor minimum value
print(a.max())  # tensor maximum value
print(a.argmin())  # tensor index of minimum value
print(a.argmax())  # tensor index of maximum value
print(a.nonzero())  # tensor nonzero values
print(a==b)  # tensor equality
print(a!=b)  # tensor inequality
print(a>0)  # tensor greater than
print(a<0)  # tensor less than
print(a>=0)  # tensor greater than or equal to
print(a<=0)  # tensor less than or equal to
c = a.clone
print(c)  # clone the tensor

# Autograd and Computational Graph
# Autograd is a powerful feature of PyTorch that allows for automatic differentiation of tensors.
# It is used for computing gradients of tensors with respect to some scalar value (usually the loss function in a neural network).
x = torch.tensor([[1., 2.,3., 4.]],requires_grad=True) # create a tensor with gradient tracking enabled
# this is useful for training neural networks and computing gradients
# for backpropagation
print(x.requires_grad) # print the tensor
y= x+2 # compute the square of the tensor
z = y.sum() # compute the sum of the tensor
z.backward()
# compute the gradients of y with respect to x
print(x.grad) # print the gradients of y with respect to x

# Using CUDA and Moving Tensors to GPU
# CUDA is a parallel computing platform and application programming interface (API) model created by NVIDIA.
# It allows developers to use a CUDA-enabled graphics processing unit (GPU) for general purpose processing – an approach known as GPGPU (General-Purpose computing on Graphics Processing Units).   
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")  # Check if GPU is available and set the device accordingly
x = torch.tensor([1.0, 2.0, 3.0], device=device)  # Create a tensor on the selected device
print(x)  # Print the tensor
print(x.device)  # Print the device of the tensor
# Model on GPU
#model = MyModel().to(device)

# Setting Random Seeds for Reproducibility
# Setting random seeds is important for reproducibility in experiments.
# It ensures that the random numbers generated are the same every time the code is run.
# This is especially important in deep learning, where random initialization of weights can lead to different results.
# Setting the seed for PyTorch
def set_seed(seed):
    """Set the seed for random number generation for reproducibility."""
    torch.manual_seed(seed)  # Set the seed for PyTorch
    np.random.seed(seed)  # Set the seed for NumPy
    random.seed(seed)  # Set the seed for Python's random module
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)  # Set the seed for all GPUs
    torch.backends.cudnn.deterministic = True  # Ensure deterministic behavior
    torch.backends.cudnn.benchmark = False  # Disable the benchmark for reproducibility
    torch.backends.cudnn.enabled = False  # Disable cuDNN for reproducibility

seed = 42
