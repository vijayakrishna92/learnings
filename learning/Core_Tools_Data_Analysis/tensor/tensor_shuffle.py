import tensorflow as tf

features = tf.constant([[1.0], [2.0], [3.0], [4.0]])
labels = tf.constant([0,1,1,0])

dataset = tf.data.Dataset.from_tensor_slices((features,labels))
dataset = dataset.shuffle(buffer_size=4) # buffer_size usually >= dataset size
print("After shuffling:")
for x, y in dataset:
    print(x.numpy(), y.numpy())
    '''Randomizes data order
Prevents model from learning the order and helps generalization.'''