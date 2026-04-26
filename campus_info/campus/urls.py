from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'campus'

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('clubs/', views.ClubsView.as_view(), name='clubs'),
    path('schedule/', views.schedule_view, name='schedule'),
    path('faq/', views.faq_view, name='faq'),
    path('about/', views.AboutView.as_view(), name='about'),
]
