import matplotlib.pyplot as plt
import time

sample_list = []
elapsed_time_list = []

if __name__ == '__main__':
    iteration = 20
    for i in range(iteration):
        start_time = time.thread_time_ns()
        sample_list.append(10)
        end_time = time.thread_time_ns()
        elapsed_time = end_time - start_time
        elapsed_time_list.append(elapsed_time)

    fig = plt.figure()
    fig.suptitle("some graph")
    plt.plot(elapsed_time_list, 'k--')
    plt.xlim((0,iteration))
    plt.xticks(range(iteration+1), range(iteration+1))

    plt.show()

