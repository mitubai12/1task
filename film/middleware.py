import logging
import time

from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import redirect


class IPBlockMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')

        if ip in ['127.0.0.1']:
            return HttpResponseForbidden()

        response = self.get_response(request)

        return response
