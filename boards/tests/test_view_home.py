from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve
from ..views import BoardListView, TopicListView, new_topic
from ..models import Board, Topic, Post
from ..forms import NewTopicForm

class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('boards:home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    '''we are making use of the resolve function. Django uses it to match a requested URL with a list of URLs listed in the urls.py module. This test will make sure the URL /, which is the root URL, is returning the home view.'''

    '''To see more details: python manage.py test boards --verbosity=2'''
    def test_home_url_resolves_home_view(self):
        view = resolve('/boards/')
        self.assertEqual(view.func.view_class, BoardListView)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('boards:board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))