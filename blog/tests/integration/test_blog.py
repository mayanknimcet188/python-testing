from unittest import TestCase
from blog import Blog
from post import Post


class BlogTest(TestCase):
    def test_create_post(self):
        b = Blog('Blog', 'Mayank')
        b.create_post('First Post', 'This is a test post')
        self.assertIsInstance(b.posts[0], Post)
        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'First Post')
        self.assertEqual(b.posts[0].content, 'This is a test post')

    def test_json_no_posts(self):
        b = Blog('Blog', 'Mayank')
        expected = {'title': 'Blog', 'author': 'Mayank', 'posts': []}
        self.assertDictEqual(expected, b.json())

    def test_json(self):
        b = Blog('Blog', 'Mayank')
        b.create_post('First Post', 'This is a test post')

        expected = {
            'title': 'Blog',
            'author': 'Mayank',
            'posts': [
                {
                    'title': 'First Post',
                    'content': 'This is a test post'
                }
            ]
        }
        self.assertDictEqual(expected, b.json())
