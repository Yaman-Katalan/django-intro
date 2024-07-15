from django.contrib import admin
from django.urls import path
from .views import HomePageView, AboutPageView, ServicesPageView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name="home"),
    path('about-us', AboutPageView.as_view(), name="about"),
    path('our-services', ServicesPageView.as_view(), name="services"),
    # path('contact',)
]
