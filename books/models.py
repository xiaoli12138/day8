from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField(auto_now_add=True)

    # 元类信息 : 修改表名
    class Meta:
        db_table = 'book'


# 轮播图
class Banner(models.Model):
    carousel_id = models.IntegerField(auto_created=True, primary_key=True)
    carousel_url = models.CharField(max_length=100)
    redirect_url = models.CharField(max_length=100)
    carousel_rand = models.IntegerField()
    is_deleted = models.IntegerField(default=0)
    create_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'mall_carousel'


# 用户表
class User(models.Model):
    user_id = models.IntegerField(auto_created=True, primary_key=True)
    login_name = models.CharField(max_length=100)
    user_pwd = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    locked = models.IntegerField(default=0)
    introduce = models.CharField(max_length=100)
    is_deleted = models.IntegerField(default=0)
    create_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'mall_user'


# 用户地址表
class Address(models.Model):
    address_id = models.IntegerField(auto_created=True, primary_key=True)
    user_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_phone = models.IntegerField()
    default_flag = models.IntegerField(default=0)
    province_name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    region_name = models.CharField(max_length=100)
    detail_address = models.CharField(max_length=100)
    create_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'user_address'


# 用户token表
class Token(models.Model):
    Token_id = models.IntegerField(auto_created=True, primary_key=True)
    user_id = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    update_time = models.DateField(auto_now_add=True)
    expire_time = models.DateField()

    class Meta:
        db_table = 'user_token'


# 商品信息表
class Goods(models.Model):
    goods_id = models.IntegerField(auto_created=True, primary_key=True)
    goods_name = models.CharField(max_length=100)
    goods_intro = models.CharField(max_length=100)
    goods_category = models.CharField(max_length=100)
    goods_cover_img = models.CharField(max_length=100)
    goods_carousel = models.CharField(max_length=100)
    goods_detail_content = models.CharField(max_length=100)
    original_price = models.FloatField()
    selling_price = models.FloatField()
    stock_num = models.IntegerField()
    tag = models.CharField(max_length=100)
    goods_sell_status = models.IntegerField(default=0)
    create_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'goods_info'


# 商品分类表
class Category(models.Model):
    category_id = models.IntegerField(auto_created=True, primary_key=True)
    category_level = models.IntegerField()
    parent_id = models.CharField(max_length=100)
    category_name = models.CharField(max_length=100)
    category_rank = models.IntegerField()
    is_deleted = models.IntegerField(default=0)
    create_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'goods_category'


# 购物车表
class Cart(models.Model):
    cart_item_id = models.IntegerField(auto_created=True, primary_key=True)
    user_id = models.CharField(max_length=100)
    goods_id = models.CharField(max_length=100)
    goods_count = models.CharField(max_length=100)
    is_deleted = models.IntegerField(default=0)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField()

    class Meta:
        db_table = 'shopping_cart'
