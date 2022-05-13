from django.db import models

# Create your models here.
from .utils import unique_slug_generator

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    slug = models.CharField(max_length=80,unique=True,default='your full name')
    photo = models.ImageField(upload_to='profile')
    phone = models.CharField(max_length=20, blank=True,null=True)
    email = models.EmailField(max_length=254, unique=True,blank=True,null=True)
    dob = models.DateField(blank=True,null=True)

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)

    MARRIED = 'MA'
    WIDOWED = 'WI'
    SEPARATED = 'SE'
    DIVORCED = 'DI'
    SINGLE = 'SI'

    MARITAL_STATUS_CHOICES = [
        (MARRIED, 'Married'),
        (WIDOWED, 'Widowed'),
        (SEPARATED, 'Separated'),
        (DIVORCED, 'Divorced'),
        (SINGLE, 'Single'),
    ]
    marital_status = models.CharField(
        max_length=2,
        choices=MARITAL_STATUS_CHOICES,
        default=SINGLE,
    )

    enollment_id = models.CharField(max_length=30,blank=True, null=True)
    joining_date = models.DateField(blank=True, null=True)
    department   = models.CharField(max_length=256, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    reporting_employee = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)

    FULL_TIME = 'F'
    PART_TIME = 'P'
    CONTRACTUAL = 'C'
    TRAINEE = 'T'

    EMPLOYMENT_STATUS_CHOICES = (
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (CONTRACTUAL, 'Contractual'),
        (TRAINEE, 'Trainee'),
    )
    employment_type = models.CharField(max_length=1, choices=EMPLOYMENT_STATUS_CHOICES, default=FULL_TIME)

    address = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=20,blank=True,null=True)
    state = models.CharField(max_length=20,blank=True,null=True)
    zip_code = models.CharField(max_length=10,blank=True,null=True)
    country = models.CharField(max_length=20,blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)

    def save(self, **kwargs):
        slug = "%s-%s" % (self.first_name, self.last_name)
        self.slug = unique_slug_generator(self, slug)
        super(Employee, self).save(**kwargs)