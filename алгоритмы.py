input_str = input("Введите список чисел через запятую: ")

numbers = [int(x.strip()) for x in input_str.split(',')]

even_numbers = [num for num in numbers if num % 2 == 0]

maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

sorted_numbers = numbers.copy()
n = len(sorted_numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if sorted_numbers[j] > sorted_numbers[j + 1]:
            sorted_numbers[j], sorted_numbers[j + 1] = sorted_numbers[j + 1], sorted_numbers[j]

print("Четные числа:", even_numbers)
print("Максимальное число:", maximum)
print("Минимальное число:", minimum)
print("Отсортированный список:", sorted_numbers)

