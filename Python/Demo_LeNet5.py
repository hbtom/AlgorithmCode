import tensorflow as tf 
from tensorflow.contrib.layers import flatten
import numpy as np
import time
from sklearn.utils import shuffle

def _fc(name, x, out_dim):
	with tf.variable_scope(name):
		w = tf.get_variable('DW', [x.get_shape()[1], out_dim],initializer=tf.uniform_unit_scaling_initializer(factor=1.0))
		b = tf.get_variable('biases', [out_dim],initializer=tf.constant_initializer())
		return tf.nn.xw_plus_b(x, w, b)

def _conv(name, x, filter_size, in_filters, out_filters, strides):
	with tf.variable_scope(name):
		n = filter_size * filter_size * out_filters
		kernel = tf.get_variable('DW', [filter_size, filter_size, in_filters, out_filters], tf.float32, initializer = tf.random_normal_initializer(stddev=np.sqrt(2.0/n)))
		return tf.nn.conv2d(x, kernel, strides, padding = 'VALID')


# Data processing to making it 32 x 32 
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", reshape=False, one_hot = True)
X_train,      y_train      = mnist.train.images, mnist.train.labels
X_validation, y_validation = mnist.validation.images, mnist.validation.labels
X_test,       y_test       = mnist.test.images, mnist.test.labels
X_train      = np.pad(X_train, ((0,0),(2,2),(2,2),(0,0)), 'constant') # pad zeros in each order
X_validation = np.pad(X_validation, ((0,0),(2,2),(2,2),(0,0)), 'constant')
X_test       = np.pad(X_test, ((0,0),(2,2),(2,2),(0,0)), 'constant')
x  	= tf.placeholder("float", shape = [None, 32, 32, 1])
y_ 	= tf.placeholder("float", shape = [None, 10])													


lrn				= 1e-3
EPOCHS 			= 5
BATCH_SIZE 		= 128

saver_p = "tmp/LeNet5/model"
logs_path = 'tmp/tensorflow_logs/LeNet5/'

conv1 = tf.nn.max_pool(tf.nn.relu(_conv('conv1', x, 5, 1, 20,[1,1,1,1])), ksize=[1,2,2,1], strides=[1,2,2,1], padding='VALID')
conv2 = tf.nn.max_pool(tf.nn.relu(_conv('conv2', conv1, 5, 20, 50,[1,1,1,1])), ksize=[1,2,2,1], strides=[1,2,2,1], padding='VALID')
fc0 	= flatten(conv2)
fc1 	= tf.nn.relu(_fc('fc1',fc0,320))
fc2 	= _fc('fc2', fc1, 10)
fc3 	= tf.nn.softmax(fc2)

with tf.name_scope('Loss'):
	cross_entropy = -tf.reduce_sum(y_*tf.log(fc3))	

train_step = tf.train.AdamOptimizer(lrn).minimize(cross_entropy)

with tf.name_scope('Accuracy'):
	accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(fc3,1), tf.argmax(y_,1)), tf.float32))		

#log
init = tf.global_variables_initializer()
loss = tf.summary.scalar('loss', cross_entropy)
train_accuracy = tf.summary.scalar('train_accuracy', accuracy)
merged_summary_op = tf.summary.merge_all()
valid_accuracy = tf.summary.scalar('validation_accuracy', accuracy)
test_accuracy  = tf.summary.scalar('test_accuracy', accuracy)
train_time = []
valid_time = []
saver = tf.train.Saver()
start = time.time()
with tf.Session() as sess:
	sess.run(init)
	summary_writer = tf.summary.FileWriter(logs_path, graph = tf.get_default_graph())

	num_examples	= len(X_train)
	move_size       = int(num_examples/BATCH_SIZE)
	for i in range(EPOCHS):
		# training
		X_train, y_train = shuffle(X_train, y_train)
		for offset in range(0, num_examples, BATCH_SIZE):
			end = offset + BATCH_SIZE
			batch_x, batch_y = X_train[offset:end], y_train[offset:end]
			time_tp =time.time()
			_, summary=sess.run([train_step, merged_summary_op], feed_dict={x: batch_x, y_: batch_y})
			train_time.append(time.time()-time_tp)
			summary_writer.add_summary(summary, i*move_size + offset)
		# validation
		time_tp = time.time()
		print_valid_accuracy, summary = sess.run([accuracy, valid_accuracy], feed_dict={ x: X_validation, y_: y_validation})
		valid_time.append(time.time()-time_tp)
		summary_writer.add_summary(summary, i)
		print('epoch %d, validation accuracy %g, total time %g' %(i, print_valid_accuracy, time.time()-start))
	# testing
	time_tp = time.time()
	print_test_accuracy, summary = sess.run([accuracy, test_accuracy], feed_dict={ x: X_test, y_: y_test})
	test_time = time.time()-time_tp
	summary_writer.add_summary(summary, i)
	TotalPar = np.sum([np.prod(v.get_shape().as_list()) for v in tf.trainable_variables()])
	print('Test accuracy %g, total parameter is %g, testing time is %g' % (print_test_accuracy, TotalPar, test_time))


print("Run the command line:\n" \
      "--> tensorboard --logdir=" + logs_path + \
      "\nThen open http://0.0.0.0:6006/ into your web browser")