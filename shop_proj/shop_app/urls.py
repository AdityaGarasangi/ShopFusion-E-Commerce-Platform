from django.contrib import admin
from django.urls import path
from shop_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("detail/<int:id>", views.detail, name="detail"),
    path("checkout/", views.checkout, name="checkout"),
    path("seller/", views.seller, name="seller"),
    path("createproduct/", views.create_product, name="createproduct"),
    path("edit/<int:id>", views.product_edit, name="edit"),
    path("delete/<int:id>", views.product_delete, name="delete"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("sales/", views.sales, name="sales"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
