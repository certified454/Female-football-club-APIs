from django.db import models

# Create your models here.


class JoinForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    other_name = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100, default=None)
    guardian_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class SportGallery(models.Model):
    img = models.ImageField(upload_to='gallery/',
                            default=None, blank=True, null=True)
    player = models.CharField(max_length=50)
    caption = models.TextField()
    date_uploaded = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.player


class Team(models.Model):
    team_name = models.CharField(max_length=50)
    team_logo = models.ImageField(
        upload_to='team_img/', default=None, null=True, blank=True)
    head_coach = models.CharField(max_length=70)
    description = models.TextField()
    player = models.ForeignKey(
        SportGallery, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.team_name
