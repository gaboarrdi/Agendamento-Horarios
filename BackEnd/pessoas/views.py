from rest_framework import viewsets
from pessoas.models import Pessoa
from pessoas.serializer import PessoaSerializer

class PessoasViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
