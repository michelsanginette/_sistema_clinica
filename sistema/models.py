# Importação do módulo models que traz métodos do banco de dados.
from django.db import models

# Importação do módulo timezone que traz datas e horários
from django.utils import timezone

# Aqui fica o model do paciente
class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    criacao_data = models.DateTimeField(default=timezone.now)
    mensagem = models.TextField(blank=True)
    ativo = models.BooleanField(default=False)
    imagem = models.ImageField(upload_to='img/%Y/%m/', blank=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

# Aqui fica o model da especialidade    
class Especialidade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
# Aqui fica o model do médico   
class Medico(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    crm = models.CharField(max_length=6)
    email = models.EmailField()
    criacao_data = models.DateTimeField(default=timezone.now)
    telefone = models.CharField(max_length=20)
    imagem = models.ImageField(upload_to='img/%Y/%m/', blank=True)
    ativo = models.BooleanField(default=False)
    mensagem = models.TextField(blank=True)
    especialidade_id = models.ForeignKey(Especialidade, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    

# Aqui fica o model da consulta
class Consulta(models.Model):
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    medico_id = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True)
    horario = models.DateTimeField(default=timezone.now)
    observacao = models.TextField(blank=True)
    status = models.CharField(default='A', max_length=1, choices=(('A', 'AGENDADA'), ('C', 'CANCELADA'), ('R', 'REALIZADA'), ('M', 'CONFIRMADA')))

    def __str__(self):
        return f'Consulta {self.status} com sucesso.'