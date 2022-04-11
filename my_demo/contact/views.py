from django.shortcuts import render
from .forms import FriendForm

# Create your views here.
def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text" : "Hi my name is Bevo and I am a very good longhorn"
    }
    return render(request, "contact.html", my_context)

def contact_view(request):
    form = FriendForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = FriendForm()
    context = {
        'form': form
    }
    return render(request, "contact.html", context)
