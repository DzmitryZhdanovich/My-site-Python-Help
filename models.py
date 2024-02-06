from django.db import models

class Author(models.Model):

    name = models.CharField(max_length=150)
    email = models.EmailField(primary_key=True)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    # объект для выбора нескольких вариантов значений в виде списка кортежей
    # кортежи представляют собой пары ключ-значение
    POST_TYPES = [('c', "copyright"), ('p', "public license")]

    title = models.CharField(max_length=150, blank=True)
    content = models.TextField()
    post_type = models.CharField(max_length=1, choices=POST_TYPES)
    issued = models.DateTimeField()
    # upload_to - путь на файловой системе, куда должны складываться файлы изображений после загрузки
    image = models.ImageField(upload_to='uploads')

    author = models.ForeignKey('Author', on_delete=models.CASCADE)





