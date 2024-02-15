import json
from uuid import uuid4
from utils import input_with_prefill
from constants import prompt_title, prompt_desc, prompt_edit, prompt_delete
from typing import Dict, TypeAlias

Tasks: TypeAlias = list[Dict[str, str]]


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

    def add_task(self, tasks: Tasks):
        print('Add Task')
        title = input(prompt_title)
        description = input(prompt_desc)
        task_id = TaskId()
        new_task = {'id': task_id.uid, 'title': title,
                    'description': description}
        tasks.append(new_task)

    def view_tasks(self, tasks):
        print('Current Tasks: ', tasks)

    def delete_task(self, tasks: Tasks):
        task_id = input(prompt_delete)
        for index, task in enumerate(tasks):
            if task['id'] == str(task_id):
                tasks.pop(index)

    def edit_task(self, tasks: Tasks):
        task_id = input(prompt_edit)
        for task in tasks:
            if task['id'] == str(task_id):
                task['title'] = input_with_prefill(
                    prompt_title, task['title'])
                task['description'] = input_with_prefill(prompt_desc,
                                                         task['description'])
                break


def main():
    task = TaskController()
    tasks = task.load_tasks()
    try:
        while True:
            print('1: Add')
            print('2: View')
            print('3: Delete Task')
            print('4: Edit Task')
            print('5: Save and Exit')
            choice = input('Please select an option: ')

            if choice == '1':
                task.add_task(tasks)
            elif choice == '2':
                task.view_tasks(tasks)
            elif choice == '3':
                task.delete_task(tasks)
            elif choice == '4':
                task.edit_task(tasks)
            elif choice == '5':
                task.save_tasks(tasks)
                break
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main()
