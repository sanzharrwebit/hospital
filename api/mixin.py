from rest_framework import viewsets

from .permissions import RoleBasedPermissionsMixin, HasPermissionByAuthenticatedUserRole


class HospitalGenericViewSet(
    viewsets.GenericViewSet,
    RoleBasedPermissionsMixin,
):
    permission_classes = [HasPermissionByAuthenticatedUserRole]

    # pagination_class = [CustomPagination]
