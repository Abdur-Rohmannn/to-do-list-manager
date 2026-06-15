'''1. Добавить
2. Посмотреть список
3. Удалить
4. Сохранить задачи
5. Загрузить задачи
6. Очистить список
7. Выход ''' 
tasks = []


def save_tasks():
    pass

def load_tasks():
    pass

def clean_tasks():
    pass
    
def exit_tasks():
    pass 

while True:
    
    print("1. Добавить")
    print("2. Посмотреть список")
    print("3. Удалить")
    print("4. Сохранить задачи")
    print("5. Загрузить задачи")
    print("6. Очистить список")
    print("7. Выход")
    
    choice = input("Выбрать задачу: ")
    
    if choice == "7":
        print("Выход")
        break
    
    
    if choice == "1":
        task = input("Добавить запись: ")
        tasks.append(task)
        
    elif choice == "2":
        if not tasks:
            print("Список пуст !")
        else:
            print("Cписок: ")
            for task in tasks:
                print("- " + task)
        

        
    elif choice == "3":
        delet = input("Какую запись удалить ?: ")
        if delet in tasks:
            tasks.remove(delet)
            print("Запись удалена !")
        else:
            print("Такой записи нет !")
            
    elif choice == "4":
        if not tasks:
            print("Список пуст !")
            
        else:
            with open("tasks.txt", 'w') as file:
                for item in tasks:
                    file.write(item)
            print("Сохранено")
            
            continue
        
    elif choice == "5":
        try:
            with open("tasks.txt", "r") as file:
                tasks = [task.strip() for task in file.readlines()]
                
            print("Задачи загружены")
        except FileNotFoundError:
            print("Ошибка") 
            
    elif choice == "6":
        if not tasks:
            print("Список пуст !")
        else:
            tasks.clear()
            print("Список очищен")
            
        continue
        
        
                