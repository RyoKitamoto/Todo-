from django.urls import path
from .views import TodoView,TodoDetailView,TodoCreateView,TodoDeleteView,TodoUpdateView

urlpatterns=[
    path('',TodoView.as_view(),name='list'),
    path('detail/<pk>/',TodoDetailView.as_view(),name='detail'),
    path('create/',TodoCreateView.as_view(),name='create'),
    path('delete/<pk>',TodoDeleteView.as_view(),name='delete'),
    path('update/<pk>',TodoUpdateView.as_view(),name='update'),
]
