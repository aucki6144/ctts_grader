import numpy as np

if __name__ == "__main__":

    time_path = "./time.txt"

    try:
        with open(time_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        lines = [float(line.strip()) for line in lines]

    except Exception as e:
        print(f"An error occurred: {e}")
        lines = []

    print(lines)

    lines = np.array(lines)

    print(np.average(lines))
