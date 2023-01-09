from django.contrib import admin
from .models import *
from constance.admin import ConstanceAdmin, Config


class ConfigAdmin(ConstanceAdmin):
    change_list_template = 'admin/config/settings.html'


class BasicInfoAdmin(admin.ModelAdmin):

    list_display = [
        "profile_picture_tag",
        "first_name",
        "last_name",
        "about_me",
    ]


class StackAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "order",
        "is_active",
    ]


class TechSkillAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "order",
        "is_active",
    ]


class SocialMediaAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "icon_tag",
        "link",
        "order",
        "is_active",
    ]


class ExperienceAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "company",
        "from_date",
        "to_date",
        "order",
        "is_active",
    ]


class ReviewAdmin(admin.ModelAdmin):

    list_display = [
        "client_name",
        "country",
        "comment",
        "date",
        "order",
        "is_active",
    ]


class CertificateAdmin(admin.ModelAdmin):

    list_display = [
        "logo_tag",
        "title",
        "institute",
        "year",
        "order",
        "is_active",
    ]


class PublicationAdmin(admin.ModelAdmin):

    list_display = [
        "logo_tag",
        "title",
        "institute",
        "date",
        "order",
        "is_active",
    ]


class ProjectAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "order",
        "is_active",
    ]


class DemoAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "icon_tag",
        "url",
        "release_date",
        "order",
        "is_active",
    ]


class ProjectImageAdmin(admin.ModelAdmin):

    list_display = [
        "image_tag",
        "project",
        "order",
        "is_active",
    ]


class CommonImageAdmin(admin.ModelAdmin):

    list_display = [
        "image_tag",
        "name",
    ]


class BlogAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "url",
        "published_date",
        "order",
        "is_active",
    ]


class ContactAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "email",
        "subject",
        "message",
        "created_at",
    ]

    exclude = [
        "is_active",
        "order",
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False


class LogAdmin(admin.ModelAdmin):

    list_display = [
        "ip_address",
        "device_type",
        "device_name",
        "os",
        "browser",
        "login_at",
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False


admin.site.unregister([Config])
admin.site.register([Config], ConfigAdmin)

admin.site.register(BasicInfo, BasicInfoAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Stack, StackAdmin)
admin.site.register(TechSkill, TechSkillAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Demo, DemoAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
admin.site.register(CommonImage, CommonImageAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Log, LogAdmin)
