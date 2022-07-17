import tracemalloc
import matplotlib.pyplot as plt

if __name__ == '__main__':
    iteration = 1000
    tracemalloc.start(1)
    sample_list = []
    sample_dict = {}
    list_size_vector = []
    dict_size_vector = []

    old_snapshot = tracemalloc.take_snapshot()
    new_snapshot = tracemalloc.take_snapshot()
    for i in range(iteration):
        old_snapshot = new_snapshot
        new_snapshot = tracemalloc.take_snapshot()
        sample_list.append(100)
        sample_dict[i] = str(i)
        list_result = new_snapshot.filter_traces([tracemalloc.Filter(inclusive=True, filename_pattern="*.py", lineno=17)]).statistics('lineno', cumulative=True)
        dict_result = new_snapshot.filter_traces([tracemalloc.Filter(inclusive=True, filename_pattern="*.py", lineno=18)]).statistics('lineno', cumulative=True)
        if list_result:
            list_size_vector.append(list_result[0].size)
        if dict_result:
            dict_size_vector.append(dict_result[0].size)

    fig = plt.figure()
    fig.suptitle("some graph")
    plt.plot(list_size_vector, 'k--')
    plt.plot(dict_size_vector, 'r--')
    plt.xlim((0,iteration))
    plt.xticks(range(0, iteration+1, int(int(iteration)/10)), range(0, iteration+1, int(int(iteration)/10)))

    plt.show()
