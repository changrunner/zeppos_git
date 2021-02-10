import unittest
from zeppos_git.branch import Branch


class TestTheProjectMethods(unittest.TestCase):
    def test_get_hello_world_methods(self):
        self.assertEqual("main", Branch.get_current())


if __name__ == '__main__':
    unittest.main()
