
import os

from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import numpy as np

import tensorflow as tf
import sys, os
from keras import backend as K

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ["CUDA_VISIBLE_DEVICES"] = "1"
config = tf.ConfigProto(allow_soft_placement = True)
config.gpu_options.allow_growth=True
sess = tf.Session(config=config)
K.set_session(sess)

model_path = "../../../../data/multiagent_rl/conv256.h5"
train_filepath = "../../../../data/multiagent_rl/simple_600K_disc0.99_cleaned.npz"
valid_filepath = "../../../../data/multiagent_rl/valid_100K_disc0.99_cleaned.npz"


def get_pommerman_data(filepath):
	npz_data = np.load(filepath)
	print(npz_data.keys())
	observations = npz_data['observations']
	actions = npz_data['actions']
	rewards = npz_data['rewards']
	# values = npz_data['values']
	return (observations, actions, rewards)

(x_valid, p_valid, v_valid) = \
 	get_pommerman_data(valid_filepath)
(x_train, p_train, v_train) = \
 	get_pommerman_data(train_filepath)


def get_model(filepath):
	with tf.device("/gpu:0"):
		# load the weights and model from .h5
		model = load_model(model_path)
	print(model_path)
	model.compile(optimizer='adam', loss=['sparse_categorical_crossentropy', 'mse'], \
		loss_weights=[1, 10], metrics={'p': 'accuracy'})
	model.summary()
	return model

model = get_model(model_path)

# history = model.fit(x_train, [p_train, v_train], batch_size=128, epochs=10, validation_data=(x_test, [p_test, v_test]))

score = model.evaluate(x_train, [p_train, v_train], verbose=1)
print(score)

score = model.evaluate(x_valid, [p_valid, v_valid], verbose=1)
print(score)
