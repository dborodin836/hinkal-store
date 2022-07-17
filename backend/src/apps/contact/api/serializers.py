from rest_framework import serializers

from src.apps.contact.models import Contact


class ContactListSerializer(serializers.ModelSerializer):
    """List of all contacts"""

    class Meta:
        model = Contact
        fields = ("id", "subject", "message")


class ContactDetailSerializer(serializers.ModelSerializer):
    """Detailed ContactMe"""

    class Meta:
        model = Contact
        fields = ("id", "name", "subject", "email", "message", "created_at")
