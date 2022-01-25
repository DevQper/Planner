from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.TaskView.as_view(), name="most_page"),
    # path('accounts', include('allauth.urls')),
    path("create", views.AddTask.as_view(), name="add_task"),
    path("delete/<int:pk>", views.Delete.as_view(), name="delete_task"),
    path("completeness/<int:pk>", views.Completeness.as_view(), name="complete_task"),
    path("my_completeness/<int:pk>", views.MyCompleteness.as_view(), name="my_complete_task"),
    path("history", views.TaskHistory.as_view(), name="history_tasks"),
    path("profile", views.Profile.as_view(), name="user_profile"),
    path("new_blogs", views.BlogView.as_view(), name="new_blog"),
    path("review/<int:pk>", views.AddReview.as_view(), name="add_review"),
]
