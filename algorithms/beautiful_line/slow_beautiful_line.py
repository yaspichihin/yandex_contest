filename = 'D:/qsync/1.git/yandex_contest/algorithms/beautiful_line/beautiful_line_input_6.txt'


with open(filename, encoding='utf-8') as src:
    k = int(src.readline().strip())
    string = src.readline().strip()

# k = 1
# string = "aabbaa"

result = 0
string_length = len(string)
for letter in sorted(set(string)):

    # Для каждой буквы сбрасываем максимальную дистанцию к 0 для ее расчета
    max_symbol_distance = 0

    # Для каждой буквы будем двигать левый указатель до конца строки
    for left_pointer in range(string_length):
        right_pointer = left_pointer
        symbol_distance = 0
        changes = k

        while changes >= 0 and right_pointer <= string_length - 1:
            if letter != string[right_pointer]:
                changes -= 1
            if changes >= 0:
                symbol_distance += 1
                right_pointer += 1
            else:
                break
    
        if symbol_distance > max_symbol_distance:
            max_symbol_distance = symbol_distance

    if max_symbol_distance > result:
        result = max_symbol_distance
            
print(result)
