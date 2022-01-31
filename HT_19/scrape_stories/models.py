from django.db import models


class Ask(models.Model):
    # Possible fields: by, descendants, id, kids, score, text, time, title, type
    by = models.CharField(max_length=100, default=None, null=True)
    descendants = models.IntegerField(default=None)
    stories_id = models.IntegerField()
    score = models.IntegerField(default=None, null=True)
    time = models.IntegerField(default=None, null=True)
    title = models.CharField(max_length=150, default=None, null=True)
    type = models.CharField(max_length=20, default=None, null=True)
    text = models.TextField(default=None, null=True)

    def __str__(self):
        return str(self.stories_id)


class New(models.Model):
    # Possible fields: by, descendants, id, score, time, title, type, url, text, kids
    by = models.CharField(max_length=100, default=None, null=True)
    descendants = models.IntegerField(default=None)
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
    # Possible fields: by,id,score,time,title,type,url,text
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
    # Possible fields: by,descendants,id,kids,score,time,title,type,url,text
    by = models.CharField(max_length=100, default=None, null=True)
    descendants = models.IntegerField(default=None)
    stories_id = models.IntegerField()
    score = models.IntegerField(default=None, null=True)
    time = models.IntegerField(default=None, null=True)
    title = models.CharField(max_length=150, default=None, null=True)
    type = models.CharField(max_length=20, default=None, null=True)
    url = models.URLField(default=None, null=True)
    text = models.TextField(default=None, null=True)

    def __str__(self):
        return str(self.stories_id)
