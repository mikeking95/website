from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Product

# class SimpleExView(TemplateView):
        
#     # TemplateResponseMixin
#     template_name = "simple_cbv.html"
    
#     #ContentMixin
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['shop'] = "Knifekits.com"
#         return context

class ProductListView(ListView):
    model = Product
    template_name = "product/product_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sku']="TEST-1"
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context

def product_detail(request, product):
    product = get_object_or_404(Product, pk=product)
    return render(request, 'product_detail.html', {'product': product})
