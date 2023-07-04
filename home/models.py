from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
class gameMode(models.Model):
    title = models.CharField(max_length=400, verbose_name='اسم بازی')
    img = models.ImageField(verbose_name='عکس', upload_to='img')
    my_id = models.IntegerField(default=0,verbose_name='شماره')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی '
        verbose_name_plural = 'دسته بندی ها'


class lDitaile(models.Model):
    title = models.CharField(max_length=300, verbose_name='تایتل')
    category = models.ForeignKey(gameMode, models.CASCADE, verbose_name='دسته بندی')
    body = RichTextField(verbose_name='توصیحات', null=True, blank=True)
    img1 = models.URLField(verbose_name='عکس یک', null=True, blank=True)
    img2 = models.URLField(verbose_name='عکس دو', null=True, blank=True)
    img3 = models.URLField(verbose_name='عکس سه', null=True, blank=True)
    film = models.URLField(verbose_name="فیلم", null=True, blank=True)
    Money = models.IntegerField(default=0, verbose_name='قیمت')
    link = models.CharField(max_length=1000, verbose_name='لینک', unique=True)
    alt = models.CharField(max_length=300, verbose_name='توضیحات عکس', null=True, blank=True)
    like = models.IntegerField(default=0, verbose_name='تعداد لایک')

    class Meta:
        verbose_name = 'بازی '
        verbose_name_plural = 'بازی ها '
