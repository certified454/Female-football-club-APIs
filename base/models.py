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
    player = models.ManyToManyField(
        SportGallery)

    def __str__(self):
        return self.team_name


class Fixtures(models.Model):
    team1_logo = models.ImageField(
        upload_to='team1_logo/', default='media/images (6).jpeg')
    team2_logo = models.ImageField(
        upload_to='team2_logo/', null=True, blank=True)
    team1_name = models.CharField(max_length=50, null=True, blank=True)
    team2_name = models.CharField(max_length=50, null=True, blank=True)
    venue = models.CharField(max_length=50)
    kickoff = models.CharField(max_length=20)
    date_schedule = models.CharField(max_length=20)

    def __str__(self):
        return self.venue


class News(models.Model):
    post = models.FileField(upload_to='news_post/', default=None)
    capation = models.TextField()
    title = models.CharField(
        max_length=10, default=None, null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    post_id = models.AutoField(primary_key=True, default=None)

    def __str__(self) -> str:
        return self.capation
