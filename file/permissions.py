import authority
from authority import permissions
from django.contrib.flatpages.models import FlatPage

class FlatPagePermission(permissions.BasePermission):
    label = 'flatpage_permission'
    checks = ('review',)

authority.utils.register(FlatPage, FlatPagePermission)