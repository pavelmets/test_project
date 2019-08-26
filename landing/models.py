from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return "Пользователь %s с имейлом - %s" % (self.name, self.email)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'
