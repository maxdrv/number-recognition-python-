from scipy.io import loadmat
import numpy as np


def download():

    input_data = loadmat('C:/Users/user/Documents/PythonNotes/LABPY2/test_set.mat')
    data_labels = np.array(input_data['y'])
    network_input = np.array(input_data['x'])

    network_weights = loadmat('C:/Users/user/Documents/PythonNotes/LABPY2/weights.mat')
    weights_layer_1 = network_weights['Theta1']
    weights_layer_2 = network_weights['Theta2']

