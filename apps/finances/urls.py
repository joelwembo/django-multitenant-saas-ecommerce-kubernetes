from django.urls import path
from .views import Accounts , Transactions , Categories , AccountDetail
from . import views
urlpatterns = [
    path('apiview', Accounts.as_view()),
    path('accounts', Accounts.as_view()),
    path('transactions', Transactions.as_view()),
    path('categories', Categories.as_view()),
    path('accounts/<str:pk>', AccountDetail.as_view()),
    path('transactions/<str:pk>', Transactions.as_view()),
    path('categories/<str:pk>', Categories.as_view())
]
