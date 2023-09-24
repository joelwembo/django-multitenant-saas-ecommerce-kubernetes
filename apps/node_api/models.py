import uuid
from django.db import models


class NoteModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    category = models.CharField(max_length=100, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "notes"
        ordering = ['-createdAt']

        def __str__(self) -> str:
            return self.title
        

class SubscribeToNewsletter(models.Model):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.email        
    
    
# Models for pytest

class Retail(models.Model):
    name = models.CharField(max_length=128)

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True)  # unique model number
    name = models.CharField(max_length=50)
    description = models.TextField(default="", blank=True)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    retails = models.ManyToManyField(
        Retail,
        related_name="products",
        verbose_name="Retail stores that carry the product",
    )
    category = models.ForeignKey(
        Category, 
				related_name="products", 
				on_delete=models.CASCADE,
				blank=True,
				null=True,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)    

# Example for Custom migration

class Users(models.Model):
        name = models.CharField(max_length=255)
        bank_name = models.CharField(max_length=255)
        branch_name = models.CharField(max_length=255)
        ifsc_code = models.CharField(max_length=255)
        account_number = models.CharField(max_length=255)
        
        class Meta:
            db_table = 'users'
 
            
# class BankAccounts(models.Model):
#     class Meta:
#         db_table = 'bank_accounts'
    
#     bank_name = models.CharField(max_length=255)
#     branch_name = models.CharField(max_length=255)
#     ifsc_code = models.CharField(max_length=255)
#     account_number = models.CharField(max_length=255)
#     user = models.ForeignKey(Users, on_delete=models.CASCADE)            