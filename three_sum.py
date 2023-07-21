# Brute Force approach with time complexity = O(N^3)

def three_sum(num_array: list) -> list[list[int]]:
    result_array: list = []
    for i in range(len(num_array) - 2):
        for j in range(i+1, len(num_array) - 1):
            for k in range(j+1, len(num_array)):
                if num_array[i] + num_array[j] + num_array[k] == 0:
                    result_array.append([num_array[i], num_array[j], num_array[k]])
    return result_array


try:
    nums_array = list(map(int, input("Enter integers separated by space : ").split()))
    print("The resultant array is : ", three_sum(nums_array))
except ValueError:
    print("Invalid Input. Enter only integers")