from rest_framework.exceptions import (
    APIException,
    NotFound,
    PermissionDenied,
    NotAuthenticated,
)


class TokenExpired(NotAuthenticated):
    status_code = 403
    default_detail = "Access token expired"
    default_code = "forbidden"


class ClientNotFound(NotAuthenticated):
    status_code = 403
    default_detail = "Client not found"
    default_code = "forbidden"
