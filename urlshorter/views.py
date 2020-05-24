from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from requests.utils import requote_uri
import urllib.parse
import json
import requests
from customauth.auth import CustomAuthentication

# Create your views here.

class UrlShorterView(APIView):
    authentication_classes = (CustomAuthentication,)

    @swagger_auto_schema(
        operation_description="Get the Shortned URL from the url passed.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['url'],
            properties={
                'url': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        tags=['ShortenURL'],
    )
    def post(self, request, *args, **kwargs):
        """[Post call which shortnes the URL]

        Arguments:
            request {[type]} -- [description]

        Returns:
            [result URL] -- [URL]
        """
        url_req = request.data['url']
        encode_url = urllib.parse.quote(url_req, safe='')
        url = "https://url-shortener-service.p.rapidapi.com/shorten"

        payload = "url=" + encode_url
        headers = {
            'x-rapidapi-host': "url-shortener-service.p.rapidapi.com",
            'x-rapidapi-key': "4c2c69f6f0msXXXXXXXXXXXXXXXXXXX0jsn7421053067af",
            'content-type': "application/x-www-form-urlencoded"
            }

        response = requests.request("POST", url, data=payload, headers=headers)

        return Response(json.loads(response.text), status=status.HTTP_200_OK)