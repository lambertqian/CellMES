from django.db import models
class tbl_base(models.Model):
    # 基本表
    creator = models.CharField('创建人', max_length=32, default='admin')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_user = models.CharField('最后更新人', max_length=32, default='admin')
    update_time = models.DateTimeField(u'最后更新时间', auto_now=True)
    class Meta:
        abstract = True
        ordering = ('update_time',)