from django.contrib import admin

# Register your models here.
from .models import GoodsCategary, GoodsInfo

# 註冊模型
admin.site.register(GoodsCategary)
admin.site.register(GoodsInfo)