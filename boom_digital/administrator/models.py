from django.db import models

# Create your models here.

class Admin_users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta :
        db_table = 'admin_users'

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='category_images/')

    class Meta :
        db_table = 'category'

class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='brand_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta :
        db_table = 'brand'
                                                                                                                                                                                                                                                                                                                                 
class Employee(models.Model):
    first_name = models.CharField(max_length=50,default='')
    second_name = models.CharField(max_length=50,default='')
    email = models.EmailField(default='')
    password = models.CharField(default='user@123')
    phone = models.CharField(max_length=15,default=0)
    gender = models.CharField(max_length=15)
    position = models.CharField(max_length=100,default='')
    hired_date = models.DateField(default='')
    qualification = models.CharField(max_length=100,default='')
    profile_img = models.ImageField(upload_to='employee_images/')
    
    def full_name(self):
        return f"{self.first_name}{self.second_name}"

    class Meta :
        db_table = 'employee'

class Customer(models.Model) :
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'customer'
