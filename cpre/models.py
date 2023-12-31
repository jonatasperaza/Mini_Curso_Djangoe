from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=40)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Categorias"

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    categorias = models.ManyToManyField(Categoria)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.preco}) ({self.descricao}) ({', '.join(str(categoria) for categoria in self.categorias.all())})"

    
#class Pais(models.Model):
    #nome = models.CharField(max_length=60)
    
    #def __str__(self):
        #return self.nome
    
#class tipoatuacao(models.Model):
    #descricao = models.CharField(max_length=100)
    
    #def __str__(self):
        #return self.descricao

#class Produtora(models.Model):
    #nome = models.CharField(max_length=100)
    #pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    
    #def __str__(self):
        #return f"{self.nome} ({self.pais})"
    
#class Membros(models.Model):
    #nome = models.CharField(max_length=100)
    #DataDeNascimento = models.DateField()
    #pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    
    #def __str__(self):
        #return f"{self.nome} ({self.DataDeNascimento}) ({self.pais})"
    
#class Filme(models.Model):
    #titulo = models.CharField(max_length=100)
    #ano = models.IntegerField()
    #sinopse = models.TextField()
    #duracao = models.TimeField()
    #classificacao = models.IntegerField()
    #Produtora = models.ForeignKey(Produtora, on_delete=models.PROTECT)
    #Categoria = models.ManyToManyField(Categoria)
    
    #def __str__(self):
        #return f"{self.titulo} ({self.ano}) ({self.sinopse}) ({self.duracao}) ({self.classificacao}) ({self.Produtora})"
    
#class Atuacao(models.Model):
    #membro = models.ForeignKey(Membros, on_delete=models.PROTECT)
    #tipoatuacao = models.ForeignKey(tipoatuacao, on_delete=models.PROTECT)
    #personagem = models.CharField(max_length=100, blank=True, null=True)