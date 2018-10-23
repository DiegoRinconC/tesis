from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from prices.forms import SearchForm


def search(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/buscar/')

    else:
        form = SearchForm()

    return render(request, 'search_price.html', {"form":form})

