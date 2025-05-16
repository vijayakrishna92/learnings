import tensorflow as tf

features = tf.constant([[1.0], [2.0], [3.0], [4.0]])
labels = tf.constant([0,1,1,0])

dataset = tf.data.Dataset.from_tensor_slices((features,labels))
dataset = dataset.batch(2)
print("After batching:")
for batch_x, batch_y in dataset:
    print(batch_x.numpy(), batch_y.numpy())
    '''Groups samples together
Speeds up training and uses GPU efficiently.'''