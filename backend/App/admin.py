from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Staff)
admin.site.register(Assets)
admin.site.register(AssetsIssuance)
admin.site.register(Categories)
admin.site.register(Todo)

