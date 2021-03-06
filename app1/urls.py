from django.urls import include, path
from django.views.generic import RedirectView
from app1.views import BookingCreateView, BookingUpdateView, App1BookingConfirmationView

app_name = 'app1'

urlpatterns = [
    path('create/', BookingCreateView.as_view(), name='app1_create'),
    path('update/', BookingUpdateView.as_view(), name='app1_update'),
    path('confirm/', App1BookingConfirmationView.as_view(), name='confirm'),
]