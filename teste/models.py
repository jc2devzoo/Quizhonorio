from django.db import models



class Tema(models.Model):
    id_tema = models.CharField(max_length=100)
    

    def  __str__(self):

        return self.id_tema
    


class Pergunta(models.Model):

    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)

    pergunta = models.CharField(max_length=100)

    resposta = models.IntegerField()
    prim_res = models.CharField(max_length=100)
    sec_res = models.CharField(max_length=100)
    ter_res = models.CharField(max_length=100)
    quar_res = models.CharField(max_length=100 , blank=True)
    quin_res = models.CharField(max_length=100 , blank= True)
    
    def __str__(self):
        return self.pergunta
    