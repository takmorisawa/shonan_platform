from django.contrib import admin
from rest_app.models import Product,Series,Device,Report,Support


class ProductAdmin(admin.ModelAdmin):
    list_display=("id","name")
    list_display_links=("id","name")

class SeriesAdmin(admin.ModelAdmin):
    list_display=("id","name")
    list_display_links=("id","name")

class DeviceAdmin(admin.ModelAdmin):
    list_display=("id","name","series")
    list_display_links=("id","name")
    raw_id_fields=("series",)

class ReportAdmin(admin.ModelAdmin):
    list_display=("id","user_id","date","usable","comment","enable_escape",
        "authorized","voice","data","priority","device","product")
    list_display_links=("id","user_id","date","usable","comment","enable_escape",
        "authorized","voice","data","priority")
    # raw_id_fields=("device","product")

class SupportAdmin(admin.ModelAdmin):
    list_display=("id","device_name","maker_name","voice","data","tethering","sns","product")
    list_display_links=("id","device_name","maker_name","voice","data","tethering","sns")
    #raw_id_fields=("product",)

admin.site.register(Product,ProductAdmin)
admin.site.register(Series,SeriesAdmin)
admin.site.register(Device,DeviceAdmin)
admin.site.register(Report,ReportAdmin)
admin.site.register(Support,SupportAdmin)
