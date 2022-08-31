from . import views
from django.urls import path

urlpatterns = [
    path ('', views.HomePage.as_view(), name='home'),
    path ('booking_request/', views.FormView.as_view(), name='booking_request'),  
    path ('reservation_confirmation/', views.ReservationConfirmation.as_view(), name='reservation_confirmation'),  
]