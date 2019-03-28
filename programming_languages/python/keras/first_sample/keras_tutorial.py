import keras
from keras import backend as K 
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy

model = Sequential([
    Dense(16, input_shape=(1,), activation='relu'),
    Dense(32, activation='relu'),
    Dense(2, activation='softmax')
])


# print(model.summary())
model.compile(Adam(lr=.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])


import creating_samples_and_layers as item

# valid_set = item.scale_valid_set

model.fit(item.scale_train_samples, item.train_labels, batch_size=10, epochs=20, shuffle=True, verbose=0)
# validation_split=.1, # validation_data, validation_split

prediction = model.predict(item.scale_valid_samples, batch_size=10, verbose=0)

# for ele in prediction:
#     print(ele)

# print(item.scale_valid_samples)

rounded_prediction = model.predict_classes(item.scale_valid_samples, batch_size=10, verbose=0)
# for ele in rounded_prediction:
#     print(ele)

model.save('first_model.h5')

