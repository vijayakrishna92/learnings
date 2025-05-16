#arithmatic

import tensorflow as tf

#add
one = tf.constant(1)
two = tf.constant(2)

sums = tf.add(one, two)
print(sums)

#sub
one = tf.constant([1,2,3])
two = tf.constant([4,5,6])

sub = tf.subtract(one, two)
print(sub)

#mul 1d and 2d
one = tf.constant([1,2,3])
two = tf.constant([4,5,6])

mul = tf.multiply(one, two)
print(mul)

one = tf.constant([[1,2,3],[4,5,6]])
two = tf.constant([[1,2,3],[4,5,6]])

mul = tf.multiply(one, two)
print(mul)

one = tf.constant([[1,2,3],[4,5,6]])

sums = tf.reduce_sum(one)
print(sums)