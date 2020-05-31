from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):

    def create(self,validated_data):
        apelido = validated_data.get('apelido')
        username = validated_data.get('username')
        password = validated_data.get('password')

        usuario = Usuario(apelido=apelido,username=username,password=password)
        usuario.save()
        return usuario

    def update(self,instance,validated_data):
        instance.apelido = validated_data.get('apelido', instance.apelido)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

    class Meta:
        model = Usuario
        fields = ('id','username','apelido','password')


class UsuarioListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('id','username','apelido','password')

class UsuarioIDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('id','username','apelido','password')

class AutorSerializer(serializers.ModelSerializer):
    
    def create(self,validated_data):
        nome_autor = validated_data.get('nome_autor')
        autor = Autor(nome_autor=nome_autor)
        autor.save()
        return autor

    def update(self,instance,validated_data):

        instance.nome_autor = validated_data.get('nome_autor',instance.nome_autor)
        instance.save()

    class Meta:
        model = Autor
        fields = "__all__"

class AutorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Autor
        fields = "__all__"

class AutorIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"

class LivroSerializer(serializers.ModelSerializer):

    def create(self,validated_data):

        return Livro.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.titulo = validated_data.get('titulo',instance.titulo)
        instance.autor = validated_data.get('autor',instance.autor)
        instance.pontuacao_maxima = validated_data.get('pontuacao_maxima',instace.pontuacao_maxima)
        instance.save()
        return instance

    class Meta:
        model = Livro
        fields = '__all__'