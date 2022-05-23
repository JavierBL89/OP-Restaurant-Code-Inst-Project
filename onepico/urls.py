from . import views
from django.urls import path

urlpatterns = [
    path ('', views.HomePage.as_view(), name='home'),
    path ('cancelations', views.BookingSearch.as_view(), name='booking_search'),
    path ('cancel booking/<int:pk>', views.BookingCancelation.as_view(), name='cancel_booking'),
    path ('cancelation-confirmation', views.CancelationConfirmation.as_view(), name='cancelation_confirmation'),
    path ('reservation-confirmation', views.FormView.as_view(), name='booking_request'),  
    path ('reservation_confirmation', views.ReservationConfirmation.as_view(), name='reservation_confirmation'),  
]