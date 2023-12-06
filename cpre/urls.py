from django.urls import path
from .views import ProdutoListView

urlpatterns = [
    path('api/produtos/', ProdutoListView.as_view(), name='produto-list'),
    
]
