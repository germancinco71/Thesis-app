from django.contrib import admin
from .models import medpapers, itpapers, cspapers, Comment, itcomment

admin.site.register(medpapers)
admin.site.register(itpapers)
admin.site.register(cspapers)
admin.site.register(Comment)
admin.site.register(itcomment)