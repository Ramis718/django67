from django.shortcuts import get_object_or_404, render
from . import models, forms
from django.views.generic import ListView, DetailView, CreateView


def home_page(request):
    products = models.Product_in.objects.filter().order_by('-id')
    return render(request, 'product/home_page_in.html', {'product': products})


class HomePageView(ListView):
    template_name = 'product/home_page_in.html'
    queryset = models.Product_in.objects.order_by('-id')

    def get_queryset(self):
        return models.Product_in.objects('-id')

class ProductDatailView(DetailView):
    template_name = 'product/product_datail.html'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.Product_in, id=product_id)

class CustomerCreateViev(CreateView):
    template_name ='product/customer_create.html' 
    form_class = forms.CustomerForm
    success_url ='..'
    queryset = models.Customer_in.objects.all()  

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)

class OrderCreateView(CreateView):
    template_name = 'product/order_create.html'
    form_class = forms.OrderForm
    success_url = '..'
    queryset = models.Order_in.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)             

