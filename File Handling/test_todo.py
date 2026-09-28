import unittest
from todo import add_task, get_tasks, clear_tasks


class TestTodo(unittest.TestCase):

    def setUp(self):
        clear_tasks()

    def test_add_task(self):
        add_task("Study Python")

        tasks = get_tasks()

        self.assertEqual(tasks, ["Study Python"])

    def test_multiple_tasks(self):
        add_task("Study Python")
        add_task("Finish homework")

        tasks = get_tasks()

        self.assertEqual(
            tasks,
            ["Study Python", "Finish homework"]
        )

    def test_clear_tasks(self):
        add_task("Study Python")

        clear_tasks()

        tasks = get_tasks()

        self.assertEqual(tasks, [])


if __name__ == "__main__":
    unittest.main()