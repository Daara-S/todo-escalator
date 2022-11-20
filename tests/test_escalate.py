from dataclasses import dataclass
from datetime import date

import pytest
from todoist_api_python.models import Task

from tests.test_defaults import DEFAULT_TASK_RESPONSE
from todo_escalator.handler import escalate_task


@dataclass
class MockAPI:
    task: Task

    def get_task(self, task_id):
        return self.task

    def update_task(self, task_id, priority):
        self.task.priority = priority


@pytest.mark.parametrize("priority, exp_priority", [(1, 2), (2, 3), (3, 4), (4, 4)])
def test_escalate_task_priority(priority, exp_priority):
    task = Task.from_dict(DEFAULT_TASK_RESPONSE)
    task.priority = 1
    api = MockAPI(task)
    task.due.date = str(date.today())
    escalate_task(api, task.id)

    assert task.priority == 2
