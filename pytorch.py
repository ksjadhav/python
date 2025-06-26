import torch

import torch.nn as nn
import torch.optim as optim

# Simple linear regression example
# y = 2x + 1

# Training data
x_train = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y_train = torch.tensor([[3.0], [5.0], [7.0], [9.0]])

# Define a simple linear model
model = nn.Linear(1, 1)

# Loss and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training loop
for epoch in range(1000):
    # Forward pass
    outputs = model(x_train)
    loss = criterion(outputs, y_train)

    # Backward and optimize
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch+1) % 200 == 0:
        print(f'Epoch [{epoch+1}/1000], Loss: {loss.item():.4f}')

# Test the model
with torch.no_grad():
    test_input = torch.tensor([[5.0]])
    predicted = model(test_input)
    print(f'Prediction for input 5.0: {predicted.item():.4f}')