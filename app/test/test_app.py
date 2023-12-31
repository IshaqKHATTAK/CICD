import unittest
from app import views


class SimpleRequestTest(unittest.TestCase):
    """
    This class is used for request based unit tests
    """
    def setUp(self):
        views.testing = True
        self.views = views.test_client()

    def test_main_page(self):
        response = self.views.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main(verbosity=2)
