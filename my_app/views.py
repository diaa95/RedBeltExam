from django.shortcuts import render, redirect
from django.contrib import messages
from . import models
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    errors = models.User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user_id = models.registration(request.POST)
        request.session['logged_id'] = user_id
        return redirect(f"success/{user_id}")


def log_in(request):
    errors = models.User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        context = models.log_in(request.POST)
        if context['flag']:
            request.session['logged_id'] = context['this_user'].id
            return redirect(f"success/{context['this_user'].id}")
        else:
            messages.error(request, "you need to register")
            return redirect("/")


def log_out(request):
    del request.session['logged_id']
    return redirect('/')


def success(request, user_id):
    user = models.success(user_id)
    if request.session['logged_id'] == user['this_user'].id:
        return render(request, 'Home.html', user)
    else:
        return redirect('/')


def user_page(request, user_id):
    context = {
        'this_user': models.get_user(user_id),
        'all_quotes': models.get_users_quotes(user_id)
    }
    return render(request, "YourProfile.html", context)


def add_quote(request, user_id):
    errors = models.Quote.objects.add_quote_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/success/{user_id}")
    else:
        models.add_quote(user_id, request.POST)
        return redirect(f'/success/{user_id}')


def add_fav(request, quote_id, user_id):
    models.add_fav(quote_id, user_id)
    return redirect(f'/success/{user_id}')


def unfavorite(request, quote_id, user_id):
    models.unfavorite(quote_id, user_id)
    return redirect(f'/success/{user_id}')


def destroy(request, quote_id, user_id):
    models.destroy(quote_id)
    return redirect(f'/success/{user_id}')


def edit(request, user_id):
    context = {
        "this_user": models.get_user(user_id)
    }
    return render(request, 'edit.html', context)


def update(request, user_id):
    errors = models.User.objects.update_info_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/edit/{user_id}")
    else:
        models.update(request.POST, user_id)
        return redirect(f'/success/{user_id}')

#

