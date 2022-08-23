# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from core.models import Gate

class GatewayView(APIView):
    authentication_classes = ()

    def operation(self, request):
        path = request.path_info.split('/')
        if len(path) < 2:
            return Response('bad request #1', status=status.HTTP_400_BAD_REQUEST)

        gates = Gate.objects.filter(name=path[2])
        if gates.count() != 1:
            return Response('bad request #2', status=status.HTTP_400_BAD_REQUEST)

        res = gates[0].send_request(request)
        if res.headers.get('Content-Type', '').lower() == 'application/json': data = res.json()
        else: data = res.content
        return Response(data=data, status=res.status_code)
    
    def get(self, request):
        return self.operation(request)

    def post(self, request):
        return self.operation(request)

    def put(self, request):
        return self.operation(request)
    
    def patch(self, request):
        return self.operation(request)
    
    def delete(self, request):
        return self.operation(request)