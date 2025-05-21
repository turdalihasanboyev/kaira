from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SubEmail(BaseModel):
    email = models.EmailField(max_length=100, unique=True, db_index=True, help_text='Email address')

    def __str__(self):
        return f'{self.email}'
    
    class Meta:
        verbose_name = 'Sub Email'
        verbose_name_plural = 'Sub Emails'
