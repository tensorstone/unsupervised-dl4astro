import lasagne
from lasagne.layers import (
    InputLayer, MaxPool2DLayer, Conv2DLayer, DenseLayer, DropoutLayer,
    batch_norm
)
from lasagne.nonlinearities import leaky_rectify, softmax
from lasagne.init import HeNormal


def build_cnn(input_var, num_outputs, size, num_channels=3):

    network = InputLayer(shape=(None, num_channels, size, size), input_var=input_var)

    network = batch_norm(Conv2DLayer(
        network,
        num_filters=32, filter_size=(3, 3), pad="same",
        nonlinearity=leaky_rectify, W=HeNormal()
    ))

    network = batch_norm(Conv2DLayer(
        network,
        num_filters=32, filter_size=(3, 3), pad="same",
        nonlinearity=leaky_rectify, W=HeNormal()
    ))
    network = MaxPool2DLayer(network, pool_size=(2, 2))

    network = batch_norm(Conv2DLayer(
        network,
        num_filters=64, filter_size=(3, 3), pad="same",
        nonlinearity=leaky_rectify, W=HeNormal()
    ))

    network = batch_norm(Conv2DLayer(
        network,
        num_filters=64, filter_size=(3, 3), pad="same",
        nonlinearity=leaky_rectify, W=HeNormal()
    ))
    network = MaxPool2DLayer(network, pool_size=(2, 2))

    network = batch_norm(Conv2DLayer(
        network,
        num_filters=128, filter_size=(3, 3), pad="same",
        nonlinearity=leaky_rectify, W=HeNormal()
    ))

    network = batch_norm(Conv2DLayer(
        network,
        num_filters=128, filter_size=(3, 3), pad="same",
        nonlinearity=leaky_rectify, W=HeNormal()
    ))

    network = batch_norm(Conv2DLayer(
        network,
        num_filters=128, filter_size=(3, 3), pad="same",
        nonlinearity=leaky_rectify, W=HeNormal()
    ))
    network = MaxPool2DLayer(network, pool_size=(2, 2))

    network = batch_norm(Conv2DLayer(
        network,
        num_filters=256, filter_size=(3, 3), pad="same",
        nonlinearity=leaky_rectify, W=HeNormal()
    ))

    network = batch_norm(Conv2DLayer(
        network,
        num_filters=256, filter_size=(3, 3), pad="same",
        nonlinearity=leaky_rectify, W=HeNormal()
    ))

    network = batch_norm(Conv2DLayer(
        network,
        num_filters=256, filter_size=(3, 3), pad="same",
        nonlinearity=leaky_rectify, W=HeNormal()
    ))
    network = MaxPool2DLayer(network, pool_size=(2, 2))

    network = DenseLayer(
        network,
        num_units=2048, nonlinearity=leaky_rectify,
        W=HeNormal()
    )

    network = DropoutLayer(network, p=0.5)

    network = DenseLayer(
        network,
        num_units=num_outputs, nonlinearity=softmax,
        W=HeNormal()
    )

    return network

