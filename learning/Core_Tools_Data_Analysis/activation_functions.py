#activation functions
# they are used to introduce non-linearity in the model, allowing it to learn complex patterns in the data.

import torch
import torch.nn as nn

class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__() 
        self.conv = nn.Conv2d(1, 16, kernel_size=3, padding=1) 

        # 2. ReLU Activation: Apply non-linearity
        #activation functions
        self.relu = nn.ReLU() #  image classification, object detection. Simple, avoids vanishing gradient (for positive values) Use for hidden layers in CNNs, MLPs
        self.relu = nn.Sigmoid() #  # image classification, binary classification. Outputs between 0 and 1. Use for binary classification tasks
        self.relu = nn.Tanh() #  image classification, regression. Outputs between -1 and 1. Use for hidden layers in RNNs, MLPs
        self.relu = nn.Softmax(dim=1) #  image classification, multi-class classification. Outputs probabilities for each class. Use for multi-class classification tasks


        self.flatten = nn.Flatten()
        self.fc = nn.Linear(16 * 32 * 32, 2)  

    def forward(self, x):
        x = self.conv(x)       
        x = self.relu(x)       
        x = self.flatten(x)    
        x = self.fc(x)         
        return x
    
# Example usage
if __name__ == "__main__":
    model = SimpleNN()  # Create an instance of the model
    print(model)        # Print the model architecture
    
    # Example input: batch of 4 grayscale images of size 32x32
    input_data = torch.randn(4, 1, 32, 32)  # if 1000 images then 1000/4 times + remaining images at last will be the input(number of times it runs)
    output_data = model(input_data)  # Forward pass
    print(output_data.shape)  # Output shape should be (4, 2) for batch size of 4 and 2 classes