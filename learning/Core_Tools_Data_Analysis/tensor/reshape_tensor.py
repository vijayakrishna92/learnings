#reshaping
import tensorflow as tf

tensors = tf.constant([[1,2,3],[4,5,6]])
sizes = tf.size(tensors)
reshaped_1d = tf.reshape(tensors,[sizes]) # convert from 2d to 1d
print(reshaped_1d)
reshaped_2d = tf.reshape(reshaped_1d,[3,2]) # convert from 1d to 2d
print(reshaped_2d)
transopses = tf.transpose(reshaped_2d) # transpose from [3,2] to [2,3]
print(transopses)