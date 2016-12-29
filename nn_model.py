from keras.layers import Dense, Merge, Activation
from keras.models import Sequential

class NNModel:
    def __init__(self):
        ONE_HOT_FULL_SIZE = 57
        ONE_HOT_HAND_SIZE = 28

        modelRNN = Sequential()
        modelRNN.add(LSTM(32, input_dim=ONE_HOT_FULL_SIZE))

        modelHand = Sequential()
        modelHand.add(Dense(ONE_HOT_HAND_SIZE, input_dim=ONE_HOT_HAND_SIZE))
        modelHand.add(Activation('relu'))

        self.model = Sequential()
        model = self.model
        model.add(Merge([modelRNN, modelHand], mode='concat'))
        model.add(Dense(32))
        model.add(Activation('relu'))
        model.add(Dense(1))
        model.add(Activation('linear'))

        model.compile(loss='mean_squared_error', optimizer='rmsprop')
