from django.db import models


class ImageUploadModel(models.Model):
    image_field = models.ImageField(upload_to="myuploads")
