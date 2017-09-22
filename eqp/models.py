from django.db import models
from CellMES.models import tbl_base as base
# Create your models here.

# 站点信息表
class tbl_station(base):
    def __str__(self):
        return self.station_name_cn
    station_id = models.CharField('站点ID', max_length=32, primary_key=True)
    station_name_en = models.CharField('站点名称(英文)', max_length=32)
    station_name_cn = models.CharField('站点名称(中文)', max_length=32)
    station_desc = models.CharField('站点描述', max_length=100)
    station_seq = models.CharField('站点顺序', max_length=32)

# 设备信息表


class tbl_eqp(base):
    def __str__(self):
       return self.eqp_name_cn
    # 设备编号
    eqp_id = models.CharField('设备编号', max_length=32, primary_key=True)
    # 设备名称
    eqp_name_en = models.CharField(u'设备名称(英文)', max_length=32)
    # 设备名称
    eqp_name_cn = models.CharField(u'设备名称(中文)', max_length=32)
    # 设备对应的站点
    eqp_station = models.ForeignKey(tbl_station)
    # 设备状况，分多个等级，1-10
    eqp_status = models.TextField('设备状况', max_length=128)

# 二维码信息表
class tbl_qr_code(base):
    def __str__(self):
        return self.qr_content
    qr_status = (
        ('Valid', '有效'),
        ('Invalid', '失效'),
        ('Pending', '待定'),
        ('Deleted', '已删除'),
    )
    use = (
        ('Box', '料盒'),
        ('Batch', '批次号'),
    )
    qr_kinds = (
        ('1', '一维码'),
        ('2', '二维码'),
    )
    qr_id = models.AutoField(primary_key=True)
    qr_create_station = models.ForeignKey(tbl_station, verbose_name='生码站点')
    qr_content = models.CharField('标识内容', max_length=128)
    qr_use = models.CharField('用途', max_length=32, choices=use, default='Box')
    qr_kind = models.CharField('种类', max_length=32, choices=qr_kinds, default='2')
    qr_description = models.CharField('备注', max_length=128)
    # box_no = models.BigIntegerField('二维码ID', default=0)
    qr_status = models.CharField('状态', max_length=32, choices=qr_status, default='Valid')


# 料盒信息表
class tbl_box(base):
    def __str__(self):
        return str(self.box_id)
    box_status = (
        ('Normal', '正常'),
        ('Pending', '挂起'),
        ('Deleted', '废弃'),
    )
    box_id = models.AutoField(primary_key=True, verbose_name='料盒ID')
    box_name = models.CharField('料盒名称', max_length=32)
    # 料盒的二维码
    box_code = models.ForeignKey(tbl_qr_code, verbose_name='二维ID')
    # 料盒容量
    box_capacity = models.BigIntegerField(default=50)
    # 料盒描述
    box_description = models.CharField('料盒描述', max_length=100)


