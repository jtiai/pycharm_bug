from django.test import TestCase


class SmokeTestTestCase(TestCase):
    def test_smoke(self):
        self.assertEqual("A", "A")

    def test_some_two(self):
        self.assertNotEqual("A", "B")
