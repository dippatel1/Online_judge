from django.urls import path

from . import views
app_name = 'oj'
urlpatterns = [
    path('', views.problems, name='problems'),
      path('problems/<int:problem_id>/', views.detail, name='detail'),
      path('problems/<int:problem_id>/submit/', views.SubmitProblem, name='submit')
]