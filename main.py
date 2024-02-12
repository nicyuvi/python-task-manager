import json
from uuid import uuid4


class TaskId():
    def __init__(self):
        self.uid = uuid4().hex


class TaskController():
    def load_tasks(self):
        # need try/except bc this will error if file does not exists
        try:
            with open('tasks.json', 'r') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = []
        return tasks

    def save_tasks(self, tasks):
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file, indent=4)

    def add_task(self, tasks, title, description):
        task_id = TaskId()
        new_task = {'id': task_id.uid, 'title': title,
                    'description': description}
        tasks.append(new_task)

    def view_tasks(self, tasks):
        print('Current Tasks: ', tasks)

    def delete_task(self, tasks, task_id):
        for index, task in enumerate(tasks):
            if task['id'] == str(task_id):
                tasks.pop(index)


def main():
    task = TaskController()
    tasks = task.load_tasks()
    try:
        while True:
            print('1: Add')
            print('2: View')
            print('3: Delete Task')
            print('4: Save and Exit')
            choice = input('Please select an option: ')

            if choice == '1':
                print('Add Task')
                title = input('Enter title: ')
                description = input('Enter description: ')
                task.add_task(tasks, title, description)
            elif choice == '2':
                task.view_tasks(tasks)
            elif choice == '3':
                task_id = input('Enter task ID to delete: ')
                task.delete_task(tasks, task_id)
            elif choice == '4':
                task.save_tasks(tasks)
                break
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main()
