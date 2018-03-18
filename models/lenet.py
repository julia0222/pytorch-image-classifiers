import torch.nn as nn
import torch.nn.functional as F  # torch functions


class LeNet(nn.Module):
    def __init__(self):
        super(LeNet, self).__init__()
        
        # convolutional layers
        # 1 image, 6 output channels, 5*5 convolution
        self.conv1 = nn.Conv2d(1, 6, kernel_size=(5, 5), stride=(1, 1))
        self.conv2 = nn.Conv2d(6, 16, kernel_size=(5, 5), stride=(1, 1))

        # hidden layers
        # self.fc1 = nn.Linear(16 * 5 * 5, 120)  # layer 1 activation
        self.fc1 = nn.Linear(4, 120)  # layer 1 activation
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        """
        forward must be overwritten in torch model class
        """
        # conv layers
        print(1, x.shape)
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))  # add pooling layer
        print(2, x.shape)
        x = F.max_pool2d(F.relu(self.conv2(x)), (2, 2))
        print(3, x.shape)
        x = x.view(-1, self.num_flat_features(x))  # view manipulates shape
        print(4, x.shape)

        # fully connected layers
        x = F.relu(self.fc1(x))
        print(5, x.shape)
        x = F.relu(self.fc2(x))
        print(6, x.shape)
        x = self.fc3(x)
        print(7, x.shape)

        return x

    def num_flat_features(self, x):
        size = x.size()[1:]
        num_features = 1
        for s in size:
            num_features *= s

        return num_features


if __name__ == "__main__":
    net = LeNet()
    print(net)

    params = list(net.parameters())
    print(len(params))
