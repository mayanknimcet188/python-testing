from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test Title', 'Test Content')

        self.assertEqual('Test Title', p.title)
        self.assertEqual('Test Content', p.content)

    def test_post_json(self):
        p = Post('Flask', 'Learn Flask')
        expected_json = {'title': 'Flask', 'content': 'Learn Flask'}

        self.assertDictEqual(expected_json, p.json())
