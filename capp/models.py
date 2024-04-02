from django.db import models
from datetime import datetime
# Create your models here.

class Music(models.Model):

    type = models.CharField(max_length=50, verbose_name='Music Type')

    class Meta:
        verbose_name = ("Music")
        verbose_name_plural = ("Musics")
        ordering = ['type']


    def __str__(self):
        return self.type

#--------------------------------------------------------------------------------

class Artist(models.Model):

    name = models.CharField(max_length=50, null=False)
    salary = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    youtube = models.CharField(max_length=50, null=True)
    youtube_link = models.URLField(max_length=200, null=True)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=True)
    nationality = models.CharField(max_length=50, null=True)
    birthdate = models.DateField(verbose_name='Birthdate Or Created Band', null=True)
    joined = models.DateTimeField(default=datetime.now)

    music = models.ManyToManyField(Music, verbose_name='Music Types')

    class Meta:
        verbose_name = ("Artist")
        verbose_name_plural = ("Artists")
        ordering = ['name']

    def __str__(self):
        return self.name

#--------------------------------------------------------------------------------


class Pros(models.Model):

    description = models.CharField(max_length=200)
    category = models.CharField(max_length=50, default='Allowed', choices=[
        ('allowed','Allowed'),
        ('not_allowed','Not Allowed'),
    ])

    class Meta:
        verbose_name = ("Pros")
        verbose_name_plural = ("Pros")

    def __str__(self):
        return self.description

#--------------------------------------------------------------------------------

class Plan(models.Model):

    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.IntegerField(default=0, verbose_name='save up tp')

    pros = models.ManyToManyField(Pros, verbose_name='Pros')

    class Meta:
        verbose_name = ("Plan")
        verbose_name_plural = ("Plans")
        ordering = ['name']

    def __str__(self):
        return self.name

#--------------------------------------------------------------------------------
class Party(models.Model):
    
    title = models.CharField(max_length=50)
    date = models.DateField(null=False, unique=True)
    time = models.TimeField(null=False)

    artist = models.ForeignKey(Artist, verbose_name='Artist', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = ("Party")
        verbose_name_plural = ("Parties")
        ordering = ['date']

    def __str__(self):
        return self.title

#--------------------------------------------------------------------------------

class Ticket(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254,null=True)
    phone = models.CharField(max_length=50,null=True)
    feedback = models.TextField(null=True)

    plan = models.ForeignKey(Plan, verbose_name='Ticket Type', on_delete=models.PROTECT, null=True)
    party = models.ForeignKey(Party, verbose_name='Party', on_delete=models.PROTECT, null=True)

    number = models.IntegerField(default=1)
    total = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        self.total = self.number * self.plan.price
        super(Ticket, self).save(*args, **kwargs)

    class Meta:
        verbose_name = ("Ticket")
        verbose_name_plural = ("Tickets")
        ordering = ['name']

    def __str__(self):
        return self.name
    
#--------------------------------------------------------------------------------

class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    company = models.CharField(max_length=50, null=True)
    message = models.TextField(null=True)

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")
        ordering = ['name']

    def __str__(self):
        return self.name
    
#--------------------------------------------------------------------------------

class About(models.Model):

    cjazz = models.TextField(verbose_name='About Cairo Jazz Club')
    developers = models.TextField(verbose_name='About Developers')
    technology = models.TextField(verbose_name='About Technology')

    class Meta:
        verbose_name = ("About")
        verbose_name_plural = ("About")

    def __str__(self):
        return 'About Us'