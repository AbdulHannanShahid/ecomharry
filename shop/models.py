from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name= models.CharField(max_length=50)
    product_category= models.CharField(max_length=30,default='')
    product_subcategory= models.CharField(max_length=30,default='')
    product_price= models.IntegerField(default=0)
    product_desc= models.CharField(max_length=300)
    product_date= models.DateField()
    product_img= models.ImageField(upload_to='shop/images',default='')
    def __str__(self):
        return self.product_name
class Contact(models.Model):
    msg_id = models.AutoField(primary_key="true")
    name= models.CharField(max_length=50,default="")
    email= models.CharField(max_length=70,default='')
    phone= models.CharField(max_length=100,default='')
    desc= models.CharField(max_length=500,default='')
    
    def __str__(self):
        return self.name
class Orders(models.Model):
    order_id = models.AutoField(primary_key="true")
    items_json= models.CharField(max_length=5000)
    name= models.CharField(max_length=70)
    amount= models.IntegerField(default=0)
    email= models.CharField(max_length=70,default='')
    address= models.CharField(max_length=500,default='')
    city= models.CharField(max_length=50,default='')
    state= models.CharField(max_length=50,default='')
    zip_code= models.CharField(max_length=5 ,default='')
    phone= models.CharField(max_length=70, default='')
    
    def __str__(self):
        return self.name
class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
