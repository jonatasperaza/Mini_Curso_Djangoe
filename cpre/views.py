from rest_framework import generics
from .models import Produto
from .serializers import ProdutoSerializer

class ProdutoListView(generics.ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
