def sort_strings_by_length(strings):
    return sorted(strings, key=len)

# Пример использования:
strings = ['apple', 'banana', 'orange', 'kiwi', 'grape']
sorted_by_length = sort_strings_by_length(strings)
print("Список строк, отсортированный по длине (по возрастанию):", sorted_by_length)
print("Список строк, отсортированный по длине (по убыванию):", sorted_by_length[::-1])