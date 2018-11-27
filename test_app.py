from unittest import TestCase
from app import app
from desserts import dessert_list, Dessert


class FlaskTests(TestCase):
    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def tearDown(self):
        """reset the dessert_list after each test.
        Only an issue because we don't know about databases yet."""

        cookie = Dessert(1, "Chocolate chip cookie",
                         "C is for cookie, that's good enough for me", 200)
        sundae = Dessert(2, "Banana split",
                         "I'm going to eat all of my feelings", 600)
        donut = Dessert(3, "Glazed Donut", "Perfect with a cup of coffee", 300)
        dessert_list.desserts = [cookie, sundae, donut]
        dessert_list.next_id = 4

    def test_homepage(self):
        """Make sure homepage has correct routing information"""

        with self.client:
            response = self.client.get('/')
            # test that the status code is a 200
            self.assertEqual(response.status_code, 200)
            # test that there's a table in the response data
            self.assertIn(b'<table>', response.data)
            # test that the description for each endpoint is in the response data
            self.assertIn(b'JSON data of all desserts', response.data)
            self.assertIn(
                b'Adds a new dessert to our list (returns data on the new dessert)',
                response.data)
            self.assertIn(b'JSON data on a single dessert', response.data)
            self.assertIn(
                b'Update an existing dessert (returns data on the updated dessert)',
                response.data)
            self.assertIn(
                b'Removes a dessert from our list (returns data on the deleted dessert)',
                response.data)
            # e.g. 'JSON data of all desserts' should be in the response data,
            # 'Adds a new dessert to our list' should be in the response data,

            # etc.
