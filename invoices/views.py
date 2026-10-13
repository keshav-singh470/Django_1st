from django.utils import timezone
from rest_framework import viewsets, permissions

from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    permission_classes = [permissions.AllowAny]  # baad me IsAuthenticated kar dena

    def get_queryset(self):
        # Sirf wo records jo delete nahi hue
        return Person.objects.filter(is_deleted=False).order_by('-id')

    def perform_destroy(self, instance):
        # SOFT DELETE: DB se row delete nahi hoti, sirf mark hoti hai
        instance.is_deleted = True
        instance.deleted_at = timezone.now()
        instance.save()