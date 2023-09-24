from django.contrib import admin

# Register your models here.
from .models import NoteModel , SubscribeToNewsletter , Retail, Category, Product
from .models import  Users
admin.site.register(NoteModel)
admin.site.register(SubscribeToNewsletter)
admin.site.register(Retail)
admin.site.register(Category)
admin.site.register(Product)

admin.site.register(Users)
# admin.site.register(BankAccounts)