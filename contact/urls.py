from . import views
from django.urls import path

urlpatterns = [
    path ('contact/', views.Contact.as_view(), name='contact'),
]