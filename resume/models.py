from django.db import models
from django.core.validators import MinValueValidator
from django.utils.html import format_html
from utils import (
    get_upload_path,
    current_year,
    max_value_current_year,
)


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ("order",)


class BasicInfo(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_picture = models.ImageField(
        default="avatar.jpg",
        upload_to=get_upload_path,
    )
    about_me = models.TextField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def profile_picture_tag(self):
        image_url = self.profile_picture.url
        return format_html(
            '<img src="%s"'
            ' width="60px" height="60px" style="border-radius:30px"/>' % image_url
        )

    profile_picture_tag.short_description = "Image"
    profile_picture_tag.allow_tags = True

    class Meta:
        get_latest_by = "updated_at"


class TechSkill(BaseModel):
    title = models.CharField(max_length=100)

    def skills(self):
        return self.title.split(",")

    def __str__(self) -> str:
        return self.title


class Stack(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class SocialMedia(BaseModel):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    link = models.CharField(max_length=255)

    def icon_tag(self):
        return format_html('<i class="%s"></i>' % self.icon)

    icon_tag.short_description = "Icon"
    icon_tag.allow_tags = True

    def __str__(self) -> str:
        return self.name


class Experience(BaseModel):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    logo = models.CharField(max_length=255, blank=True, null=True)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)
    technologies = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.title} - {self.company}"


class Review(BaseModel):
    client_name = models.CharField(max_length=255)
    country = models.CharField(max_length=100, null=True)
    comment = models.TextField()
    rate = models.PositiveSmallIntegerField(default=5)
    date = models.DateField()
    profile_picture = models.CharField(max_length=255, null=True, blank=True)

    def rate_list(self):
        return range(self.rate)

    def __str__(self) -> str:
        return f"{self.client_name} - {self.date}"


class Project(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.CharField(max_length=255, blank=True, null=True)
    technologies = models.CharField(max_length=255)

    def get_images(self):
        return self.images.values_list("image", flat=True)

    def __str__(self) -> str:
        return self.title


class ProjectImage(BaseModel):
    project = models.ForeignKey(
        Project,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to=get_upload_path,
    )

    def image_tag(self):
        image_url = self.image.url
        return format_html(
            '<img src="%s" height="150px"/>' % image_url
        )

    image_tag.short_description = "Image"
    image_tag.allow_tags = True

    def __str__(self) -> str:
        return f"{self.project} - {self.order}"


class CommonImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to=get_upload_path,
    )

    def image_tag(self):
        image_url = self.image.url
        return format_html(
            '<img src="%s" height="150px"/>' % image_url
        )

    image_tag.short_description = "Image"
    image_tag.allow_tags = True

    def __str__(self) -> str:
        return self.name


class Certificate(BaseModel):
    title = models.CharField(max_length=255)
    institute = models.CharField(max_length=255)
    year = models.PositiveIntegerField(
        default=current_year(),
        validators=[MinValueValidator(2000), max_value_current_year]
    )
    url = models.CharField(max_length=255)
    logo = models.ForeignKey(CommonImage, null=True, on_delete=models.SET_NULL)

    def logo_tag(self):
        if self.logo:
            image_url = self.logo.image.url
        else:
            image_url = ""
        return format_html(
            '<img src="%s"'
            ' width="60px" height="60px" style="border-radius:30px"/>' % image_url
        )

    logo_tag.short_description = "Logo"
    logo_tag.allow_tags = True

    def __str__(self) -> str:
        return self.title


class Publication(BaseModel):
    title = models.CharField(max_length=255, null=True)
    institute = models.CharField(max_length=255, null=True)
    date = models.DateField(null=True)
    url = models.CharField(max_length=255, null=True)
    logo = models.ForeignKey(CommonImage, null=True, on_delete=models.SET_NULL)

    def logo_tag(self):
        if self.logo:
            image_url = self.logo.image.url
        else:
            image_url = ""
        return format_html(
            '<img src="%s"'
            ' width="60px" height="60px" style="border-radius:30px"/>' % image_url
        )

    logo_tag.short_description = "Logo"
    logo_tag.allow_tags = True

    def __str__(self) -> str:
        return self.title


class Blog(BaseModel):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    image = models.ImageField(
        default="default_blog.jpg",
        upload_to=get_upload_path,
    )

    def __str__(self) -> str:
        return self.title


class Contact(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name


class Log(models.Model):
    ip_address = models.CharField(max_length=20, null=True)
    device_type = models.CharField(max_length=255, null=True)
    device_name = models.CharField(max_length=255, null=True)
    os = models.CharField(max_length=255, null=True)
    browser = models.CharField(max_length=255, null=True)
    login_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.ip_address
