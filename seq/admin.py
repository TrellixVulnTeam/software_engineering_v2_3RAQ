from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Seq


# Register your models here.
admin.site.register(Seq)
