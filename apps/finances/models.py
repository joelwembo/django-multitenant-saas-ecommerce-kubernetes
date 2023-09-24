from datetime import datetime
import uuid
from django.db import models


TYPES = [
    ("expense", "Expense"),
    ("income", "Income"),
    ("transfer", "Transfer"),
]


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(default=datetime.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPES, default="expense")
    category = models.ForeignKey(
        "Category", on_delete=models.DO_NOTHING, related_name="transactions"
    )
    account = models.ForeignKey(
        "Account", on_delete=models.CASCADE, related_name="transactions"
    )
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "Transactions"
        ordering = ['-createdAt']

        def __str__(self):
            return f"{self.date} - {self.amount} - {self.description}"


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="subcategories",
        null=True,
        blank=True,
    )
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "Categories"
        ordering = ['-createdAt']

        def __str__(self):
            return self.name


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    initial_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "Accounts"
        ordering = ['-createdAt']
        def __str__(self):
            return self.name