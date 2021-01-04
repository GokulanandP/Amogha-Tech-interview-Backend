from django.db import models

class Customer(models.Model):
    USER_TYPE = ((1, 'farmer'), (2, 'retailer'))
    CROP_TYPE = ((1, 'fruits'), (2, 'vegetables'),(3, 'crops'))
    user_key = models.IntegerField(unique=True)
    user_name = models.CharField(max_length=120)
    user_type = models.IntegerField(choices=USER_TYPE)
    address = models.CharField(max_length=500)
    crop_type = models.IntegerField(choices=CROP_TYPE)
    contact = models.IntegerField(max_length=10)

class Retailer(models.Model):
    user_key = models.IntegerField()
    auctions_participated = models.CharField(max_length=120)

class Farmer(models.Model):
    user_key = models.IntegerField()
    auctions_created = models.CharField(max_length=120)

class Auction(models.Model):
    CROP_TYPE = ((1, 'fruits'), (2, 'vegetables'), (3, 'crops'))
    AUCTION_STATUS = ((1,'ongoing'),(2,'completed'))
    user_key = models.IntegerField()
    auction_key = models.IntegerField(unique=True)
    status = models.IntegerField(choices=AUCTION_STATUS)
    max_bid = models.IntegerField(max_length=5)
    max_bid_customer = models.IntegerField()
    crop_type = models.IntegerField(choices=CROP_TYPE)
