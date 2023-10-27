from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core import serializers
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

from .serializers import BookingSerializer, MenuSerializer
from .models import Booking, Menu


# API views for Menu and Booking
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


# Views for Menu and Booking


def index(request):
    return render(request, "index.html", {})


def about(request):
    return render(request, "about.html")


def reservations(request):
    bookings = Booking.objects.all()
    booking_json = serializers.serialize("json", bookings)
    return render(request, "reservations.html", {"bookings": booking_json})
