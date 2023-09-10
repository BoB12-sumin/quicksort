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


def insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        key = array[i]
        j = i - 1
        while j >= left and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def find_ternary_pivot(array, left, right):
    # 삼중 피벗 구하기 (첫 번째, 중간, 마지막 원소를 골라 정렬하여 중간 값 사용)
    mid = (left + right) // 2
    if array[left] > array[mid]:
        array[left], array[mid] = array[mid], array[left]
    if array[left] > array[right]:
        array[left], array[right] = array[right], array[left]
    if array[mid] > array[right]:
        array[mid], array[right] = array[right], array[mid]
    return array[mid]


def quick_sort(array):
    stack = []
    stack.append((0, len(array) - 1))

    while stack:
        left, right = stack.pop()

        if right - left + 1 <= 10:  # 임계값 (10 이하일 경우 삽입 정렬 수행)
            insertion_sort(array, left, right)
            continue

        # 삼중 피벗 값 구하기
        pivot = find_ternary_pivot(array, left, right)

        # 파티션
        i, j = left, right
        while i <= j:
            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1

        # 왼쪽 파티션과 오른쪽 파티션의 인덱스를 스택에 추가
        if left < j:
            stack.append((left, j))
        if i < right:
            stack.append((i, right))


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

for filename in filenames:
    data = read_list_from_file(filename)
    memory_before = get_memory_usage()
    start_time = time.time()
    quick_sort(data)
    end_time = time.time()
    # print(data) #정렬 확인
    memory_after = get_memory_usage()
    print(f"quick_sort Time for {filename}: {end_time - start_time} seconds")
    print(f"quick_sort Memory Usage: {memory_after / (1024 * 1024)} bytes")
    save_list_to_file(filename, data)
    saved_data = read_list_from_file(filename)

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
