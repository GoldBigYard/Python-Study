import matplotlib.pyplot as plt
import time
import sys

sample_list = []
size_list = []

if __name__ == '__main__':
    iteration = 20
    for i in range(iteration):
        sample_list.append(10)
        list_size = sys.getsizeof(sample_list)
        size_list.append(list_size)

    fig = plt.figure()
    fig.suptitle("some graph")
    plt.plot(size_list, 'k--')
    plt.xlim((0,iteration))
    plt.xticks(range(iteration+1), range(iteration+1))

    plt.show()

