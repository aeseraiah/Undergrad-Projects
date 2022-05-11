import numpy as np

#Common activation function that changes the values of the input layer to 0-1. 
def sigmoid(x):
    return 1.0/(1+ np.exp(-x))

#
def sigmoid_derivative(x):
    return x * (1.0 - x)


class NeuralNetwork:
    def __init__(self, x, y, nhl): #nhl = number of neurons in hidden layer
        self.input      = x #input layer 
        self.weights1   = np.random.rand(self.input.shape[1],nhl) #weights between input layer and hidden layer 
        self.weights2   = np.random.rand(nhl,1) #weights between hidden layer and output layer                  
        self.y          = y 
        self.output     = np.zeros(self.y.shape) #output layer

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1)) # --> Zh
        self.output = sigmoid(np.dot(self.layer1, self.weights2)) # --> Zo

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2


if __name__ == "__main__":
    X = np.array([[0,0,1],
                  [0,1,1],
                  [1,0,1],
                  [1,1,1]])
    y = np.array([[0],[1],[1],[0]])
    nhl = 7 #doesn't have to be pre-defined; could let user decide this upon calling class
    nn = NeuralNetwork(X,y,nhl) #Instantiating the class AND calling the class instance 

    for i in range(1500):
        nn.feedforward()
        nn.backprop()

    print(nn.output)