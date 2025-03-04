from django.shortcuts import redirect, render

from semi_rest_app.models import Show
from semi_rest_app.forms import UserForm


# Create your views here.

def index(request):
    context = {
        "shows" : Show.objects.all(),
    }
    return render (request, 'index.html', context)

def create(request):
    if request.method =='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            Show.objects.create(
                title = form.cleaned_data.get('title'),
                network = form.cleaned_data.get('network'),
                release_date = form.cleaned_data.get('release_date'),
                description = form.cleaned_data.get('description'),
                image_link = form.cleaned_data.get('url'),
            )
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = UserForm()
    return render(request, 'create.html',{"form":form})
    
def show(request, show_id):
    show = Show.objects.get(id = show_id)
    context = {
        "show": show
    }
    return render(request, 'show.html', context)

def delete(request, show_id):
    show = Show.objects.get(id = show_id)
    show.delete()
    return redirect('/')



def edit(request, show_id):
    if(request.method == 'GET'):
        show = Show.objects.get(id = show_id)
        context = {
        "show":show
    }
        return render(request, 'edit.html', context)
    else:
        show = Show.objects.get(id = show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.image_link = request.POST['url']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        return redirect(f"/show/{show_id}")
    
