from unittest import TestCase
from desserts import Dessert, DessertList


class DessertListTests(TestCase):
    def setUp(self):
        self.sample_list = DessertList()

    def test_init(self):
        """Test the __init__ method for DessertList"""

        self.assertEqual(self.sample_list.desserts, [])
        self.assertEqual(self.sample_list.next_id, 1)

    def test_repr(self):
        """Test the __repr__ method for DessertList"""

        self.assertEqual(self.sample_list.__repr__(),
                         "<DessertList: desserts=[] next_id=1>")

    def test_add(self):
        """Test the add method for DessertList"""

        # append new dessert
        self.sample_list.add(
            name="Coconut Cream Pie", description="Delish", calories=400)

        # get dessert that was appended
        new_dessert = self.sample_list.desserts[0]

        # test dessert appended is correct and in the right place
        self.assertIn(new_dessert, self.sample_list.desserts)

        # check that increment increased
        self.assertEqual(self.sample_list.next_id, 2)

    def test_serialize(self):
        """Test the serialize method for DessertList"""

        self.assertEqual(self.sample_list.serialize(), {
            "desserts": [],
            "next_id": 1
        })
