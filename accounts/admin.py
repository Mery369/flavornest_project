from django.contrib import admin
from .models import UserProfile
from .models import CollaborateRequest

admin.site.register(UserProfile)
@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)
    # Restrict the queryset so only requests related to the logged-in user are visible
    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     if not request.user.is_superuser:
            # Filter so that users can only see their own requests (not others')
        #     queryset = queryset.filter(user=request.user)
        # return queryset

