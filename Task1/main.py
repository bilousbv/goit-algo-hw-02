import queue
import time
import random
import threading

# Створення черги для заявок
request_queue = queue.Queue()

# Лічильник для унікального ID заявки
request_id = 1

# Функція для генерації нових заявок
def generate_request():
    global request_id
    while True:
        # Створюємо нову заявку з унікальним ID
        request = f"Заявка №{request_id}"
        request_queue.put(request)
        print(f"{request} додана до черги")
        request_id += 1
        # Затримка, щоб імітувати час між заявками
        time.sleep(random.uniform(1, 3))

# Функція для обробки заявок
def process_request():
    while True:
        if not request_queue.empty():
            # Виймаємо заявку з черги
            request = request_queue.get()
            print(f"Обробка {request}")
            # Імітуємо час обробки заявки
            time.sleep(random.uniform(2, 4))
            print(f"{request} оброблена")
            # Відмічаємо заявку як оброблену
            request_queue.task_done()
        else:
            print("Черга пуста, очікуємо нові заявки...")
            time.sleep(2)

# Створення потоків для генерації та обробки заявок
generate_thread = threading.Thread(target=generate_request)
process_thread = threading.Thread(target=process_request)

# Запуск потоків
generate_thread.start()
process_thread.start()

# Очікуємо завершення потоків (буде працювати безкінечно)
generate_thread.join()
process_thread.join()