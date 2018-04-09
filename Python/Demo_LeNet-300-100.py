import numpy as np 
import tensorflow as tf 
import time

from tensorflow.examples.tutorials.mnist import input_data

def _relu(x, leakness=0.0):
    return tf.where(tf.less(x, 0.0), leakness * x, x, name = 'leaky_relu')

def _fc(name, x, out_dim):
    with tf.variable_scope(name):
        w = tf.get_variable('DW', [x.get_shape()[1], out_dim],initializer=tf.uniform_unit_scaling_initializer(factor=1.0))
        b = tf.get_variable('biases', [out_dim],initializer=tf.constant_initializer())
        return tf.nn.xw_plus_b(x, w, b)

mnist = input_data.read_data_sets('MNIST_data', one_hot = True)
x	= tf.placeholder('float', shape = [None, 784], name = 'InputData')
y_ 	= tf.placeholder('float', shape = [None, 10] , name = 'InputLabel')
keep_prob = tf.placeholder('float')
keep_prob_val = 1
batch_size  = 50

lrn 	  = 2e-3
_epoch    = 4
maxIter   = _epoch * 55000/50


logs_path = 'tmp/tensorflow_logs/LeNet300100/'
save_path = 'tmp/savepoint/'

x_image = x
l1 		= tf.nn.dropout(_relu(_fc('layer1', x_image, 300)), keep_prob)
l2 		= tf.nn.dropout(_relu(_fc('layer2', l1, 100)), keep_prob)
l3 		= _relu(_fc('layer3', l2, 10))
y_pred 	= tf.nn.softmax(l3)

# Training 
with tf.name_scope('Loss'):
	cross_entropy = - tf.reduce_sum(y_*tf.log(y_pred))

train_step = tf.train.AdamOptimizer(lrn).minimize(cross_entropy)

with tf.name_scope('Accuracy'):
	accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(y_pred, 1), tf.argmax(y_,1)), tf.float32))

# Log
init = tf.global_variables_initializer()
loss = tf.summary.scalar('loss', cross_entropy)
train_accuracy = tf.summary.scalar('train_accuracy', accuracy)
merged_summary_op = tf.summary.merge_all()
valid_accuracy = tf.summary.scalar('validation_accuracy', accuracy)
test_accuracy  = tf.summary.scalar('test_accuracy', accuracy)

train_time = []
valid_time = []
start = time.time()
saver = tf.train.Saver()
with tf.Session() as sess:
	sess.run(init)
	summary_writer = tf.summary.FileWriter(logs_path, graph = tf.get_default_graph())
	
	for i in range(maxIter):
		# training
		batch = mnist.train.next_batch(batch_size)
		time_tp = time.time()
		_, _, summary = sess.run([train_step, cross_entropy,merged_summary_op], feed_dict = {x: batch[0], y_:batch[1], keep_prob:keep_prob_val})
		train_time.append(time.time()-time_tp)
		summary_writer.add_summary(summary, i)

		# validation
		if i%1100 ==0:
			time_tp = time.time()
			print_valid_accuracy, summary = sess.run([accuracy, valid_accuracy], feed_dict={x:mnist.validation.images, y_:mnist.validation.labels, keep_prob:1})
			valid_time.append(time.time()-time_tp)
			summary_writer.add_summary(summary, i)
			print('epoch %d, validation accuracy %g, total time %g' %(i/1100, print_valid_accuracy, time.time()-start))

	# testing
	time_tp = time.time()
	time_tp = time.time()
	print_test_accuracy, summary = sess.run([accuracy, test_accuracy],feed_dict={x:mnist.test.images, y_:mnist.test.labels, keep_prob:1.0})
	test_time = time.time()-time_tp
	TotalPar = np.sum([np.prod(v.get_shape().as_list()) for v in tf.trainable_variables()])
	print('Test accuracy %g, total parameter is %g, testing time is %g' % (print_test_accuracy, TotalPar, test_time))

print("Run the command line:\n" \
      "--> tensorboard --logdir=" + logs_path + \
      "\nThen open http://0.0.0.0:6006/ into your web browser")
















