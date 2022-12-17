from django.db import models

class Collection(models.Model):
    title=models.CharField(max_length=255)

class Product(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
    collection=models.ForeignKey(Collection,on_delete=models.PROTECT)

class Customer(models.Model):
    MEMBERSHIP_BROMZE='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'
    membership_choice=[
        (MEMBERSHIP_BROMZE,'bronze'),
        (MEMBERSHIP_SILVER,'silver'),
        (MEMBERSHIP_GOLD,'gold')
    ]
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=255)
    birth_date=models.DateField(null=True)
    membership=models.CharField(max_length=1,choices=membership_choice,default=MEMBERSHIP_BROMZE)

title=models.CharField(max_length=255)

class Order(models.Model):
    pending_payment='P'
    complete_payment='C'
    failed_payment='F'
    payment_choice=[
        (pending_payment,'pending'),
        (complete_payment,'complete'),
        (failed_payment,'failed')
    ]
    placed_at=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=1, choices=payment_choice,default=pending_payment)
    order=models.ForeignKey(Customer,on_delete=models.CASCADE)
    items=models.ForeignKey('OrderItems', on_delete=models.CASCADE)

class Address(models.Model):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    Customer=models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True) 
    #cascade means that when we delete the address the whole record will be deleted.


class OrderItems(models.Model):
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    price=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.PositiveSmallIntegerField()
    unit_price=models.DecimalField(max_length=6,decimal_places=3)


class Cart(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)

class CartItems(models.model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()



