from django.db import models

# Create your models here.

class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date',
        help_text='',
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date',
        help_text='',
    )

    class Meta: 
        abstract=True

class GeneralSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.',
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='',
    )
    parameters = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameters',
        help_text='',
    )

    def __str__(self) -> str:
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = ('General Setting')
        verbose_name_plural = ('General Settings')
        ordering = ('name', )

    
class ImageSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.',
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='',
    )
    file = models.ImageField(
        default='',
        blank=True,
        verbose_name='Image',
        help_text='',
        upload_to='images/'
    )

    def __str__(self) -> str:
        return f'Image Setting: {self.name}'

    class Meta:
        verbose_name = ('Image Setting')
        verbose_name_plural = ('Image Settings')
        ordering = ('name', )


class Experience(AbstractModel):
    company_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Company Name',
    )
    job_title = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Job Title',
    )
    job_period = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Job Period',
    )
    job_description = models.CharField(
        default='',
        max_length=750,
        blank=True,
        verbose_name='Job Description',
    )
    start_date = models.DateField(
        null=True,
        verbose_name='Start Date', 
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Date',
    )

    def __str__(self) -> str:
        return f'Experience: {self.company_name}'

    class Meta:
        verbose_name = ('Experience')
        verbose_name_plural = ('Experiences')
        ordering = ('-start_date', )