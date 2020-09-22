from django.db import models
from django.utils import timezone


class Contract(models.Model):
    contract_name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)


class LoanApplication(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    loan_application = models.ForeignKey(
        LoanApplication,
        on_delete=models.CASCADE,
        related_name='product',
    )
    created_date = models.DateTimeField(default=timezone.now)


contract_id = 'some_id'
manufacturer_ids = LoanApplication.objects.filter(contract=contract_id).values('product__manufacturer').distinct()
manufacturers_by_id_contract = Manufacturer.objects.filter(id__in=manufacturer_ids)
