from src.environment import GridEnvironment
from src.path_planning import astar
from src.visualization import run_simulation

import matplotlib
matplotlib.use('Agg')   # No GUI error

import matplotlib.pyplot as plt
import time
import os

def main():
    print("Program started")

    # Create environment
    env = GridEnvironment(20, 20)

    start = (0, 0)
    goal = (19, 19)

    # Moderate obstacles
    env.add_random_obstacles(70)

    # ⏱️ Execution time
    start_time = time.time()
    path = astar(env.grid, start, goal)
    end_time = time.time()

    execution_time = end_time - start_time
    print("Execution Time:", execution_time, "seconds")

    print("Path:", path)

    # If no path, stop
    if not path:
        print("No path found!")
        return

    path_length = len(path)
    print("Path Length:", path_length)

    # ==============================
    # 📊 PATH SHAPE GRAPH
    # ==============================
    x = [node[0] for node in path]
    y = [node[1] for node in path]

    plt.figure()
    plt.plot(x, y, marker='o')
    plt.title("Path Taken by Agent")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.gca().invert_yaxis()

    if os.path.exists("outputs/images/path_shape.png"):
        os.remove("outputs/images/path_shape.png")

    plt.savefig("outputs/images/path_shape.png")
    print("Updated path_shape.png")


    # ==============================
    # 🔥 OBSTACLES vs PATH LENGTH
    # ==============================
    obstacle_counts = [5, 10, 15, 20, 25]
    path_lengths = []

    for count in obstacle_counts:
        temp_env = GridEnvironment(20, 20)
        temp_env.add_random_obstacles(count)

        temp_path = astar(temp_env.grid, start, goal)

        if temp_path:
            path_lengths.append(len(temp_path))
        else:
            path_lengths.append(0)

    plt.figure()
    plt.plot(obstacle_counts, path_lengths, marker='o')
    plt.title("Obstacles vs Path Length")
    plt.xlabel("Number of Obstacles")
    plt.ylabel("Path Length")

    if os.path.exists("outputs/images/obstacle_vs_path.png"):
        os.remove("outputs/images/obstacle_vs_path.png")

    plt.savefig("outputs/images/obstacle_vs_path.png")
    print("Updated obstacle_vs_path.png")


    # ==============================
    # 🔥 OBSTACLES vs EXECUTION TIME
    # ==============================
    times = []

    for count in obstacle_counts:
        temp_env = GridEnvironment(20, 20)
        temp_env.add_random_obstacles(count)

        t1 = time.time()
        astar(temp_env.grid, start, goal)
        t2 = time.time()

        times.append(t2 - t1)

    plt.figure()
    plt.plot(obstacle_counts, times, marker='o')
    plt.title("Obstacles vs Execution Time")
    plt.xlabel("Number of Obstacles")
    plt.ylabel("Time (seconds)")

    if os.path.exists("outputs/images/time_vs_obstacles.png"):
        os.remove("outputs/images/time_vs_obstacles.png")

    plt.savefig("outputs/images/time_vs_obstacles.png")
    print("Updated time_vs_obstacles.png")


    # ==============================
    # 🔥 HEATMAP
    # ==============================
    plt.figure()
    plt.imshow(env.grid, cmap='hot', interpolation='nearest')
    plt.title("Obstacle Heatmap")
    plt.colorbar()

    if os.path.exists("outputs/images/heatmap.png"):
        os.remove("outputs/images/heatmap.png")

    plt.savefig("outputs/images/heatmap.png")
    print("Updated heatmap.png")


    print("Starting simulation...")

    # Run simulation
    run_simulation(env, path, start, goal)


if __name__ == "__main__":
    main()