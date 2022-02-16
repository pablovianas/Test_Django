
from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)


    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


    def __str__(self) -> str:
        return self.name


class Books(models.Model):

 
    title = models.CharField(max_length=20, null=False, blank=False)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    summary = models.TextField(null=False, blank=False)
    isbn = models.CharField(max_length=13, null=False, blank=False)
    genre = models.ManyToManyField(Genre)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self) -> str:
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self) -> str:
        return self.name
