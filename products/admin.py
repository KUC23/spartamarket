from django.contrib import admin

# Register your models here.
# articles/admin.py
from .models import Product

@admin.register(Product)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "content")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
