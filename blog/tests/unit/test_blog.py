from unittest import TestCase
from blog import Blog
from post import Post

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Blog','Mayank')

        self.assertEqual('Blog',b.title)
        self.assertEqual('Mayank',b.author)
        self.assertListEqual([],b.posts)

    def test_repr(self):
        b = Blog('Blog','Mayank')

        self.assertEqual(b.__repr__(),'Blog by Mayank (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Blog','Mayank')
        b.posts = ['Test Post']

        self.assertEqual(b.__repr__(),'Blog by Mayank (1 posts)')
