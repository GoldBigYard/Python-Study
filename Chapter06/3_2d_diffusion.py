import timeit

grid_shape = (640, 640)
new_grid = [[0.0] * grid_shape[0] for x in range(grid_shape[0])]


def evolve(grid, dt, D=1.0):
    xmax, ymax = grid_shape
    new_grid = [[0.0] * ymax for x in range(xmax)]
    for i in range(xmax):
        for j in range(ymax):
            grid_xx = (
                grid[(i + 1) % xmax][j] + grid[(i - 1) % xmax][j] - 2.0 * grid[i][j]
            )
            grid_yy = (
                    grid[i][(j + 1) % ymax] + grid[i][(j - 1) % ymax] - 2.0 * grid[i][j]
            )
            new_grid[i][j] = grid[i][j] + D * (grid_xx + grid_yy) * dt
    return new_grid


def evolve_not_create_list(grid, dt, D=1.0):
    xmax, ymax = grid_shape
    for i in range(xmax):
        for j in range(ymax):
            grid_xx = (
                    grid[(i + 1) % xmax][j] + grid[(i - 1) % xmax][j] - 2.0 * grid[i][j]
            )
            grid_yy = (
                    grid[i][(j + 1) % ymax] + grid[i][(j - 1) % ymax] - 2.0 * grid[i][j]
            )
            new_grid[i][j] = grid[i][j] + D * (grid_xx + grid_yy) * dt
    return new_grid


def evolve_better(grid, dt, D=1.0):
    xmax, ymax = grid_shape
    new_grid = []
    for i in range(xmax):
        new_row = []
        for j in range(ymax):
            grid_xx = (
                    grid[(i + 1) % xmax][j] + grid[(i - 1) % xmax][j] - 2.0 * grid[i][j]
            )
            grid_yy = (
                    grid[i][(j + 1) % ymax] + grid[i][(j - 1) % ymax] - 2.0 * grid[i][j]
            )
            new_row.append(grid[i][j] + D * (grid_xx + grid_yy) * dt)
        new_grid.append(new_row)
    return new_grid


def run_experiment(num_iterations, evolve_func):
    xmax, ymax = grid_shape
    grid = [[0.0] * ymax for x in range(xmax)]

    block_low = int(grid_shape[0] * 0.4)
    block_high = int(grid_shape[0] * 0.5)
    for i in range(block_low, block_high):
        for j in range(block_low, block_high):
            grid[i][j] = 0.005

    for i in range(num_iterations):
        grid = evolve_func(grid, 0.1)


def timeit_and_print(exec_target, setup, repeat):
    t = timeit.Timer(exec_target, setup)
    elapsed_time = t.timeit(repeat)
    print(f"{exec_target}: {elapsed_time}")


if __name__ == '__main__':
    count = 10
    timeit_and_print(
        "run_experiment(10, evolve)",
        "from __main__ import run_experiment, evolve",
        count
    )
    timeit_and_print(
        "run_experiment(10, evolve_better)",
        "from __main__ import run_experiment, evolve_better",
        count
    )
    timeit_and_print(
        "run_experiment(10, evolve_not_create_list)",
        "from __main__ import run_experiment, evolve_not_create_list",
        count
    )
