
from django.db import models

class Member(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    skills = models.TextField(blank=True, null=True, help_text="Comma-separated skills")
    goals = models.TextField(blank=True, null=True, help_text="Comma-separated goals")
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Media(models.Model):
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"
    MEDIA_TYPES = [(IMAGE, "Image"), (VIDEO, "Video")]

    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="media")
    type = models.CharField(max_length=10, choices=MEDIA_TYPES, default=IMAGE)
    # Allow both local file uploads and external URLs
    file = models.FileField(upload_to="uploads/", blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.name} - {self.type}"

    @property
    def display_url(self):
        if self.file:
            return self.file.url
        return self.url or ""

class Social(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="socials")
    platform = models.CharField(max_length=100)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.name} - {self.platform}"
