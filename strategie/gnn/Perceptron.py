import numpy as np
import math

class Perceptron :

    def __init__ (self,
            weigth, # A numpy array of weigth
            activation_function=math.tanh # The non-linear ending function
    ) :
        self.w = weigth
        self.f = activation_function

    def process (self,
            input # A numpy array of data
    ) :
        x = np.concatenate (([1.], input)) # adding a bias
        y = np.dot (x, self.w)
        return self.f (y)

    def get_weight (self) :
        return self.w
