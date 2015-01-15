from django.contrib import admin
from app.models import Document, Committee

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    pass

@admin.register(Committee)
class CommitteeAdmin(admin.ModelAdmin):
    pass