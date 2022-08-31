from . import views
from django.urls import path

urlpatterns = [
    path ('', views.HomePage.as_view(), name='home'),
    path ('booking_search_results', views.ResultsBookingSearch.as_view(), name='booking_search'),
    path ('cancelations', views.BookingSearch.as_view(), name='cancelations'),
    path ('cancelation_confirmation', views.CancelationConfirmation.as_view(), name='cancelation_confirmation'),
    path ('reservation_confirmation', views.FormView.as_view(), name='booking_request'),  
    path ('reservation_confirmation', views.ReservationConfirmation.as_view(), name='reservation_confirmation'),  
]