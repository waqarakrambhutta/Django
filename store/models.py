from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)

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

class order(models.Model):
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


class address(models.Model):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    Customer=models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True) 
    
    
    #cascade means that when we delete the address the whole record will be deleted.



