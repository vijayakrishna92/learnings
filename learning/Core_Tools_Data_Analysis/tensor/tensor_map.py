import tensorflow as tf

def add_one(x, y):
    return x + 1, y

features = tf.constant([[1.0], [2.0], [3.0], [4.0]])
labels = tf.constant([0,1,1,0])

dataset = tf.data.Dataset.from_tensor_slices((features,labels))
dataset = dataset.map(add_one)
print("After mapping (adding 1 to features):")
for x, y in dataset:
    print(x.numpy(), y.numpy())

    '''Applies custom functions (e.g., resize, augment)
 Preprocesses each sample dynamically and efficiently.'''