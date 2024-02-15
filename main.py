from task import TaskController


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
