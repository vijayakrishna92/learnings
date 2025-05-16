import tensorflow as tf

features = tf.constant([[1.0], [2.0], [3.0], [4.0]])
labels = tf.constant([0,1,1,0])

dataset = tf.data.Dataset.from_tensor_slices((features,labels))
for i,j in dataset:
  print(i.numpy(),j.numpy())