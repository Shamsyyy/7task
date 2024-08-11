def count_unique_numbers(n, numbers):
  """Задание 1: Подсчитать количество различных чисел."""
  unique_numbers = set(numbers)
  return len(unique_numbers)

def count_common_numbers(list1, list2):
  """Задание 2: Подсчитать количество общих чисел в двух списках."""
  set1 = set(list1)
  set2 = set(list2)
  common_numbers = set1.intersection(set2)
  return len(common_numbers)

if __name__ == "__main__":
  # Задание 1
  N1 = int(input("Введите количество чисел для первой задачи: "))
  numbers1 = list(map(int, input("Введите числа через пробел: ").split()))
  unique_count = count_unique_numbers(N1, numbers1)
  print("Количество различных чисел:", unique_count)

  # Задание 2
  print("Введите первый список чисел:")
  list1 = [int(input()) for _ in range(int(input("Введите количество чисел в первом списке: ")))]
  print("Введите второй список чисел:")
  list2 = [int(input()) for _ in range(int(input("Введите количество чисел во втором списке: ")))]
  common_count = count_common_numbers(list1, list2)
  print("Количество общих чисел:", common_count)