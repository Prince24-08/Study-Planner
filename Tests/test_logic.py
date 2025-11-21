import unittest
from Planner.models import Task
from Planner.logic import compute_progress

class TestLogic(unittest.TestCase):
    def test_progress(self):
        tasks = [
            Task("1","Math","Math",2,"2025-12-01",1,"Completed"),
            Task("2","Phy","Physics",3,"2025-12-02",2,"Pending")
        ]
        summary = compute_progress(tasks)
        self.assertEqual(summary["total"],2)

if __name__ == "__main__":
    unittest.main()
