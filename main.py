import random
import matplotlib.pyplot as plt

data = [random.randint(1, 100) for _ in range(20)]

speed = float(input("Enter speed (0.01 fast - 1 slow): "))


def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            
            colors = ["blue"] * len(data)
            colors[j] = "red"
            colors[j + 1] = "red"

            plt.clf()
            plt.bar(range(len(data)), data, color=colors)
            plt.title("Bubble Sort")
            plt.pause(speed)

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            
            colors = ["blue"] * len(data)
            colors[i] = "green"
            colors[j] = "red"

            plt.clf()
            plt.bar(range(len(data)), data, color=colors)
            plt.title("Selection Sort")
            plt.pause(speed)

            if data[j] < data[min_index]:
                min_index = j
        
        data[i], data[min_index] = data[min_index], data[i]


# Menu
print("1. Bubble Sort")
print("2. Selection Sort")

choice = input("Choose algorithm: ")

plt.figure()

if choice == "1":
    bubble_sort(data)
elif choice == "2":
    selection_sort(data)
else:
    print("Invalid choice")

plt.show()