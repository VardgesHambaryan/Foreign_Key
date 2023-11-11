from django.urls import path
from .views import *


urlpatterns = [
    path('' , HomeListView.as_view() , name='home'),
    path('category/<slug:slug>/' ,  CategoryListView.as_view() , name='cats'),
    path('category/<slug:slug>/<int:id>/' ,  ProductListView.as_view() , name='prod'),
    path('detail/<int:prod_id>' , ProductDetailView.as_view() , name='detail')
]
