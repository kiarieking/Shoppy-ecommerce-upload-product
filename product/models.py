from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=150)


class Seller(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    status = models.IntegerField()
    county = models.CharField(max_length=150)
    store_name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class SellerProduct(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)


class Sales(models.Model):
    sellerproduct = models.ForeignKey(SellerProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Category(models.Model):
    name = models.CharField(max_length=150)
    parent_id = models.ForeignKey('Category', on_delete=models.DO_NOTHING,)
    description = models.TextField()


class ProductDetails(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    details_id = models.TextField()


class Details(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    full_specifications = models.TextField()


class Brand(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=150)
    parent_id = models.ForeignKey('Brand',on_delete=models.DO_NOTHING)


class Buyer(models.Model):
    name = models.CharField(max_length=150)
    phone_no = models.IntegerField(max_length=12)
    email = models.EmailField()
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=40)


class Address(models.Model):
    city = models.CharField(max_length=150)
    zip_code = models.IntegerField(max_length=40)
    county = models.CharField(max_length=150)
    postal_code = models.IntegerField(max_length=150)


class Order(models.Model):
    buyer_id = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)


class Admin(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=50)


class OrderProduct(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()


class Region(models.Model):
    name = models.CharField(max_length=150)
    delivery_amount = models.IntegerField()


class Discount(models.Model):
    product = models.ForeignKey(Products,on_delete=models.DO_NOTHING)
    percentage = models.IntegerField()


class SellerOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    sales = models.ForeignKey(Sales, on_delete=models.DO_NOTHING)


class OrderDelivery(models.Model):
    PENDING = 1
    DELIVERED = 2
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (DELIVERED, 'Delivered')
    )
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    delivery_status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING, blank=False, null=False)
    date_dispatched = models.DateTimeField()
    date_delivered = models.DateTimeField()


class Ratings(models.Model):
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    rates = models.IntegerField()
    buyer = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING)


class Inventory(models.Model):
    seller_product = models.ForeignKey(SellerProduct,on_delete=models.CASCADE)
    amount = models.IntegerField()


class Checkout(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Address,on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    phone_no = models.IntegerField()


class Offers(models.Model):
    offer = models.CharField(max_length=200)
    seller_product = models.ForeignKey(SellerProduct, on_delete=models.DO_NOTHING)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()


class Review(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING)
    comment = models.TextField()
    seller_product = models.ForeignKey(SellerProduct, on_delete=models.DO_NOTHING)


class Settings(models.Model):
    element = models.CharField(max_length=50)
    value = models.IntegerField()


class WishList(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)


class PasswordReset(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)


class DeActivatedSellers(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    reason = models.TextField()


class Variants(models.Model):
    name = models.CharField(max_length=150)
    variant_type = models.CharField(max_length=150)


class VariantOptions(models.Model):
    variant = models.ForeignKey(Variants, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Product_Variant_Options():
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    variant_option = models.ForeignKey(VariantOptions, on_delete=models.CASCADE)