from utils import load_operations, get_last_5_operations, get_right_format

# Загружаем данные из файла
operations_data = load_operations('operations.json')
# Собираем последние 5 операций в список
last_five_operations = get_last_5_operations(operations_data)
# Преобразуем каждый элемент списка в экземпляр класса Operations с занемением необходимой информации
final_list = get_right_format(last_five_operations)
# Преобразуем данные по операциям в нужный формат и выводим на экран
for operation in final_list:
    print(operation.right_format_data())
    print()
