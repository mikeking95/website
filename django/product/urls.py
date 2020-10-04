from django.urls import path
from .views import ProductPageView

app_name = "product"
urlpatterns = [
    path('', ProductListView.as_view(), name="product_list")
    path('<int:pk>/', ProductPageView.as_view(), name="product_detail"),
]
