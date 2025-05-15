# ragged tensors
#  Sentences and paragraphs have different lengths. Ragged tensors handle this irregularity perfectly, making them ideal for tasks like sentiment analysis and machine translation. ensor readings or financial data may have missing entries or be collected at irregular intervals. Ragged tensors effortlessly manage these inconsistencies.

import tensorflow as tf

tensors = tf.ragged.constant([[1,2],[3,4,5],[5]])
print(tensors)

words = [1,2,3,4,5,6]
row_id = [0,0,0,0,2,2]
ragged_tensors = tf.RaggedTensor.from_value_rowids(words, row_id)
print(ragged_tensors)