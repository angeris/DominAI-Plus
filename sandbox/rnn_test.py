from keras.models import Sequential
from keras.layers import Activation, Dense, LSTM, Merge
import numpy as np

model = Sequential()
model.add(LSTM(32, input_dim=64))
model.add(Dense(1))
model.add(Activation('linear'))

model_new = Sequential()
model_new.add(Dense(10, input_dim=10))
model_new.add(Activation('relu'))

model_combined = Sequential()
model_combined.add(Merge([model, model_new], mode='concat'))
model_combined.add(Dense(1))
model_combined.add(Activation('linear'))

model_combined.compile(optimizer='rmsprop', loss='mean_squared_error')

data = np.random.random((1000, 10, 64))
data_new = np.random.random((1000,10))
output = np.random.random((1000))

model_combined.fit([data, data_new], output)

print 'predicted'
print model_combined.predict(data[0:3,:,:])
