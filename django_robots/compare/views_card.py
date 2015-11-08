from random import randint
from .models import Image
from .forms import UploadImage, VoteForm
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext, loader
from django.views import generic
from django.utils import timezone
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, SignInForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

class CardsIndexView(generic.base.TemplateView):
    template_name = 'compare/cards_index.html'

# @csrf_protect
class SignIn(generic.View):

    def get(self, request):
        context = {}
        return render(request, 'compare/signin.html', context)

    @method_decorator(csrf_protect)
    def post(self, request):
        form = SignInForm(request.POST)
        context = {}

        if form.is_valid():
            context = form.cleaned_data
            auth_level = form.auth()
            if auth_level == 2:
                raise Exception('Coder confirmed for lazy faggot')
                return render(request, 'compare/404.html', context)
            elif auth_level == 1:
                context['errors'] = 'You have not confirmed your email yet!'
                return render(request, 'compare/signin.html', context)
            else:
                context['errors'] = 'I think you got your email/password mixed up!'
                return render(request, 'compare/signin.html', context)


class SignUp(generic.View):

    def get(self, request):
        context = {}
        return render(request, 'compare/signup.html', context)

    @method_decorator(csrf_protect)
    def post(self, request):
        form = SignUpForm(request.POST)
        context = {}
        if form.is_valid():
            context = form.cleaned_data
            if form.email_is_valid():
                if form.username_is_valid():
                    if form.passwords_match():
                        if form.passwords_meet_requirements():
                            user = User.objects.create_user(
                                first_name=form.cleaned_data['fname'],
                                last_name=form.cleaned_data['lname'],
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'],
                                email=form.cleaned_data['email'],
                                # is_active=False
                            )
                            user.is_active = False
                            user.save()
                            context['body_block'] = '<h1>An email has been sent to %s</h1><p>When you confirm your email you can log in</p>' % form.cleaned_data['email']
                            return render(request, 'compare/template.html', context)
                        else:
                            context['errors'] = 'Hey, your password isn\'t that strong.. Make it at <b>least</b> 8 characters!'
                    else:
                        context['errors'] = 'Check your fingers! Your passwords do not match'
                else:
                    context['errors'] = 'Yo! Sorry about that, but that username has been taken'
            else:
                context['errors'] = 'Did you mean to sign in? That email is already in use!'
        else:
            context['errors'] = 'I think your browser messed up... Try refreshing the page?'

        return render(request, 'compare/signup.html', context)
