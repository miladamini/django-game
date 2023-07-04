from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class blogMolde(models.Model):
    title = models.CharField(max_length=1000, verbose_name="تایتل")
    img = models.ImageField(verbose_name='عکس', upload_to='img')
    body = RichTextField()

    class Meta:
        verbose_name = 'وبلاگ'
        verbose_name_plural = 'وبلاگ ها'

    def __str__(self):
        return self.title
