def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

def get_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

def clear_tasks():
    with open("tasks.txt", "w") as file:
        pass


add_task("Brush my teeth")

print(get_tasks())