from django.contrib import admin

from eqp.models import tbl_station, tbl_box, tbl_qr_code, tbl_eqp
admin.site.register(tbl_box)
admin.site.register(tbl_station)
admin.site.register(tbl_qr_code)
admin.site.register(tbl_eqp)
# Register your models here.
