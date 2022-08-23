from django.contrib import admin

from django.apps import apps
from core.urls import app_name
from django.contrib.admin.sites import AlreadyRegistered

SpecialAdmin = lambda model: type(model.__name__, (admin.ModelAdmin,), {
    #'list_display': [x.name for x in model._meta.fields if x.get_internal_type() in ['CharField', 'BigAutoField']],
    #'list_filter': ['employee__place'],
    #'date_hierarchy': 'date'
})

app_models = apps.get_app_config(app_name).get_models()
for model in app_models:
    try:
        admin.site.register(model,SpecialAdmin(model))
    except AlreadyRegistered:
        pass