from tkinter import CASCADE
from unicodedata import category
from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=45)
    class Meta: #모델에 대한 다양한 사항 정의
        db_table = 'menu' # 테이블을 식별하는데 사용하는 이름 설정(db상 이름 menus)

class Categories(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE) 
    # 1:N에서 N쪽이 관계(FK)선언
    # CASCADE: 1쪽이 삭제됐을때 모든 N쪽 데이터 삭제
    class Meta:
        db_table = 'categories'

class Images(models.Model):
    image_url = models.CharField(max_length=300)
    drink = models.ForeignKey('Drinks',on_delete=models.CASCADE)
    class Meta:
        db_table = 'images'

class Drinks(models.Model):
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField(max_length=100)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    class Meta:
        db_table = 'drinks'

class Allergy_drink(models.Model):     #drinks와 allergy 의 중간테이블 
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink = models.ForeignKey('Drinks', on_delete=models.CASCADE)
    class Meta:
        db_table = 'allergy_drink'


class Allergy(models.Model):
    name = models.CharField(max_length=45)
    drinks = models.ManyToManyField(Drinks, through='Allergy_drink') #through에 중간테이블명 넣어줌
    class Meta:
        db_table = 'allergy'
   

class Nutritions(models.Model):  
    one_serving_kcal = models.DecimalField(max_digits=10, decimal_places=5)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=5)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=5)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=5)
    protein_g = models.DecimalField(max_digits=10, decimal_places=5)
    drink = models.ForeignKey('Drinks', on_delete=models.CASCADE )
    size = models.ForeignKey('Sizes', on_delete=models.CASCADE)
    class Meta:
        db_table = 'nutritions'

class Sizes(models.Model):
    name = models.CharField(max_length=45)
    size_mi = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)
    class Meta:
        db_table = 'sizes'

# # categories(다) - (일)menu :  one-to-many : Menu 메뉴에 음료/푸드/상품 등 카테고리
# # drinks(다) - (일)categories : one-to-many
# # images (다) - drinks(일) : one-to-many
# # nutritions(다) - drinks(일) : one-to-many
# # nutritions(다) - sizes(일) : one-to-many
# drinks(다) - (다) allergy : many-to-many / allergy_drink 중간테이블
# NULL은 포인터가 가져올 값이 없는 상태
# 중간테이블 직접 정의 through model
# drinks와 sizes가 다대다이고, nutritions가 중간테이블인가? - 아님

