from .models import Application, AuthToken
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.utils import timezone
from datetime import timedelta
import json
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .exceptions import TokenExpired
from .generators import generate_client_id, generate_client_secret
from .serializers import AuthTokenCreateSerializer

class CreateAccessView(APIView):
    authentication_classes = []
    permission_classes = []
    parser_classes = (JSONParser,)

    @swagger_auto_schema(
        operation_description="Get the Access token and refresh token for the Client_id and Client_Secret Provided",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['client_id', 'client_secret'],
            properties={
                'client_id': openapi.Schema(type=openapi.TYPE_STRING),
                'client_secret': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        security=[],
        tags=['GetAccessToken'],
        responses={200: AuthTokenCreateSerializer}
    )
    def post(self, request, *args, **kwargs):
        """[Get the Access token and refresh token for the Client_id and Client_Secret Provided]

        Arguments:
            {
                'client_id': str,
                'client_secret': str
            }

        Returns:
            {
                application: integer
                access_token: string
                refresh_token: string
                expiry_date: string($date-time)
                refresh_token_expiry: string($date-time)
                expired: boolean
                created_on: string($date-time)
            }
        """
        details = request.data
        req_client_id = details["client_id"]
        req_client_secret = details["client_secret"]
        try:
            client_present = Application.objects.get(
                client_id=req_client_id, client_secret=req_client_secret
            )
            try:
                token = AuthToken.objects.get(application=client_present)
                if (timezone.now() < token.expiry_date) and (timezone.now() < token.refresh_token_expiry):
                    res = (
                    AuthToken.objects.filter(application=client_present)
                    .order_by("-application_id")[0:1]
                    .values()
                    )[0]
                else:
                    token.access_token = generate_client_secret()
                    token.expiry_date = timezone.now() + timedelta(hours=2)
                    token.refresh_token = generate_client_secret()
                    token.refresh_token_expiry = timezone.now() + timedelta(days=7)
                    token.save()
                    res = (
                        AuthToken.objects.filter(application=client_present)
                        .order_by("-application_id")[0:1]
                        .values()
                    )[0]
            except Exception:
                AuthToken.objects.create(
                    application=client_present,
                    access_token=generate_client_secret(),
                    refresh_token=generate_client_secret(),
                    refresh_token_expiry = timezone.now() + timedelta(days=7),
                    expiry_date=timezone.now() + timedelta(hours=2),
                )
                res = AuthToken.objects.filter(application=client_present).values()[0]
                return Response(res, status=status.HTTP_200_OK)
        except Exception as e:
            res = "Client not found"
            return Response(data={"status": "Client not found"}, status=status.HTTP_403_FORBIDDEN)
        return Response(res, status=status.HTTP_200_OK)


class RefreshAccessView(APIView):
    
    authentication_classes = []
    permission_classes = []
    parser_classes = (JSONParser,)

    @swagger_auto_schema(
        operation_description="Get new Access token for the refresh token provided.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['refresh_token'],
            properties={
                'refresh_token': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        security=[],
        tags=['RefreshTheToken'],
        responses={200: AuthTokenCreateSerializer}
    )
    def post(self, request, *args, **kwargs):
        """[Get the new Access token with the refresh token Provided]

        Arguments:
            {
                'refresh_token': str
            }

        Returns:
            {
                application: integer
                access_token: string
                refresh_token: string
                expiry_date: string($date-time)
                refresh_token_expiry: string($date-time)
                expired: boolean
                created_on: string($date-time)
            }
        """

        details = request.data
        req_refresh_token = details["refresh_token"]
        try:
            token_present = AuthToken.objects.get(refresh_token=req_refresh_token)
            token = AuthToken.objects.get(application=token_present)
            if timezone.now() < token.refresh_token_expiry:
                token.access_token = generate_client_secret()
                token.expiry_date = timezone.now() + timedelta(hours=2)
                token.save()
                res = (
                    AuthToken.objects.filter(refresh_token=req_refresh_token)
                    .order_by("-application_id")[0:1]
                    .values()
                )
            else:
                return Response(data={"status": "Refresh Token expired"}, status=status.HTTP_403_FORBIDDEN)
        except Exception:
            res = "Token not found"
            return Response(data={"status": "Token not found"}, status=status.HTTP_403_FORBIDDEN)
        return Response(res, status=status.HTTP_200_OK)

