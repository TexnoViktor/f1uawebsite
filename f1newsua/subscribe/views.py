from django.shortcuts import render, redirect
from .forms import FollowersForm


def follow(request):
    if request.method ==  'POST':
        form = FollowersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'введено неправильний імейл'

    form = FollowersForm()

    data = {
        'form': form
    }

    return render(request, 'subscribe/subscribe.html', data)
