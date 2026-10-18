#----------------------------------------------------------------------------
# Deep Learning Assignment :
#----------------------------------------------------------------------------
# 1: Write a Python program to simulate a single artificial neuron.
# Input:
# x1 = 2
# x2 = 3
# w1 = 0.4
# w2 = 0.6
# bias = 0.5
# Tasks:
# 1. Calculate weighted sum.
# 2. Apply sigmoid activation function.
# 3. Display final output.
# 4. Explain whether output is close to 0 or 1.
#----------------------------------------------------------------------------
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf

inputs = tf.constant([2.0, 3.0])
weights = tf.constant([0.4, 0.6])
bias = tf.constant(0.5)

# 1. Calculate weighted sum
weighted_sum = tf.reduce_sum(inputs * weights) + bias

print("Inputs:", inputs.numpy())
print("Weights:", weights.numpy())
print("Bias:", bias.numpy())
print("Weighted Sum:", weighted_sum.numpy())

# 2. Apply sigmoid activation function
output = tf.sigmoid(weighted_sum)

# 3. Display final output
print("Final Output:", output.numpy())

# 4. Explain the output
if output.numpy() > 0.5:
    print("The output is close to 1.")
else:
    print("The output is close to 0.")
