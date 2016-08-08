from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    #role
    phone = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField()  
    address = models.CharField(max_length=200, blank=True, null=True)
    signup_date = models.DateTimeField('sign up date')
    has_sign_up = models.BooleanField(default=False)
    
    def __str__(self):
        return self.first_name + "," + self.last_name

class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    start_date = models.DateTimeField('sign up date')
    last_edit_date = models.DateTimeField('sign up date')

    def __str__(self):
        return self.title

class ServiceProvider(User):
    business_name = models.CharField(max_length=200)
    url = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.business_name



class Wedding(models.Model):
    name = models.CharField(max_length=200)
    spouse = models.ForeignKey(User, related_name='wedding_owner')
    budget = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    start_date = models.DateTimeField('start date', blank=True, null=True)
    wedding_date = models.DateTimeField('wedding date', blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    venue = models.CharField(max_length=200, blank=True, null=True)
    guest_list = models.ManyToManyField(User, related_name='wedding_guest', blank=True, null=True)
    note_list = models.ManyToManyField(Note, related_name='wedding_note', blank=True, null=True)

    def __str__(self):
        return self.name


    
class Event(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.DateTimeField('start_time', blank=True, null=True)
    end_time = models.DateTimeField('end_time', blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    owner = models.ForeignKey(User, related_name='event_owner')
    service_provider_list = models.ManyToManyField(ServiceProvider, related_name='event_service_provider', blank=True, null=True)
    helper_list = models.ManyToManyField(User, related_name='event_helper', blank=True, null=True)
    guest_list = models.ManyToManyField(User, related_name='event_guest', blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
