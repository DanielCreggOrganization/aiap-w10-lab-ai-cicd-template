import unittest
from hello_app.webapp import app

class FailingTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_fail(self):
        # This test is designed to fail
        self.assertEqual(1, 0, "Intentional failure for testing CI/CD")

    def test_math_fail(self):
        # Another intentional failure
        assert 1 + 1 == 3

if __name__ == "__main__":
    unittest.main()
