from django.contrib import admin
from web.models import Testimonial,Promoter,Faq,Subscribe


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id","name", "description","image","designation"]

admin.site.register(Testimonial,TestimonialAdmin)


class PromoterAdmin(admin.ModelAdmin):
    list_display = ["id","name", "image"]

admin.site.register(Promoter,PromoterAdmin)


class FaqAdmin(admin.ModelAdmin):
    list_display = ["id","title", "faq_type","description"]

admin.site.register(Faq,FaqAdmin)


admin.site.register(Subscribe)