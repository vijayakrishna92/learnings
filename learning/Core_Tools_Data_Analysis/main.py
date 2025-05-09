#opencv, rastero, Image, pytorch, tensorflow/keras

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

ar = torch.arange(0, 10, 2)  # create a tensor of arange values
print(ar)
lin = torch.linspace(0, 1, 5)  # create a tensor of linspace values
print(lin)
