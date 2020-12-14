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
        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
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
path = u'c:\\Users\\-\\Desktop\\trainset'
dataset = os.listdir(path)
input_nodes = len(dataset)
hidden_nodes = 2000
output_nodes = 10000
learning_rate = 0.3
nt = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
#TTTTRRRRAAAAIIIIINNNNN
trainig_data_file = open('c:\\Users\\-\\Desktop\\train.csv', 'r')
data_train = trainig_data_file.readlines()
trainig_data_file.close()
for record in data_train:
    all_values = record.split(',')
    targets = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    inputs = numpy.zeros(input_nodes) + 0.01
    inputs[int(float(all_values[0]))] = 0.99
    nt.train(inputs, targets)
#TTTTEEEEESSSSSSTTTTT
test_data_file = open('c:\\Users\\-\\Desktop\\test.csv', 'r')
data_test = test_data_file.readlines()
test_data_file.close()
scorepad = []
for record in data_test:
    all_values = record.split(',')
    correct_label = int(float(all_values[0]))
    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    outputs = nt.query(inputs)
    label = numpy.argmax(outputs)
    if(label == correct_label):
        scorepad.append(1)
    else:
        scorepad.append(0)
scorepad_array = numpy.asarray(scorepad)
print("эффектиность = ", scorepad_array.sum() / scorepad_array.size, "%")
print(scorepad)
