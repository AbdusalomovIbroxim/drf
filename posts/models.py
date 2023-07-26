from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    parent_category = models.ForeignKey('self', null=True, blank=True, related_name='subcategories',
                                        on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    parent_country = models.ForeignKey('self', null=True, blank=True, related_name='cities',
                                       on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField()
    phone_number = models.CharField(max_length=20)
    # image = models.ImageField("Картинка", upload_to="product-images/", blank=True, null=True)
    # view_count = models.PositiveBigIntegerField("Количество просмотров", default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # city = models.ForeignKey(City, on_delete=models.CASCADE)
    status = models.CharField(max_length=4, default='BUY')
    is_published = models.BooleanField("Опубликовано", default=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("film_detail", kwargs={
            "pk": self.pk
        })

    # class Meta:
    #     verbose_name = "Запрос"
    #     verbose_name_plural = "Запросы"
