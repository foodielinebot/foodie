from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from NTPUFoodie_bot.models import *

class User_Info_Admin(admin.ModelAdmin):
    list_display = ('uid','name','pic_url','mtext','mdt')
admin.site.register(User_Info,User_Info_Admin)


class FoodieDatabase_Admin(admin.ModelAdmin):
	list_display = ('column1','restaurant','address','class_field')
admin.site.register(FoodieDatabase,FoodieDatabase_Admin)