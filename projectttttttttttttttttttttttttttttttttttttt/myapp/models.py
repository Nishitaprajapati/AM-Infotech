from django.db import models
from django.utils.safestring import  mark_safe
# Create your models here.
list_gender = [
    ("1", "Male"),
    ("2", "Famale")
]

list_status = [
    ("1", "online"),
    ("2", "offline")
]

list_cancel = [
    ("1", "yes"),
    ("2", "no")
]


class Company(models.Model):
    company_name = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.company_name


class State(models.Model):
    state_name = models.CharField(max_length=30)

    def __str__(self):
        return self.state_name


class City(models.Model):
    city_name = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class Area(models.Model):
    area_name = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.area_name


class User(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Email_id = models.EmailField(max_length=40)
    Contact_number = models.IntegerField()
    Password = models.CharField(max_length=15)
    cpassword=models.CharField(max_length=15,null=True)

    Address = models.CharField(max_length=80)
    image2=models.ImageField(upload_to='photos',null=True)
    Security_Que = models.CharField(max_length=50)
    Security_Answer = models.CharField(max_length=50)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def user_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image2.url))

    user_photo.allow_tags = True

    def __str__(self):
        return self.First_name




class Order(models.Model):
    Pay_amount = models.FloatField()
    Payment_date = models.DateTimeField(auto_now_add=True)
    Payment_status = models.CharField(choices=list_status, max_length=30)
    cgst = models.FloatField()
    sgst = models.FloatField()
    is_order_cancel = models.CharField(choices=list_cancel, max_length=30)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.TextField(null=True)

    def __float__(self):
        return self.Pay_amount

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


class Sub_category(models.Model):
    sub_category_name = models.CharField(max_length=30)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_category_name

class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_description = models.TextField()
    price = models.IntegerField()
    quantity_on_hand = models.IntegerField()
    sub_category_id = models.ForeignKey(Sub_category, on_delete=models.CASCADE)
    image_path = models.ImageField(upload_to='photos',null=True)
    def __int__(self):
        return self.id
    def __str__(self):
        return self.product_name

    def admin_photo(self):
        return mark_safe('<Img src="{}" width="100"/>'.format(self.image_path.url))
        admin_photo.allow_tags=True


class order_details(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)





class Order_return(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_return_date = models.DateTimeField()
    order_return_amt = models.FloatField()

    def __str__(self):
        return self.order_return_date


class Order_return_details(models.Model):
    return_reason = models.CharField(max_length=100)
    return_qoh = models.IntegerField()


class Inquery(models.Model):
    inquery_description = models.TextField()
    inquery_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.CharField(max_length=60,null=True)



class Cart(models.Model):
    quantity = models.IntegerField()
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    totalprice = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_status = models.IntegerField(null=True)
    orderid = models.IntegerField()

class Cartfinal(models.Model):
    quantity = models.IntegerField()
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_status=models.IntegerField()



class Compliant(models.Model):
    compliant_description = models.TextField()
    compliant_date = models.DateTimeField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Complaints(models.Model):
    compliant_details=models.TextField()
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

class Brand(models.Model):
    brand_name = models.CharField(max_length=30)



class Offer(models.Model):
    offer_description = models.TextField(null=True)
    Start_date = models.DateTimeField(null=True)
    End_date = models.DateTimeField(null=True)
    discount = models.FloatField(null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)

    def __int__(self):
        return self.id


class Feature(models.Model):
    feature_name = models.CharField(max_length=30)
    feature_description = models.TextField()

    def __str__(self):
        return self.feature_name





class Feedback(models.Model):
    feedback = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.feedback

class connectus(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    subject_here=models.CharField(max_length=30)
    details=models.CharField(max_length=100)
