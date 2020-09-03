from django.conf.urls import url
from django.urls import path

from . import views
from django.contrib.auth.views import LoginView

app_name = 'polls'
urlpatterns = [

    #example: /polls/
    path('', views.IndexView, name='index'),
    #example: /polls/5
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #example: /polls/5/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #example: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),


]
