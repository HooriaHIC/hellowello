from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import *
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .forms import *


class HomeView(TemplateView):
    template_name = "home.html"


class BlogView(ListView):
    model = Posts
    context_object_name = 'posts'
    template_name = "blog.html"


class BlogDetailView(DetailView):
    model = Posts
    template_name = "post_detail.html"


def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name', '')
            contact_email = request.POST.get(
                'contact_email', '')
            form_content = request.POST.get('content', '')
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "HelloWello" + '',
                ['hooria.hic@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            messages.info(request, "Your message has been send.")
            return redirect('/blog')
        else:
            messages.info(request, "Something went wrong. Try Again :(")
            return redirect('/')

    return render(request, 'contact.html', {
        'form': form_class,
    })
