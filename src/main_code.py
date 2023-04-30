from utils import load_operations, get_last_five_operations, get_operation_data

OPERATIONS_LIST_PATH = 'operations.json'

# Загружаем данные из файла, формируем список экземпляров класса Operation
operations_list = load_operations(OPERATIONS_LIST_PATH)
# Собираем последние 5 операций в список
last_five_operations = get_last_five_operations(operations_list)
# Формируем вывод данных по каждой операции
for operation in last_five_operations:
    print(get_operation_data(operation))
    print()
