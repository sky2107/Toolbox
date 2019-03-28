import keras
from keras import backend as K 
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy

new_model = keras.models.load_model('first_model.h5')
print(new_model.summary())