from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class Post(models.Model):
    author = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField()
    phone_number = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("film_detail", kwargs={
            "pk": self.pk
        })

    # class Meta:
    #     verbose_name = "Запрос"
    #     verbose_name_plural = "Запросы"
