# tensorflow
# it is a library for dataflow and differentiable programming across a range of tasks.
# it is used for machine learning and deep learning
# it is used for building and training neural networks

import tensorflow as tf

gpu_check = tf.config.experimental.list_physical_devices('GPU')
if gpu_check:
    print("GPU is available")
else:
    print("GPU is not available")