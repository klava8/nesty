from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(
        verbose_name='Тег',
        max_length=128,
        unique=True,
    )
    
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=128,
    )
    text = models.TextField(
        verbose_name='Содержание',
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='articles'
    )
    public_data = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now=True,
    )
    tags = models.ManyToManyField(
        to=Tag,
        verbose_name='Теги',
        related_name='articles'
    )
    
    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=128,
    )
    desc = models.CharField(
        verbose_name='Описание',
        max_length=256,
    )
    public_data = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now=True,
    )
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(
        max_length=256,
        verbose_name='текст комментария'
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Имя пользователя',
        related_name='comments'
    )
    article = models.ForeignKey(
        to=Article,
        on_delete=models.CASCADE,
        verbose_name='Комментарииииии',
        related_name='comments'
    )
    
    def __str__(self):
        return f'{self.user.username}({self.article.title})'


class Review(models.Model):
    
    estimation = models.PositiveSmallIntegerField(
        choices=((i, f'{i}') for i in range(1, 11))
    )
    comment = models.TextField(
        verbose_name='Текст комментария'
    )
    product = models.CharField(
        max_length=128,
        verbose_name='я сосал меня ебали ))()!)(*)!(*(Ш(%;?:*())))'
    )
    
    def __str__(self):
        return self.product

    
class Poll(models.Model):
    
    quest = models.CharField(
        max_length=128,
        verbose_name='вопрос'
    )
    
    

class Answer(models.Model):
    
    poll = models.ForeignKey(
        to=Poll,
        on_delete=models.CASCADE,
        related_name='answers',
    )
    rating = models.PositiveIntegerField(
        verbose_name='Рейтинг'
    )
    text = models.CharField(
        verbose_name='Текст',
        max_length=128,
    )

    def __str__(self):
        return self.poll.quest
    
    
class Blog(models.Model):
    
    title = models.CharField(
        max_length=128,
        verbose_name='заголовок'
    )
    text = models.TextField(
        verbose_name='текст блога'
    )
    data = models.DateTimeField(
        auto_now=True,
        verbose_name='дфтф публикации'
    )
    author = models.ForeignKey(
        to = User,
        on_delete=models.CASCADE,
        related_name='blogs'
    )
    
    def __str__(self):
        return self.title