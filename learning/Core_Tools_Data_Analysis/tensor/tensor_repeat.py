import tensorflow as tf

features = tf.constant([[1.0], [2.0], [3.0], [4.0]])
labels = tf.constant([0,1,1,0])

dataset = tf.data.Dataset.from_tensor_slices((features,labels))
dataset = dataset.repeat(2)
print("After repeating:")
for i, (x, y) in enumerate(dataset):
    print(x.numpy(), y.numpy())
    if i >= 7:  # Stop after some samples to avoid infinite loop
        break

    '''Loops over the data multiple times (epochs)
Needed for training over multiple passes.'''