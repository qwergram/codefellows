from random import randint
from .models import Image
from .forms import UploadImage, VoteForm
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views import generic
from django.utils import timezone
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .views_card import *

# Create your views here.

class IndexView(generic.base.TemplateView):
    template_name = 'compare/index.html'

class UploadView(generic.base.TemplateView):
    template_name = 'compare/upload.html'

class StatView(generic.ListView):
    model = Image
    # template_name = 'compare/stats.html'
    def get_context_data(self, **kwargs):
        context = super(StatView, self).get_context_data(**kwargs)
        context['length'] = len(Image.objects.all())
        context['showcase'] = Image.objects.all().order_by('-wins', 'loses')[:100]
        context['last'] = context['showcase'][0].pub_date
        return context

class IndividualStatView(generic.DetailView):
    model = Image
    template_name = 'compare/detail.html'

class CompareView(generic.View):

    def get(self, request):
        first_image = Image.objects.all()[randint(0, len(Image.objects.all())-1)]
        second_image = Image.objects.filter(~Q(pk=first_image.pk))[randint(0, len(Image.objects.all())-2)]
        context = {
            'first_image': first_image,
            'second_image': second_image
        }
        return render(request, 'compare/compare.html', context)

    def post(self, request):
        form = VoteForm(request.POST)
        if form.is_valid():
            winner = get_object_or_404(Image, pk=form.cleaned_data['winner'])
            loser = get_object_or_404(Image, pk=form.cleaned_data['loser'])
            winner.wins += 1
            loser.loses += 1
            winner.save()
            loser.save()
            return HttpResponseRedirect(reverse('compare:compare'))
        else:
            return HttpResponseRedirect(reverse('compare:compare'))

class PopularityView(CompareView):

    def get(self, request):
        first_image = Image.objects.order_by('-wins', 'loses')[:100][randint(0, len(Image.objects.order_by('-wins')[:100]) - 1)]
        second_image = Image.objects.order_by('-wins', 'loses').filter(~Q(pk=first_image.pk))[:100][randint(0, len(Image.objects.order_by('-wins')[:100]) - 2)]
        context = {
            'first_image': first_image,
            'second_image': second_image
        }
        return render(request, 'compare/popularity.html', context)

def upload_image(request):
    if request.method == 'POST':
        form = UploadImage(request.POST, request.FILES)
        if form.is_valid():
            instance = Image(
                image = request.FILES['image_file'],
                wins = 0, loses = 0,
                image_desc = request.POST['image_desc'],
                pub_date = timezone.now()
            )
            instance.save()
            return HttpResponseRedirect(reverse('compare:stats'))
        else:
            return HttpResponse('compare/upload.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse('compare:upload'))


# def vote(request, question_id):
#
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {'question': question, 'error_message': 'Invalid Choice'})
#
#     else:
#         choice.votes += 1
#         choice.save()
#
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
