from django.shortcuts import render
from web.models import Testimonial,Promoter,Faq


def index(request):
    testimonials = Testimonial.objects.all()
    promoters = Promoter.objects.all()
    rent_tracking_faqs = Faq.objects.filter(faq_type="rent_tracking")
    new_deposit_faqs = Faq.objects.filter(faq_type="new_deposit")
    existing_deposit_faqs = Faq.objects.filter(faq_type="existing_deposit")

    print(testimonials)
    
    context = {
        "testimonials" : testimonials,
        "promoters" : promoters,
        "rent_tracking_faqs" : rent_tracking_faqs,
        "new_deposit_faqs" : new_deposit_faqs,
        "existing_deposit_faqs" : existing_deposit_faqs,
    }
    return render(request, "index.html",context=context)
