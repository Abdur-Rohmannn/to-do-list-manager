tasks = []

def add_task():
    return tasks.append()
    
    
def show_tasks():
    for item in tasks:
        print(item)
    
    
def  delete_task():
    return tasks.remove()
    
while True:
    
    print("1. Добавить")
    print("2. Посмотреть список")
    print("3. Удалить")
    print("4. Выход")
    
    choice = input("Выбрать задачу: ")
    
    if choice == "4":
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