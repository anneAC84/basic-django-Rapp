
from django.urls import path
from .views import ReceipeListCreateView

urlpatterns = [
path('', ReceipeListCreateView.as_view()) # /books
]


