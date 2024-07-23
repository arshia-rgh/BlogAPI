from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from .models import Post, Comment


class PostModelTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='test1')
        self.post1 = Post.objects.create(author=self.user1, title='post1', status=1)
        self.comment1 = Comment.objects.create(auther=self.user1, posts=self.post1, status=1, approved=True)
        self.comment2 = Comment.objects.create(auther=self.user1, posts=self.post1, status=0, approved=False)

    def test_custom_model_manager(self):
        approved_comments = Comment.objects.approved()
        unapproved_comments = Comment.objects.unapproved()
        active_comments = Comment.objects.active()
        inactive_comments = Comment.objects.inactive()

        # Check if comment1 is in approved and active comments
        self.assertIn(self.comment1, approved_comments)
        self.assertIn(self.comment1, active_comments)

        # Check if comment2 is in unapproved and inactive comments
        self.assertIn(self.comment2, unapproved_comments)
        self.assertIn(self.comment2, inactive_comments)