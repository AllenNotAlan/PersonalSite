from django.urls import path
from .views import (
    ProjectListView, 
    ProjectDetailView, 
    ProjectCreateView, 
    ProjectUpdateView,
    ProjectDeleteView
)
from . import views

urlpatterns = [
    path('', ProjectListView.as_view(), name='myHome-home'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    # path('about/', views.about_view, name='myHome-about'),
    # path('education/', views.education_view, name='myHome-education'),
    path('other/', views.other_view, name='myHome-other'),
    path('contact/', views.contact_view, name='myHome-contact'),
]

# <app>/<model>_<viewtype>.html