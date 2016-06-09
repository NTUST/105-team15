from django.db import models
from django.utils import timezone

# Create your models here.
class MRTLines(models.Model):
    line_name = models.CharField(max_length=10)

    def __str__(self):
        return self.line_name

class MRTStops(models.Model):
    #路線顏色
    #車站名稱
    stop_line = models.ManyToManyField(MRTLines)
    stop_name = models.CharField(max_length=10)

    def __str__(self):
        return self.stop_name

class HotSpot(models.Model):
    #景點類型
    TYPES = (
        ('美食', '美食'),
        ('景點', '景點'),
    )

    #景點所在車站
    spot_stop = models.ForeignKey(MRTStops)

    #景點
    spot_type = models.CharField(
        max_length = 10,
        choices = TYPES,
        default = '美食'
    )

    spot_name = models.CharField(max_length=20)#名稱
    spot_commit = models.TextField(max_length=500)#心得
    spot_img_source = models.CharField(max_length=50)#圖片相對位置

    #更新時間
    created_time = models.DateTimeField(editable=False)
    modified_time = models.DateTimeField()

    #Super()
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_time = timezone.now()
        self.modified_time = timezone.now()
        return super(HotSpot, self).save(*args, **kwargs)

    def __str__(self):
        return self.spot_name
