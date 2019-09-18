from django.shortcuts import render
from django.views.generic.detail import DetailView
from Course.models import Course, Lecture
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'course_detail.html'
    # Course.objects.filter(pk=id).update(status_course=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        context['lecture'] = Lecture.objects.filter(course=kwargs['object'])
        # Course.objects.filter(name=kwargs['object']).update(status_course=True)
        return context


def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=1000,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')


class LectureDetalView(DetailView):
    model = Lecture
    context_object_name = 'lecture'
    template_name = 'lecture_detail.html'

