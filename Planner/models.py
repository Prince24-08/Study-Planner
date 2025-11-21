from dataclasses import dataclass, asdict

@dataclass
class Task:
    id: str
    title: str
    subject: str
    est_hours: float
    deadline: str
    priority: int
    status: str = "Pending"

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(d):
        return Task(**d)
