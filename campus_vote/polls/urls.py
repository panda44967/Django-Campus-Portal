from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.QuestionListView.as_view(), name='home'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('stats/', views.stats_view, name='stats'),
]
