__author__ = 'robert'

import numpy as np
import matplotlib.pyplot as plt
import fast_soinn


mean1 = [0.5, 0.5]
mean2 = [5.0, 0.5]
conv1 = [[1, 0], [0, 1]]
conv2 = [[1.5, 0], [0, 1.2]]
class1_data = np.random.multivariate_normal(mean1, conv1, 5000)
class2_data = np.random.multivariate_normal(mean2, conv2, 5000)
train_data = np.concatenate((class1_data, class2_data))

plt.switch_backend('Qt4Agg')
plt.figure(1)
plt.plot(train_data[:, 0], train_data[:, 1], 'x')

nodes, connection, classes = fast_soinn.fast_soinn(train_data, 15, 10, 1.0, 0.5)

plt.figure(2)
plt.hold(True)
for i in xrange(0, nodes.shape[0]):
    for j in xrange(0, nodes.shape[0]):
        if connection[i, j] != 0:
            plt.plot([nodes[i, 0], nodes[j, 0]], [nodes[i, 1], nodes[j, 1]], 'b-')
            pass
plt.hold(False)
plt.show()

