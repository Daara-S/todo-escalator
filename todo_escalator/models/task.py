from pydantic import BaseModel
from todoist_api_python.models import Due


class Task(BaseModel):
    id: str
    project_id: str
    section_id: str | None
    content: str
    description: str
    is_completed: bool
    labels: list[str]
    parent_id: int | None
    order: int
    priority: int
    due: Due | None
    url: str
    comment_count: int
    created_at: str
    creator_id: str
    assignee_id: str | None
    assigner_id: str | None

    class Config:
        arbitrary_types_allowed = True


class Due(BaseModel):
    date: str
    is_recurring: bool
    string: str
