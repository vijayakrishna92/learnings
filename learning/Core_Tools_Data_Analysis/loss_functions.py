# loss functions
'''
🟢 Classification:
Cross-Entropy Loss → Multi-class classification
Binary Cross-Entropy Loss → Binary classification
Focal Loss → Classification with class imbalance (e.g., object detection)

🔵 Regression:
Mean Squared Error (MSE) Loss → Standard regression
Mean Absolute Error (MAE) Loss → Regression, robust to outliers
Huber Loss → Combines MSE + MAE; good when outliers exist

🟡 Embedding / Similarity Learning (e.g., face recognition):
Triplet Loss / Triplet Margin Loss → For separating similar/dissimilar samples
Contrastive Loss → Siamese networks, similarity learning
Cosine Embedding Loss → Measures similarity between vectors

🟣 Image Segmentation:
Dice Loss / Soft Dice Loss → Medical and semantic segmentation
Jaccard Loss / Lovasz Loss → Overlap-based loss for segmentation

❗️Specialized / Less Common:
Poisson NLL Loss / Poisson Loss → Count-based data
KL Divergence Loss → Probabilistic models, VAEs
Negative Log Likelihood Loss → Generative models
Smooth L1 Loss → Object detection (e.g., in Faster R-CNN)
Hinge Loss → Mostly for SVMs (not common in deep learning now)'''

# they are used to measure how well the model is performing. The loss function quantifies the difference between the predicted output and the actual target.
# 1. Mean Squared Error (MSE) Loss: Used for regression tasks
# 2. Cross-Entropy Loss: Used for multi-class classification tasks
# 3. Binary Cross-Entropy Loss: Used for binary classification tasks
# 4. Hinge Loss: Used for "maximum-margin" classification, primarily with Support Vector Machines (SVMs)
# 5. Kullback-Leibler Divergence Loss: Used for measuring how one probability distribution diverges from a second expected probability distribution
# 6. Contrastive Loss: Used for learning embeddings, especially in Siamese networks
# 7. Triplet Loss: Used for learning embeddings, especially in tasks like face recognition
# 8. Focal Loss: Used for addressing class imbalance in tasks like object detection
# 9. Smooth L1 Loss: Combines the properties of L1 and L2 loss, used in object detection tasks
# 10. Poisson Loss: Used for modeling count data, especially in tasks like image denoising
# 11. Cosine Embedding Loss: Used for measuring the similarity between two samples
# 12. Contrastive Divergence Loss: Used in training Restricted Boltzmann Machines (RBMs)
# 13. Dice Loss: Used for image segmentation tasks, especially in medical imaging
# 14. Jaccard Loss: Used for image segmentation tasks, especially in semantic segmentation
# 15. Huber Loss: Used for regression tasks, less sensitive to outliers than MSE
# 16. Soft Dice Loss: A differentiable version of the Dice loss, used for image segmentation tasks
# 17. Lovasz Loss: Used for image segmentation tasks, especially in semantic segmentation
# 18. Triplet Margin Loss: Used for learning embeddings, especially in tasks like face recognition
# 19. Contrastive Loss: Used for learning embeddings, especially in Siamese networks
# 20. KL Divergence Loss: Used for measuring how one probability distribution diverges from a second expected probability distribution
# 21. Poisson NLL Loss: Used for modeling count data, especially in tasks like image denoising
# 22. Negative Log Likelihood Loss: Used for probabilistic models, especially in generative models
# 23. Softmax Loss: Used for multi-class classification tasks, outputs probabilities for each class
# 24. Sparse Categorical Cross-Entropy Loss: Used for multi-class classification tasks with sparse labels
# 25. Categorical Cross-Entropy Loss: Used for multi-class classification tasks with dense labels
# 26. Mean Absolute Error (MAE) Loss: Used for regression tasks, less sensitive to outliers than MSE
# 27. Mean Squared Logarithmic Error (MSLE) Loss: Used for regression tasks, especially when the target variable has a wide range
# 28. Quantile Loss: Used for quantile regression tasks
# 29. Hinge Embedding Loss: Used for learning embeddings, especially in tasks like face recognition
# 30. Contrastive Loss: Used for learning embeddings, especially in Siamese networks

import torch
import torch.nn as nn

class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__() 
        self.conv = nn.Conv2d(1, 16, kernel_size=3, padding=1) 
        self.relu = nn.ReLU()  
        self.flatten = nn.Flatten()
        self.fc = nn.Linear(16 * 32 * 32, 2)  

    def forward(self, x):
        x = self.conv(x)       
        x = self.relu(x)       
        x = self.flatten(x)    
        x = self.fc(x)         
        return x

model = SimpleNN()
output = model(torch.randn(4, 1, 32, 32))
print(output.shape)  # Output shape should be (4, 2) for batch size of 4 and 2 classes
# loss functions
# 1. Mean Squared Error (MSE) Loss
mse_loss = nn.MSELoss()
# Example usage
targets = torch.tensor([[0.6, 0.1],
                        [0.2, 0.3],
                        [0.9, 0.5],
                        [0.4, 0.7]]) 
loss = mse_loss(output, targets)
print("MSE Loss:", loss.item())
# 2. Cross-Entropy Loss
cross_entropy_loss = nn.CrossEntropyLoss()
# Example usage 
targets = torch.tensor([1, 0, 1, 0])  # Example target labels
loss = cross_entropy_loss(output, targets)
print("Cross-Entropy Loss:", loss.item())
# 3. Binary Cross-Entropy Loss
binary_cross_entropy_loss = nn.BCELoss()
# Example usage
targets = torch.tensor([[0.0, 1.0], [1.0, 0.0], [0.5, 0.5], [1.0, 1.0]])
# Example target labels
# Note: For BCELoss, the output should be in the range [0, 1]
output = torch.sigmoid(output)  # Apply sigmoid activation
loss = binary_cross_entropy_loss(output, targets)
print("Binary Cross-Entropy Loss:", loss.item())
# 4. Dice Loss
class DiceLoss(nn.Module):
    def __init__(self, smooth=1e-6):
        super(DiceLoss, self).__init__()
        self.smooth = smooth

    def forward(self, inputs, targets):
        intersection = (inputs * targets).sum()
        dice = (2.0 * intersection + self.smooth) / (inputs.sum() + targets.sum() + self.smooth)
        return 1 - dice # Return 1 - Dice coefficient to get the loss
# Example usage
dice_loss = DiceLoss()
# Example target labels (binary segmentation)
targets = torch.tensor([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.0, 0.0]])
# Example target labels
# Note: For Dice Loss, the output should be in the range [0, 1]
output = torch.sigmoid(output)  # Apply sigmoid activation
loss = dice_loss(output, targets)
print("Dice Loss:", loss.item())