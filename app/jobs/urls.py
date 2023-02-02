from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApplyJobView.as_view(), name='job_apply'),
]
