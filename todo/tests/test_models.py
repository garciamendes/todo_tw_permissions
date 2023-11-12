# Project
from core.tests.login import CoreTestCase

# Local
from todo.models import Task
from todo.models import CommentTask


class TaskTestCase(CoreTestCase):
    def setUp(self):
        self.user = self.create_user()

    def test_should_be_possible_to_create_new_task(self):
        task = Task.objects.create(
            title='teste case',
            description='teste case description',
            user=self.user
        )

        self.assertIsNotNone(task.id)
        self.assertEqual(task.title, 'teste case')
        self.assertEqual(task.user, self.user)

    def test_should_not_be_possible_to_create_a_new_task_without_passing_the_user(self):
        with self.assertRaises(Exception):
            Task.objects.create(
                title='teste case',
                description='teste case description'
            )

    def test_should_not_be_possible_to_create_a_new_task_without_passing_the_title(self):
        with self.assertRaises(Exception):
            Task.objects.create(
                title=None,
                description='teste case description',
                user=self.user
            )


class CommentTaskTestCase(CoreTestCase):
    def setUp(self):
        self.user = self.create_user()
        self.task = Task.objects.create(title='teste case', user=self.user)

    def test_should_be_possible_to_create_new_comment_to_task(self):
        comment_instance = CommentTask.objects.create(
            comment='teste case comment',
            task=self.task
        )

        self.assertIsNotNone(comment_instance.id)
        self.assertEqual(comment_instance.comment, 'teste case comment')
        self.assertEqual(comment_instance.task.id, self.task.id)

    def test_should_not_be_possible_to_create_new_comment_to_without_task(self):
        with self.assertRaises(Exception):
            CommentTask.objects.create(
                comment='teste case comment',
                task=None
            )
