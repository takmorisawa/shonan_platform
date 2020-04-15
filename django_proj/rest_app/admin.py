from django.contrib import admin
from rest_app.models import Spot,Post,Report

# admin.site.register(Spot)
# admin.site.register(Post)

class SpotAdmin(admin.ModelAdmin):
    list_display=("id","name","address")
    list_display_links=("id","name","address")

class PostAdmin(admin.ModelAdmin):
    list_display=("id","comment")
    list_display_links=("id","comment")
    raw_id_fields=("spot",)

class ReportAdmin(admin.ModelAdmin):
    list_display=("id","user_id","date","comment")
    list_display_links=("id","user_id","date","comment")

admin.site.register(Spot,SpotAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Report,ReportAdmin)
