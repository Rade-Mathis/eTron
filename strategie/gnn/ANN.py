import numpy as np

class ANN :

    def __init__ (self,
            neurones # An array of arrays of Perceptrons. Each subarray being a
                     # layer.
    ) :
        self._nb_layers = len (neurones)
        self._layer_size = np.empty (self._nb_layers).astype (int)
        self._neurones   = [None] * self._nb_layers
        for i in range (self._nb_layers) :
            self._layer_size[i] = len (neurones[i])
            self._neurones[i] = [None] * self._layer_size[i]
            for j in range (self._layer_size[i]) :
                self._neurones[i][j] = neurones[i][j]
