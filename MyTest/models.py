from django.db import models
# Create your models here.
# my test
class mytest(models.Model):
    def __str__(self):
        return self.name
    status_choices = (
        ('有效', 'publish'),
        ('无效', 'private'),
        ('已删除', 'deleted'),
    )
    name = models.CharField(u'名称', max_length = 100)
    content = models.CharField(u'内容', max_length = 256)
    PV_num = models.BigIntegerField(u'统计量', default=0)
    status = models.CharField(u'状态', max_length=10,choices=status_choices, default = '有效')
    creator = models.CharField(u'创建人', max_length = 100)
    update_time = models.DateTimeField(u'最后更新时间', auto_now= True)



