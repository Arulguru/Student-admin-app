from django.contrib import admin

# Register your models here.
from .models import db
from .models import assign

admin.site.register(db)

admin.site.register(assign)
