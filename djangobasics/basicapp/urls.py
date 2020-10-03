from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<question_id>/', views.detail, name='detail'),
    #127.0.0.1/basicapp/2
    path('<question_id>/results/', views.results, name='results'),
    path('<question_id>/vote/', views.vote, name='vote'),
]
