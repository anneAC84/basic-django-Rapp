
from django.urls import path
from .views import ReceipeListCreateView
from .views import ReceipeRetrieveUpdateDestroyView

urlpatterns = [
path('', ReceipeListCreateView.as_view()), # /books
path('<int:pk>/', ReceipeRetrieveUpdateDestroyView.as_view())
]


