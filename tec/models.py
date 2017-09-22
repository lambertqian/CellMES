from django.db import models
from CellMES.models import tbl_base as base
from eqp.models import tbl_eqp
# Create your models here.

# 工艺参数表（也是设备设定值）
class tbl_technology(base):
    def __str__(self):
        return self.tec_id

    units = (
        ('g', 'g'),
        ('kg', 'kg'),
        ('ml', 'ml'),
        ('ml/s', 'ml/s'),
        ('C', 'C'),
    )
    # ID
    tec_id = models.CharField('ID', max_length=32, primary_key=True)
    # 设备编号
    eqp_id = models.ForeignKey(tbl_eqp)
    # 参数编号
    para_id = models.CharField('参数编号', max_length=32)
    # 参数名称
    para_name = models.CharField('参数名', max_length=32)
    # 参数设定值
    para_value = models.CharField('设定值', max_length=32)
    # 参数单位
    para_unit = models.CharField('单位', max_length=32, choices=units, default='C')


# 产品流转设定表
class tbl_flow (base):
    def __str__(self):
        return self.flow_uuid
    flow_uuid = models.CharField('id', max_length=32, primary_key=True)
    flow_version = models.CharField('工作流版本', max_length=100)
    current_eqp = models.CharField('当前站', max_length=32)
    parent_eqp = models.CharField('父站', max_length=32)
