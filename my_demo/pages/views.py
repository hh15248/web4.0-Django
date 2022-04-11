from django.shortcuts import render

# Create your views here.

# Home page
def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html", {})

# About page
def about_view(request, *args, **kwargs):
    my_context = {
        "my_text" : "Hi my name is Bevo and I am a very good longhorn that likes to make friends. If you want to be my friend, let me know in the contact page!"
    }
    return render(request, "about.html", my_context)