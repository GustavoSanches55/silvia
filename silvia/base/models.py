from django.db import models

# Create your models here.


class usuario(models.Model):
    login = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)


class instituicao(models.Model):
    nome_instituicao = models.CharField(max_length=50)
    id_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)


class aluno(models.Model):
    nome_aluno = models.CharField(max_length=50)
    genero_aluno = models.CharField(max_length=20, null=True, blank=True)
    data_nascimento_aluno = models.DateField()
    id_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    id_insituicao = models.ForeignKey(instituicao, on_delete=models.CASCADE)


class turma(models.Model):
    curso = models.CharField(max_length=50)
    periodo = models.IntegerField()
    tag = models.CharField(max_length=1)


class professor(models.Model):
    nome_professor = models.CharField(max_length=50)
    genero_professor = models.CharField(max_length=20, null=True, blank=True)
    data_nascimento_professor = models.DateField()
    id_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    id_insituicao = models.ForeignKey(instituicao, on_delete=models.CASCADE)


class assunto(models.Model):
    nome_assunto = models.CharField(max_length=50)


class sentimentos(models.Model):
    nome_sentimentos = models.CharField(max_length=50)
    carater = models.CharField(max_length=10)


class disciplina(models.Model):
    id_professor = models.ForeignKey(professor, on_delete=models.CASCADE)
    id_assunto = models.ForeignKey(assunto, on_delete=models.CASCADE)
    id_turma = models.ForeignKey(turma, on_delete=models.CASCADE)
    carga_horaria = models.IntegerField()


class grade(models.Model):
    id_aluno = models.ForeignKey(aluno, on_delete=models.CASCADE)
    id_disciplina = models.ForeignKey(disciplina, on_delete=models.CASCADE)


class avaliacao(models.Model):
    id_sentimento = models.ForeignKey(sentimentos, on_delete=models.CASCADE)
    id_aluno = models.ForeignKey(aluno, on_delete=models.CASCADE)
    id_disciplina = models.ForeignKey(
        disciplina, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=500, null=True, blank=True)
    conhecimento = models.IntegerField()
    intensidade = models.IntegerField()
    data = models.DateField()
