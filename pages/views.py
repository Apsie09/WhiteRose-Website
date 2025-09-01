from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ContactForm


def home(request):
    return render(request, 'home.html')


def technology(request):
    return render(request, 'technology.html')


def applications(request):
    return render(request, 'applications.html')


def partners(request):
    return render(request, 'partners.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email via console backend
            print(f"Contact form submission:")
            print(f"Name: {form.cleaned_data['name']}")
            print(f"Email: {form.cleaned_data['email']}")
            print(f"Message: {form.cleaned_data['message']}")
            
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


def privacy(request):
    return render(request, 'privacy.html')


def sitemap_xml(request):
    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url><loc>https://whiterose.example.com/</loc><priority>1.0</priority></url>
    <url><loc>https://whiterose.example.com/technology/</loc><priority>0.8</priority></url>
    <url><loc>https://whiterose.example.com/applications/</loc><priority>0.8</priority></url>
    <url><loc>https://whiterose.example.com/partners/</loc><priority>0.8</priority></url>
    <url><loc>https://whiterose.example.com/about/</loc><priority>0.8</priority></url>
    <url><loc>https://whiterose.example.com/contact/</loc><priority>0.7</priority></url>
    <url><loc>https://whiterose.example.com/privacy/</loc><priority>0.5</priority></url>
</urlset>'''
    return HttpResponse(xml_content, content_type='application/xml')


def robots_txt(request):
    txt_content = '''User-agent: *
Allow: /

Sitemap: https://whiterose.example.com/sitemap.xml'''
    return HttpResponse(txt_content, content_type='text/plain')
