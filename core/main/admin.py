from django.contrib import admin
from .models import HomeSlide, Product, Logo, ShortAbout, CallToAction, ProductPageHead, AboutPageHead, AboutUs
# Register your models here.

admin.site.register(HomeSlide)
admin.site.register(Product)
admin.site.register(Logo)
admin.site.register(ShortAbout)
admin.site.register(CallToAction)
admin.site.register(ProductPageHead)
admin.site.register(AboutPageHead)
admin.site.register(AboutUs)