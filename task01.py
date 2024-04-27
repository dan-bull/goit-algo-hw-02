from queue import Queue

# Створити чергу заявок
queue = Queue()

def generate_request():
    # Створити нову заявку
    new_request = input("Enter the name of your request: \n")
    print(f"Request {new_request} added to the queue.")
    # Додати заявку до черги
    queue.put(new_request)

# Функція 
def process_request():
#     Якщо черга не пуста:
    while not queue.empty():
#       Видалити заявку з черги
        current_request = queue.get()
#       Обробити заявку
        print(f"Request {current_request} was processed.")
    else:
#       Вивести повідомлення, що черга пуста
        print("Queue of requests is empty")

# Головний цикл програми:

    # Поки користувач не вийде з програми:
while True:
    # Виконати generate_request() для створення нових заявок
    generate_request()

    # Виконати process_request() для обробки заявок
    process_request()

    choice = input("Enter 'exit' to close the program:\n")
    if choice.lower() == "exit":
        break
print("Program closed")


