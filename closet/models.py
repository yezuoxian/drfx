from django.db import models

GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
CATEGORY_CHOICES = (('C', 'Clothe'), ('P', 'Pants'),)


class UserProfile(models.Model):
    nickname = models.CharField(max_length=100)
    weight = models.FloatField()
    height = models.FloatField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth = models.DateField()
    age = models.IntegerField()

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"

    def __unicode__(self):
        return self.nickname

    def __str__(self):
        return self.nickname


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='img')
    hyperlink = models.URLField()

    class Meta:
        verbose_name = "产品信息"
        verbose_name_plural = "产品信息"

    def __unicode__(self):
        return self.product_name

    def __str__(self):
        return self.product_name


class Collocation(models.Model):
    collocation = models.CharField(max_length=100)

    class Meta:
        verbose_name = "服饰搭配"
        verbose_name_plural = "服饰搭配"
