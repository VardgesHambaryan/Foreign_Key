from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Category Name' , max_length=255)
    slug = models.SlugField(unique=True, max_length=255, null=True)

    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name='subcat')
    name = models.CharField('SubCategory Name' , max_length=255)


    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory , on_delete=models.CASCADE , related_name='prodcat')
    img = models.ImageField("Image", upload_to='media')
    name = models.CharField('Name' , max_length=255)
    price = models.PositiveIntegerField('Price')
    about = models.TextField("About Product", null=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"