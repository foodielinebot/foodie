from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User_Info(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')         #user_id
    name = models.CharField(max_length=255,blank=True,null=False)       #LINE名字
    pic_url = models.CharField(max_length=255,null=False)               #大頭貼網址
    mtext = models.CharField(max_length=255,blank=True,null=False)      #文字訊息紀錄
    mdt = models.DateTimeField(auto_now=True)                           #物件儲存的日期時間

    def __str__(self):
        return self.uid

class FoodieDatabase(models.Model):
    column1 = models.IntegerField(db_column='Column1', primary_key=True)  # Field name made lowercase.
    restaurant = models.CharField(db_column='Restaurant', max_length=33, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=18, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'foodie_database'

