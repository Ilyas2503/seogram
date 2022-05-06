from django.db import models


class Post(models.Model):
    '''
    author
    pud_date
    image
    description
    author_text
    category
    '''
    author = models.CharField(max_length=50, verbose_name='Автор')
    pud_date = models.DateField(auto_now=True, verbose_name='Дата публикации')
    image = models.ImageField(upload_to='Post/%m/%d', blank=True)
    description = models.TextField()
    author_text = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.author


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
