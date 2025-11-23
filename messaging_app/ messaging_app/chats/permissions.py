from rest_framework.permissions import BasePermission

class IsParticipantOfConversation(BasePermission):
    """
    Only allow participants of a conversation to access it
    """

    def has_object_permission(self, request, view, obj):
        # Ensure the user is authenticated
        if not request.user.is_authenticated:
            return False

        # Check if the user is a participant
        return request.user in obj.participants.all()
