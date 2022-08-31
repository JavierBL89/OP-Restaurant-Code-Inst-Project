from . import views
from django.urls import path

urlpatterns = [
    # path ('manage_bookings/', views.manage_bookings.as_view(), name='manage_bookings'),
    path ('profile/', views.Profile.as_view(), name='profile'),
    path ('delete_profile/<int:user_id>/', views.delete_profile, name='delete_profile'),
    path ('cancel_booking/<int:pk>/', views.BookingCancelation.as_view(), name='cancel_booking'),
    path ('cancelation_confirmation/', views.CancelationConfirmation.as_view(), name='cancelation_confirmation'),
    path ('update_confirmation/', views.UpdateConfirmation.as_view(), name='update_confirmation'),
    path ('update_profile/<int:pk>/', views.UpdateProfile.as_view(), name='update_profile'),
]