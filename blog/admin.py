import models

from django.contrib import admin

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Article, ArticleAdmin)