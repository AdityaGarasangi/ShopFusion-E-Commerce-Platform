from django.contrib import admin
from django.urls import path
from users import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.user_login, name="login"),
    path("profile", views.user_profile, name="profile"),
    path(
        "logout",
        views.CustomLogoutView.as_view(
            http_method_names=["post", "get", "option"],
        ),
        name="logout",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
