from django.db import models

class Chapter(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=128,
    )
    
    number = models.IntegerField(
        verbose_name='Номер'
    )
    
    text = models.TextField(
        verbose_name='Содержание',
        null=True,
        blank=True,
    )
    
    book = models.ForeignKey(
        to='Book',
        on_delete=models.CASCADE,
        verbose_name='Книга',
        related_name='chapters'
    )
    
    def __str__(self):
        return self.title


class Book(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=128,
        unique=True,
    )
    
    author = models.ForeignKey(
        to='Author',
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='books'
    )
    
    date_publication = models.DateField(
        verbose_name='Дата публикации',
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.name + f"({self.author.name})"


class Author(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=128,
    )
    
    date_of_birth = models.DateField(
        verbose_name='Дата рождения',
    )
    
    date_of_dead = models.DateField(
        verbose_name='Дата смерти',
    )
    
    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=128,
    )
    
    books = models.ManyToManyField(
        to=Book,
        verbose_name='Книги',
        related_name='publishers',
    )
    
    def __str__(self):
        return self.name