from django.db import models


# Create your models here.

class Phone(models.Model):
    name = models.TextField()
    price = models.FloatField()
    os = models.TextField()
    battery = models.FloatField()
    dual_camera = models.BooleanField()
    img_preview = models.TextField(default='https://previews.123rf.com/images/alekseyvanin/alekseyvanin1811/al'
                                           'ekseyvanin181100948/111332068-unknown-phone-call-vector'
                                           '-icon-filled-flat-sign-for-mobile-concept-and-web-design-'
                                           'telephone-with-que.jpg')


class Apple(Phone):
    face_id = models.BooleanField()


class Samsung(Phone):
    two_screen = models.BooleanField()
