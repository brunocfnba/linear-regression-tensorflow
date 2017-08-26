import tensorflow as tf


# Parameters
W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)

# Input
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

# Model
lm = x * W + b

# Calculating the cost
squared_delta = tf.square(lm-y)
cost = tf.reduce_sum(squared_delta)

# Optimizing the error / cost
optimize = tf.train.GradientDescentOptimizer(0.01)

train = optimize.minimize(cost)

init = tf.global_variables_initializer()


with tf.Session() as sess:
    sess.run(init)

    # fw = tf.summary.FileWriter('<path to save the graph without file name>', sess.graph)

    for i in range(1000):
        sess.run(train, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]})
        print(sess.run(cost, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))

    print("Variables W and b: {}".format(sess.run([W, b])))
    
    test_data = 3
    print("Value for {} is {}".format(test_data, round((test_data * sess.run(W) + sess.run(b))[0])))
