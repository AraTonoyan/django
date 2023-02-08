from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import HomeSlide, Product, Logo, ShortAbout, CallToAction, ProductPageHead, AboutUs, AboutPageHead


# Create your views here.

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        shortAbout = ShortAbout.objects.all()
        products = Product.objects.all()
        homeslider = HomeSlide.objects.all()
        logo = Logo.objects.all()
        callToAction = CallToAction.objects.all()
        return render(request, self.template_name,
                      context={'homeslider': homeslider, 'products': products, 'logo': logo, 'shortAbout': shortAbout,
                               'callToAction': callToAction})


class AboutListView(ListView):
    template_name = 'about.html'

    def get(self, request):
        aboutUs = AboutUs.objects.all()
        aboutPageHead = AboutPageHead.objects.all()
        logo = Logo.objects.all()
        return render(request, self.template_name, context={'logo': logo, 'aboutUs': aboutUs, 'aboutPageHead': aboutPageHead})


class ContactListView(ListView):
    template_name = 'contact.html'

    def get(self, request):
        logo = Logo.objects.all()
        return render(request, self.template_name, context={'logo': logo})


class ProductsListView(ListView):
    template_name = 'products.html'

    def get(self, request):
        products = Product.objects.all()
        logo = Logo.objects.all()
        productPageHead = ProductPageHead.objects.all()
        return render(request, self.template_name,
                      context={'products': products, 'logo': logo, 'productPageHead': productPageHead})
