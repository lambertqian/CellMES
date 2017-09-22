from django.db import models
from CellMES.models import tbl_base as base
# Create your models here.
class tbl_spc_standard(base):
    units = (
        ('g', 'g'),
        ('kg', 'kg'),
        ('ml', 'ml'),
        ('ml/s', 'ml/s'),
        ('C', 'C'),
    )
    spc_id = models.CharField('SPC ID', max_length=32, primary_key=True, )
    spc_kind = models.CharField('SPC种类', max_length=32)
    spc_name = models.CharField('SPC名称', max_length=32)
    spc_value = models.CharField('SPC值', max_length=32, default=0)
    spc_unit = models.CharField('SPC单位', max_length=32, choices=units)
    spc_note = models.CharField('SPC备注', max_length=128)

class tbl_spc_test(base):
    units = (
        ('g', 'g'),
        ('kg', 'kg'),
        ('ml', 'ml'),
        ('ml/s', 'ml/s'),
        ('C', 'C'),
    )
    spc_id = models.CharField('SPC ID', max_length=32, primary_key=True, )
    spc_kind = models.CharField('SPC种类', max_length=32)
    spc_name = models.CharField('SPC名称', max_length=32)
    spc_value = models.CharField('SPC测试值', max_length=32, default=0)
    spc_unit = models.CharField('SPC单位', max_length=32, choices=units)
    spc_note = models.CharField('SPC备注', max_length=128)
