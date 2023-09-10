import random
import time
import psutil


def save_list_to_file(filename, data):
    with open(filename, "w") as f:
        f.write(" ".join(map(str, data)))


# Generate a list of 1000000 random numbers and save each as a file
def generate_random_list(size):
    return [random.randint(1, 1000000) for _ in range(size)]


def save_list_to_file(filename, data):
    with open(filename, "w") as f:
        f.write(" ".join(map(str, data)))


def read_list_from_file(filename):
    with open(filename, "r") as f:
        data = f.read()
        return list(map(int, data.split()))


def quick_sort(array):
    # 리스트가 하나 이하의 원소를 가지면 종료
    if len(array) <= 1:
        return array

    pivot, tail = array[0], array[1:]
    leftSide, rightSide = [], []

    for x in tail:
        if x > pivot:
            rightSide.append(x)
        else:
            leftSide.append(x)

    return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)


def get_memory_usage():
    process = psutil.Process()
    return process.memory_info().rss


# First file
randomlist = generate_random_list(1000000)
randomlist.sort()
save_list_to_file("firstfile.txt", randomlist)

# Second file
randomlist = generate_random_list(1000000)
randomlist.sort(reverse=True)
save_list_to_file("secondfile.txt", randomlist)

# Third file
randomlist = generate_random_list(1000000)
save_list_to_file("thirdfile.txt", randomlist)

# Reopen the saved files and run quicksort
filenames = ["firstfile.txt", "secondfile.txt", "thirdfile.txt"]

# for filename in filenames:
data = read_list_from_file(filenames[2])
memory_before = get_memory_usage()
start_time = time.time()
sorted_data = quick_sort(data)
end_time = time.time()
memory_after = get_memory_usage()
print(f"quick_sort Time for {filenames[2]}: {end_time - start_time} seconds")
print(f"quick_sort Memory Usage: {memory_after / (1024 * 1024)} bytes")
save_list_to_file(filenames[2], sorted_data)
saved_data = read_list_from_file(filenames[2])

# Measure memory usage for list.sort()
for filename in filenames:
    data = read_list_from_file(filename)
    memory_before = get_memory_usage()
    start_time = time.time()
    data.sort()
    end_time = time.time()
    memory_after = get_memory_usage()
    print(f"list.sort() Time for {filename}: {end_time - start_time} seconds")
    print(f"list.sort() Memory Usage: {memory_after / (1024 * 1024)} bytes")
    save_list_to_file(filename, data)
    saved_data = read_list_from_file(filename)

# Measure memory usage for sorted()
for filename in filenames:
    data = read_list_from_file(filename)
    memory_before = get_memory_usage()
    start_time = time.time()
    sorted_data = sorted(data)
    end_time = time.time()
    memory_after = get_memory_usage()
    print(f"sorted() Time for {filename}: {end_time - start_time} seconds")
    print(f"sorted() Memory Usage: {memory_after / (1024 * 1024)} bytes")
    save_list_to_file(filename, sorted_data)
    saved_data = read_list_from_file(filename)
