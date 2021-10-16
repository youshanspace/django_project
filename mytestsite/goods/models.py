from django.db import models

# Create your models here.

# 商品分類表
# 模型類 對應一張表
class GoodsCategary(models.Model):
    # 分類的名稱
    cag_name = models.CharField(max_length=30)
    # 分類的樣式
    cag_css = models.CharField(max_length=20)
    # 分類的圖片
    # cad_img = models.ImageField(upload_to='cag')
    
# 商品表 
# 模型類
class GoodsInfo(models.Model):
    # 商品名字
    goods_name = models.CharField(max_length=100)
    # 商品的價格
    goods_price = models.IntegerField(default=0)
    # 商品的描述
    goods_desc = models.CharField(max_length=2000)
    # 商品的圖片
    # goods_img = models.ImageField(upload_to='goods')
    # 所屬的分類 外鍵指向上面這張表
    # goods_cag = models.ForeignKey('GoodsCategary')