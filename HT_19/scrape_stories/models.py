from django.db import models


class Ask(models.Model):
    by = models.CharField(max_length=100, default=None, null=True)
    stories_id = models.IntegerField()
    score = models.IntegerField(default=None, null=True)
    time = models.IntegerField(default=None, null=True)
    title = models.CharField(max_length=150, default=None, null=True)
    type = models.CharField(max_length=20, default=None, null=True)
    url = models.URLField(default=None, null=True)
    text = models.TextField(default=None, null=True)

    def __str__(self):
        return str(self.stories_id)


class New(models.Model):
    by = models.CharField(max_length=100, default=None, null=True)
    stories_id = models.IntegerField()
    score = models.IntegerField(default=None, null=True)
    time = models.IntegerField(default=None, null=True)
    title = models.CharField(max_length=150, default=None, null=True)
    type = models.CharField(max_length=20, default=None, null=True)
    url = models.URLField(default=None, null=True)
    text = models.TextField(default=None, null=True)

    def __str__(self):
        return str(self.stories_id)


class Job(models.Model):
    by = models.CharField(max_length=100, default=None, null=True)
    stories_id = models.IntegerField()
    score = models.IntegerField(default=None, null=True)
    time = models.IntegerField(default=None, null=True)
    title = models.CharField(max_length=150, default=None, null=True)
    type = models.CharField(max_length=20, default=None, null=True)
    url = models.URLField(default=None, null=True)
    text = models.TextField(default=None, null=True)

    def __str__(self):
        return str(self.stories_id)


class Show(models.Model):
    by = models.CharField(max_length=100, default=None, null=True)
    stories_id = models.IntegerField()
    score = models.IntegerField(default=None, null=True)
    time = models.IntegerField(default=None, null=True)
    title = models.CharField(max_length=150, default=None, null=True)
    type = models.CharField(max_length=20, default=None, null=True)
    url = models.URLField(default=None, null=True)
    text = models.TextField(default=None, null=True)

    def __str__(self):
        return str(self.stories_id)
