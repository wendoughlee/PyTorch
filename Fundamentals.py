import torch

#       TOPICS:
#   Intro to tensors
#   Creating tensors
#   Getting information from tensors
#   Manipulating tensors
#   Dealing with tensor shapes
#   Indexing on tensors
#   Mixing PyTorch tensors and NumPy
#   Reproductibility
#   Running tensors on GPU
#

# Tensors represent data in a numerical way
# Tensor syntax: [color_channels, height, width] , 3-dimensional
# example: Tensor [3, 224, 224] -> 3 color channels (R,G,B) height of 224px and width 224px

# Scalar: single number , 0 dimension tensor , usually lowercase
scalar = torch.tensor(7)
#print(scalar)

# Get the Python number from scalar (a tensor), only works with one-element tensors
scalar.item()
#print(scalar.item())

# Vector: a flexible single dimension tensor, can contain lots of numbers , usually lowercase
vector = torch.tensor([7,7])
#print(vector)

# Check number of dimensions of vector
vector.ndim
#print(vector.ndim)

# TIP: You can tell the number of dimensions of a tensor 
# by counting square brackets on the outside

# Shape: Number of elements along each dimension of the tensor
vector.shape
#print(vector.shape)

# Matrices: as flexible as sensors, they have an extra dimension , usually uppercase
MATRIX = torch.tensor([[7, 8],
                      [9, 10]])
#print(MATRIX)
#print(MATRIX.ndim)

# Tensor: can represent almost anything, 3D , usually uppercase
TENSOR = torch.tensor([[[1, 2, 3,],
                        [3, 6, 9],
                        [2, 4, 5]]])
TENSOR
print(TENSOR)
TENSOR.shape