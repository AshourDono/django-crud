from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    rate = [('U8', 'under 8'), ('U15', '8-15'), ('+18', 'adults')]

    name = models.CharField(max_length=100, null=True)
    publish_date = models.DateField(db_column='Published At', null=True)
    add_to_site_at = models.DateField(
        auto_created=True, db_column='Added At', null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    appropriate = models.CharField(
        max_length=3, choices=rate, default='U8', null=True)
    image = models.FileField(
        upload_to='book_list/static/book_list/images', null=True, blank=True, default='book_list/static/book_list/images/1.jpg')

    def __str__(self) -> str:
        return self.name
