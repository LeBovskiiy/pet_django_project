from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageViews.as_view(), name='home'),
    path('search/', SearchResultView.as_view(), name='search-result'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('basket/', BasketView.as_view(), name='basket'),
    path('cart_action/<int:product_id>/<str:action>/', CartActionView.as_view(), name='cart-action'),
    path('js_res/', js_res, name='js_res'),
]
