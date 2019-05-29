from django.urls import path
from rest_framework.routers import DefaultRouter

from .api_views import ChoiceList, CreateVote, PollViewSet, \
    UserCreate, LoginView

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

app_name = 'polls'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserCreate.as_view(), name='user_create'),

    # These URLs can be used for DRF's APIView.
    # path('polls/', PollList.as_view(), name='polls_list'),
    # path('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail'),

    # path('choices/', ChoiceList.as_view(), name='choice_list'),
    # path('vote/', CreateVote.as_view(), name='create_vote'),
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/',
         CreateVote.as_view(), name='create_vote'),
]

urlpatterns += router.urls
