import random
import numpy as np

training_inputs = []
training_outputs = []
for i in range(10000):
    xxx = [random.randint(0, 6), random.randint(0, 6), random.randint(0, 6), random.randint(0, 6)]

    training_inputs.append(xxx)
    #print(training_list)

    maximalne = xxx.index(max(xxx)) + 1
    training_outputs.append(maximalne)
training_outputs = np.array(training_outputs).T
print(training_inputs)
print("Output list", training_outputs)
