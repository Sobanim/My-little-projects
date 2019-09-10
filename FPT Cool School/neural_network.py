import numpy as np
import paho.mqtt.client as mqtt



class NeuralNetwork():

    def __init__(self):
        # seeding for random number generation
        np.random.seed(1)

        # converting weights to a 3 by 1 matrix with values from -1 to 1 and mean of 0
        self.synaptic_weights = 2 * np.random.random((4, 1)) - 1

    def sigmoid(self, x):
        # applying the sigmoid function
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        # computing derivative to the Sigmoid function
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        # training the model to make accurate predictions while adjusting weights continually
        for iteration in range(training_iterations):
            # siphon the training data via  the neuron
            output = self.think(training_inputs)

            # computing error rate for back-propagation
            error = training_outputs - output

            # performing weight adjustments
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))

            self.synaptic_weights += adjustments

    def think(self, inputs):
        # passing the inputs via the neuron to get output
        # converting values to floats

        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output


if __name__ == "__main__":
    # initializing the neuron class
    neural_network = NeuralNetwork()

    print("Beginning Randomly Generated Weights: ")
    print(neural_network.synaptic_weights)

    # training data consisting of 4 examples--3 input values and 1 output
    training_inputs = np.array([[0, 0, 1, 0],
                                [0, 1, 0, 0],
                                [1, 0, 0, 0],
                                [0, 0, 0, 1],
                                [4, 2, 0, 0],
                                [1, 2, 3, 0],
                                [3, 2, 1, 0],
                                [2, 0, 4, 0],
                                [1, 0, 1, 4],
                                [0, 2, 4, 0],
                                [0, 0, 0, 0],
                                [1, 1, 1, 3],
                                [2, 1, 1, 2],
                                [3, 0, 3, 0],
                                [0, 0, 3, 3],
                                [1, 1, 2, 2],
                                [2, 0, 3, 0],
                                [0, 0, 5, 1],
                                [1, 1, 3, 1],
                                [1, 4, 1, 0],
                                [0, 0, 0, 0],
                                [1, 1, 4, 0],
                                [0, 1, 4, 1],
                                [1, 2, 1, 2],
                                [2, 4, 0, 0],
                                [0, 3, 0, 3],
                                [2, 3, 0, 1],
                                [0, 2, 3, 1],
                                [3, 3, 0, 0],
                                [1, 1, 1, 3]])

    training_outputs = np.array([[0.6, 0.3, 0, 1, 0, 0.6, 0, 0.6, 1, 0.6, 0, 1, 0, 0, 0.6, 0.6, 0.6, 0.6, 0.6, 0.3, 0, 0.6, 0.6, 0.3, 0.3, 0.3, 0.3, 0.6, 0, 1]]).T

    # training taking place
    neural_network.train(training_inputs, training_outputs, 2000000)

    print("Ending Weights After Training: ")
    print(neural_network.synaptic_weights)
    while(1):
        user_input_one = str(input("User Input One: "))
        user_input_two = str(input("User Input Two: "))
        user_input_three = str(input("User Input Three: "))
        user_input_fourth = str(input("User Input Fourth: "))
        print("Considering New Situation: ", user_input_one, user_input_two, user_input_three, user_input_fourth)
        print("New Output data: ")
        result = neural_network.think(np.array([user_input_one, user_input_two, user_input_three, user_input_fourth]))
        print(result)
        print("Wow, we did it!")

        broker_address = "192.168.100.151"

        client = mqtt.Client("dmytro_broker")  # name of broker
        client.connect(broker_address)  # ip adress broker

        if 0 <= result <= 0.24:
            result = 0
            client.publish("semaphore", "[1, 0, 0, 0]")  # send to semaphore
        elif 0.25 <= result <= 0.46:
            result = 0.3
            client.publish("semaphore", "[0, 1, 0, 0]")  # send to semaphore
        elif 0.47 <= result <= 0.72:
            result = 0.6
            client.publish("semaphore", "[0, 0, 1, 0]")  # send to semaphore
        elif 0.73 <= result <= 1:
            result = 1
            client.publish("semaphore", "[0, 0, 0, 1]")  # send to semaphore
        else:
            result = "Error, bad result neural network"
        print(result)
