import tracemalloc



if __name__ == '__main__':
    tracemalloc.start(1)
    a = []

    old_snapshot = tracemalloc.take_snapshot()
    new_snapshot = tracemalloc.take_snapshot()
    for i in range(100):
        old_snapshot = new_snapshot
        new_snapshot = tracemalloc.take_snapshot()
        a.append(100)
        result = new_snapshot.filter_traces([tracemalloc.Filter(inclusive=True, filename_pattern="*.py", lineno=14)]).statistics('lineno', cumulative=True)
        if result:
            print(f"{i+1}: {result[0].size}")
        # print(new_snapshot.compare_to(old_snapshot.filter_traces(tracemalloc.Filter(inclusive=True, filename_pattern="*.py", lineno=14)), "lineno"))
