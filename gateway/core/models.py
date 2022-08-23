# -*- coding: utf-8 -*-
import requests, json
from django.db import models
from django.utils.translation import gettext_lazy as _

class Gate(models.Model):
    name = models.CharField(max_length=128, unique=True)
    request_path = models.CharField(max_length=255)
    upstream_url = models.CharField(max_length=255)

    def send_request(self, request):
        headers = {}
        strip = '/service' + self.request_path
        full_path = request.get_full_path()[len(strip):]
        url = self.upstream_url + full_path
        method = request.method.lower()
        method_map = {
            'get': requests.get,
            'post': requests.post,
            'put': requests.put,
            'patch': requests.patch,
            'delete': requests.delete
        }

        for k,v in request.FILES.items():
            request.data.pop(k)
        
        if request.content_type and request.content_type.lower()=='application/json':
            data = json.dumps(request.data)
            headers['content-type'] = request.content_type
        else:
            data = request.data
        print(url)
        return method_map[method](url, headers=headers, data=data, files=request.FILES)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name