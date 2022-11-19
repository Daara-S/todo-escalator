from datetime import datetime, date

from todoist_api_python.api import TodoistAPI

from todo_escalator.config import Config
from todo_escalator.utilities import Priority

config = Config()


def escalate_task(api: TodoistAPI, task_id: str) -> None:
    """
    Raise priority level of tasks with the "@escalate" label.

    :param api: TodoistAPI
    :param task_id: id of a task
    """
    task_obj = api.get_task(task_id=task_id)
    task_date = datetime.strptime(task_obj.due.date, "%Y-%m-%d").date()
    priority_level = task_obj.priority

    if task_date == date.today():
        if priority_level < Priority.red:
            priority_level += 1
        api.update_task(task_id=task_id, priority=priority_level)
        print(f"Update task \"{task_obj.content}\" to priority {priority_level}.")


def run_classic():
    api = TodoistAPI(config.api_token.get_secret_value())

    try:
        tasks = api.get_tasks()
        for task in tasks:
            if "escalate" in task.labels:
                escalate_task(api, task.id)
    except Exception as error:
        print(error)


if __name__ == "__main__":
    run_classic()
