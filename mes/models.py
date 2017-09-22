from django.db import models
from CellMES.models import tbl_base as base
from eqp.models import tbl_eqp, tbl_station, tbl_box

# Create your models here.
# 人员信息表
class tbl_operator(base):
    def __str__(self):
        return self.operator_name
    qr_choices = (
        ('Normal', '正常工作'),
        ('Dimission', '离职'),
        ('Deleted', '已删除'),
    )
    gender = (
        ('0', '男'),
        ('1', '女'),
    )
    operator_id = models.CharField('ID', max_length=32, primary_key=True)
    operator_name = models.CharField('姓名', max_length=64)
    # 性别，0表示女，1表示男
    operator_gender = models.CharField('性别', max_length=1, default='1', choices=gender)
    operator_age = models.CharField('年龄', max_length=4, default=20)
    # 0表示正常，1表示离职，2表示请假·····
    operator_status = models.CharField('状态', max_length=32, default='Normal', choices=qr_choices)
    # 常用站点
    usual_station = models.ForeignKey(tbl_station, verbose_name='工作站点')
    # 当前站点
    # current_station = models.ForeignKey(tbl_station)

class tbl_box_record(base):
    in_out = (
        ('0', '进站'),
        ('1', '出站'),
        ('2', 'pending'),
    )
    box_id = models.ForeignKey(tbl_box, verbose_name='料盒ID')
    eqp_id = models.ForeignKey(tbl_eqp, verbose_name='设备ID')
    process = models.CharField('进出站状态', max_length=32, choices=in_out, default='0')



