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

# Scalar: single number , 0 dimension tensor

scalar = torch.tensor(7)
print(scalar)