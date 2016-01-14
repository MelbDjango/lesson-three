from django.test import TestCase, Client


class LessonOneTests(TestCase):

    def test_entries_available(self):
        c = Client()
        response = c.get('/entries/')
        self.assertEqual(response.status_code, 200)
