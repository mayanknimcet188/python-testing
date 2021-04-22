from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def setUp(self):
        self.b = Blog('Blog', 'Mayank')

    def test_create_blog(self):
        self.assertEqual('Blog', self.b.title)
        self.assertEqual('Mayank', self.b.author)
        self.assertListEqual([], self.b.posts)

    def test_repr(self):
        self.assertEqual(self.b.__repr__(), 'Blog by Mayank (0 posts)')

    def test_repr_multiple_posts(self):
        self.b.posts = ['Test Post']

        self.assertEqual(self.b.__repr__(), 'Blog by Mayank (1 posts)')
