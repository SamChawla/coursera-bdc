from django.urls import reverse
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.utils import timezone
import json

from restaurant.models import Booking
from restaurant.serializers import BookingSerializer

# Write Test Cases for Booking ViewSet using these fields 
# name = models.CharField(max_length=255)
# number_of_guests = models.IntegerField()
# booking_date =models.DateTimeField()

class BookingViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="testuser", email="testuser@littlelemon.com", password="testuser")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.booking = Booking.objects.create(
            name="testuser", number_of_guests=2, booking_date=timezone.now())
        self.booking.save()

    def test_get_all_bookings(self):
        response = self.client.get(reverse("booking-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_single_booking(self):
        response = self.client.get(reverse("booking-detail", args=[self.booking.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.booking.name)
        self.assertEqual(response.data["number_of_guests"], self.booking.number_of_guests)
        self.assertEqual(response.data["booking_date"], self.booking.booking_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
    
    def test_create_booking(self):
        data = {
            "name": "testuser2",
            "number_of_guests": 4,
            "booking_date": timezone.now()
        }
        response = self.client.post(reverse("booking-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["number_of_guests"], data["number_of_guests"])
        self.assertEqual(response.data["booking_date"], data["booking_date"].strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
    
    def test_update_booking(self):
        data = {
            "name": "testuser2",
            "number_of_guests": 4,
            "booking_date": timezone.now()
        }
        response = self.client.put(reverse("booking-detail", args=[self.booking.id]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["number_of_guests"], data["number_of_guests"])
        self.assertEqual(response.data["booking_date"], data["booking_date"].strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
    
    def test_delete_booking(self):
        response = self.client.delete(reverse("booking-detail", args=[self.booking.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 0)
