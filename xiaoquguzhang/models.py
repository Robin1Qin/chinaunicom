from django.db import models


class XiaoQuGuZhang(models.Model):
    account = models.CharField(max_length=17, verbose_name='用户账号')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='报障时间')
    bars = models.GenericIPAddressField(max_length=30, verbose_name='接入设备')

    class Meta:
        verbose_name = '小区故障'
        verbose_name_plural = '小区故障'

    def __self__(self):
        return self.account


class Raduis(models.Model):
    pub_date = models.DateTimeField(primary_key=True,verbose_name='报障时间',null=False)
    bars_ip = models.GenericIPAddressField(max_length=30, verbose_name='接入设备',null=False)
    account = models.CharField(max_length=17, verbose_name='用户账号')
    problem = models.CharField(max_length=250, verbose_name='故障详情')

    class Meta:
        verbose_name = 'Raduis日志'
        verbose_name_plural = 'Raduis日志'

    def __self__(self):
        return self.account
