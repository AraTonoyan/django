from django.db import models


# Create your models here.

class HomeSlide(models.Model):
    title = models.CharField('Home Slide title', max_length=10)
    name = models.CharField('Home Slide name', max_length=30)
    img = models.ImageField('Home Slide Img', upload_to='media')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'HomeSlider'
        verbose_name_plural = 'HomeSliders'


class Product(models.Model):
    name = models.CharField('Product Name', max_length=35)
    short_description = models.CharField('Product Short Description', max_length=120)
    description = models.TextField('Product Description')
    price = models.IntegerField('Product Description')
    img = models.ImageField('Product Image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Logo(models.Model):
    name = models.CharField('Page Name', max_length=40)

    def __str__(self):
        return self.name


class ShortAbout(models.Model):
    title = models.CharField('Main title', max_length=35)
    second_title = models.CharField('Second title', max_length=45)
    text = models.TextField('Short about')
    img = models.ImageField('Product Image', upload_to='media')
    button = models.CharField('Button text', max_length=25)

    def __str__(self):
        return self.title


class CallToAction(models.Model):
    title = models.CharField('Title', max_length=35)
    text = models.CharField('Text', max_length=120)
    button = models.CharField('Button text', max_length=25)

    def __str__(self):
        return self.title


class ProductPageHead(models.Model):
    redTitle = models.CharField('First Title', max_length=30)
    whiteTitle = models.CharField('Second Title', max_length=30)

    def __str__(self):
        return self.redTitle


class AboutPageHead(models.Model):
    redTitle = models.CharField('First Title', max_length=30)
    whiteTitle = models.CharField('Second Title', max_length=30)

    def __str__(self):
        return self.redTitle


class AboutUs(models.Model):
    firstTitle = models.CharField('Main Title', max_length=30)
    secondTitle = models.CharField('Title', max_length=30)
    text = models.TextField('Text')
    img = models.ImageField('AboutUs Img', upload_to='media')

    def __str__(self):
        return self.firstTitle

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'
