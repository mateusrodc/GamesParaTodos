from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.
class UsuarioListAll(generics.ListAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioListSerializer

class UsuarioID(generics.RetrieveAPIView):

    serializer_class = UsuarioIDSerializer
    queryset = Usuario.objects.all()

class UsuarioList(generics.ListCreateAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def create(self,request,*args,**kwargs):
        usuario = Usuario.objects.filter(username=request.data['username'])
        if usuario:
            return Response({'mensagem': 'Usuário já cadastrado'}, 403)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UsuarioDetalhes(generics.RetrieveUpdateDestroyAPIView):
    queryset= Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def update(self,request,*args,**kwargs):
        usuario = Usuario.objects.filter(username=request.data['username'], apelido=request.data['apelido'],password=request.data['password'])
        if usuario:
            return Response({'mensagem': 'Usuário já cadastrado'}, 403)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def delete(self,request,*args,**kwargs):
        #usuario = Usuario.objects.get(username=request.data['username'])
        return self.destroy(request, *args, **kwargs)

class AutorListAll(generics.ListAPIView):
    
    queryset = Autor.objects.all()
    serializer_class = AutorListSerializer

class AutorID(generics.RetrieveAPIView):
    serializer_class = AutorIDSerializer
    queryset = Autor.objects.all()

class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    def create(self,request,*args,**kwargs):
        autor = Autor.objects.filter(nome_autor=request.data['nome_autor'])
        if autor:
            return Response({'mensagem': 'Autor já cadastrado'}, 403)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class AutorDetalhes(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def update(self,request,*args,**kwargs):
        autor = Autor.objects.filter(autor_nome=request.data['autor_nome'])
        if autor:
            return Response({'mensagem': 'Autor já cadastrado'},403)
        partial = kwargs.pop('partial',False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data,partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def delete(self,request,*args,**kwargs):

        return self.destroy(request,*args,**kwargs)

class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.filter().order_by('titulo')
    serializer_class = LivroSerializer

class LivroDetalhes(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def delete(self,request,*args,**kwargs):

        self.destroy(request,*args,**kwargs)
        return Response({'mensagem':'Livro excluido'},200)