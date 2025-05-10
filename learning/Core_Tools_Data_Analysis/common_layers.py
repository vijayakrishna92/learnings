''' nn.Conv2d(1, 16, kernel_size=3, padding=1) 
    self.relu = nn.ReLU()
    self.flatten = nn.Flatten()
    self.fc = nn.Linear(16 * 32 * 32, 2) '''

import torch
import torch.nn as nn

class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        # 1. Conv2d Layer: Extract features from image
        self.conv = nn.Conv2d(1, 16, kernel_size=3, padding=1)  # 1 input channel (grayscale), 16 output channels, 3x3 kernel padding=1 for edges of image (3%2)
        # This layer will output 16 feature maps of size 32x32 (assuming input image is 32x32)
        # will have 16 images of size 32x32
        
        # 2. ReLU Activation: Apply non-linearity
        self.relu = nn.ReLU()
        
        # 3. Flatten Layer: Flatten the 2D output to 1D for fully connected layer
        self.flatten = nn.Flatten()
        
        # 4. Linear Layer: Final output (e.g., classification into 2 classes)
        self.fc = nn.Linear(16 * 32 * 32, 2)  # Flattened size from 32x32 image with 16 feature maps, output 2 classes

    def forward(self, x):
        x = self.conv(x)       # Apply convolution
        x = self.relu(x)       # Apply ReLU activation
        x = self.flatten(x)    # Flatten the 3D output to 1D
        x = self.fc(x)         # Apply fully connected layer for classification
        return x
    
# Example usage
if __name__ == "__main__":
    model = SimpleNN()  # Create an instance of the model
    print(model)        # Print the model architecture
    
    # Example input: batch of 4 grayscale images of size 32x32
    input_data = torch.randn(4, 1, 32, 32)  
    output_data = model(input_data)  # Forward pass
    print(output_data.shape)  # Output shape should be (4, 2) for batch size of 4 and 2 classes