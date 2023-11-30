from django.urls import path
from .views import my_template
from .views import MyModelCreateView
from .views import MyModelUpdateView
from .views import MyModelDetailView
urlpatterns = [
 path('my_template/', my_template.as_view(), name='my_template_view'),
 path('my_model_create/',MyModelCreateView.as_view(),name='my_model_create'),
 path('my_model/<int:pk>/update/',MyModelUpdateView.as_view(),name='my_model_update'),
 path('my_model/<int:pk>/', MyModelDetailView.as_view(), name='my_model_detail'),
]