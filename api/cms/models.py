import uuid
from django.db import models

from api.account.models import User

# File Extension Validator
from django.core.validators import FileExtensionValidator


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=30,unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=30, db_index=True)
    body = models.CharField(max_length=300, db_index=True)
    summary = models.CharField(max_length=60, db_index=True)
    document = models.FileField(upload_to="document/", validators=[FileExtensionValidator(['pdf'])])
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
