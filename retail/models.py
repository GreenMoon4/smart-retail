from django.db import models

class Products(models.Model):
    description = models.CharField(max_length=200)
    pricing = models.CharField(max_length=100)
    reviews = models.CharField(max_length=100)
    image = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'products'

class AmazonReviews(models.Model):
    id = models.IntegerField(primary_key=True)
    pid = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=2000, null=True, blank=True)
    asins = models.CharField(max_length=50, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    categories = models.CharField(max_length=1000, null=True, blank=True)
    keys = models.CharField(max_length=10000, null=True, blank=True)
    manufacturer = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    dateAdded = models.DateTimeField(null=True, blank=True)
    dateSeen = models.CharField(max_length=2000, null=True, blank=True)
    didPurchase = models.CharField(max_length=200, null=True, blank=True)
    doRecommend = models.BooleanField(null=True, blank=True)
    review_id = models.CharField(max_length=100, null=True, blank=True)
    numHelpful = models.IntegerField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    sourceURLs = models.URLField(max_length=20000, null=True, blank=True)
    text = models.CharField(max_length=15000, null=True, blank=True)
    title = models.CharField(max_length=10000, null=True, blank=True)
    userCity = models.CharField(max_length=100, null=True, blank=True)
    userProvince = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'amazonreviews'
