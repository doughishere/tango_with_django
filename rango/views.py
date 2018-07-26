from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")

def index(request):
    # Construct a dictionary of key/value pairs that we want to use within the template. Note the key 'boldmessage' is
    # the same as '{{ boldmessage }}' tag in the template.
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to the client. We make use of the shortcut function 'render(request,
    # template_name, context) in which the first parameter is the request object from the views parameter, the second
    # parameter is the template name to use and the third is a dictionary of anything we want to add to the template
    # context that will ultimately pass to the template engine.
    #
    # The render() function will take this data and mash it together with the template to produce a complete HTML page
    # that is returned with a HttpResponse. This response is then returned and dispatched to the user’s web browser.
    return render(request, 'rango/index.html', context_dict)


def about(request):
    # Construct a dictionary of key/value pairs that we want to use within the template. Note the key 'boldmessage' is
    # the same as '{{ boldmessage }}' tag in the template.
    context_dict = {'boldmessage': "This tutorial has been put together by Me!"}

    # The render() function will take this data and mash it together with the template to produce a complete HTML page
    # that is returned with a HttpResponse. This response is then returned and dispatched to the user’s web browser.
    return render(request, 'rango/about.html', context_dict)
