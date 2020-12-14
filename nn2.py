import os, sys
import numpy
import scipy.special
import matplotlib.pyplot
import random
from PIL import Image
class NeuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.lr = learningrate
        self.wih = (numpy.random.rand(self.hnodes, self.inodes) -0.5)
        self.who = (numpy.random.rand(self.onodes, self.hnodes) -0.5)
        self.activation_function = lambda x: scipy.special.logit(x)
    def train(self, inputs_list, targets_list):
        inputs = numpy.array(inputs_list, ndmin = 2).T
        targets = numpy.array(targets_list, ndmin = 2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        outputs_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.who.T, outputs_errors)
        self.who += self.lr * numpy.dot((outputs_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
    def query(self, inputs_list):
        inputs = numpy.array(inputs_list, ndmin = 1).T
        hidden_inputs = numpy.dot(inputs, self.who)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(hidden_outputs, self.wih)
        final_outputs = self.activation_function(final_inputs)
        return final_outputs
def train_fruits(train_list, amount):
    input_nodes = 2
    hidden_nodes = 2000
    output_nodes = 10000
    learning_rate = 0.3
    nt = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
    neurals = [0] * amount
    for e in range(amount):
        neurals[e] = nt
    a = 0
    print("length = ", len(train_list))
    for record in train_list:
        all_values = record.split(',')
        targets = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        inputs = numpy.zeros(input_nodes) + 0.01
        for e in range(amount):
            if(int(float(all_values[0])) == e):
                inputs[0] = 0.99
            else:
                inputs[1] = 0.99
            neurals[e].train(inputs, targets)
            inputs = [0.01, 0.01]
            
        a += 1
    return neurals
def query_fruits(neurals, test_list):
    a = 0
    scorepad = []
    signalpad = []
    for record in test_list:
        all_values = record.split(',')
        inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        for neural_network in neurals:
            outputs = neural_network.query(inputs)
            signalpad.append(outputs[0])
        label = numpy.argmax(signalpad)
        correct_label = int(float(all_values[0]))
        if (label == correct_label):
            scorepad.append(1)
        else:
            scorepad.append(0)
        signalpad = []
        a += 1
    return scorepad
path = u'c:\\Users\\-\\Desktop\\trainset'
dataset = os.listdir(path)
#TTTTRRRRAAAAIIIIINNNNN
trainig_data_file = open('c:\\Users\\-\\Desktop\\train.csv', 'r')
data_train = trainig_data_file.readlines()
trainig_data_file.close()
neural_list = train_fruits(data_train, len(dataset))

print("TRAINED!")
#TTTTEEEEESSSSSSTTTTT
test_data_file = open('c:\\Users\\-\\Desktop\\test.csv', 'r')
data_test = test_data_file.readlines()
test_data_file.close()
scorepadd = query_fruits(neural_list, data_test)
scorepad_array = numpy.asarray(scorepadd)
print( "эффективность = ", scorepad_array.sum()  / scorepad_array.size * 100, "%")
print(scorepadd)
'''
for e in range(len(neural_list)):
    numpy.savetxt('wih' + str(e) + '.csv', neural_list[e].wih, delimiter=", ", fmt = '%.1f')
    numpy.savetxt('who' + str(e) + '.csv', neural_list[e].who, delimiter=", ", fmt = '%.1f')
    '''

'''
for record in data_test:
    all_values = record.split(',')
    if(int(float(all_values[0])) == fruit):
        correct_label = 0
    else:
        correct_label = 1
    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    outputs = neural.query(inputs)
    label = numpy.argmax(outputs)
    if (label == correct_label):
        scorepad.append(1)
    else:
        scorepad.append(0)
scorepad_array = numpy.asarray(scorepad)
print( "эффективность = ", scorepad_array.sum()  / scorepad_array.size * 100, "%")
print(scorepad)
numpy.savetxt('wih.csv', neural.wih, delimiter=", ", fmt = '%.1f')
numpy.savetxt('who.csv', neural.who, delimiter=", ", fmt = '%.1f')
'''
