from django.db import models


class Course(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    dtBegin = models.DateField('Data de início', null=True, blank=True)

    image = models.ImageField(
        upload_to='courses/imagens', verbose_name='Imagem'
    )

    createAt = models.DateTimeField(
        'Criado em', auto_now_add=True
    )

    updateAt = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

