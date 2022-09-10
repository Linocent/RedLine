import requests
import os
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from user_management.models import Discord
from .models import Categorie, Vehicule, Sales


def index(request):
    query = request.GET.get('query')
    vehicules = Vehicule.objects.all()
    if query:
        answer = Vehicule.objects.filter(nom__icontains=query)
        if answer.exists():
            if len(answer) > 1:
                return render(
                    request,
                    'redline_car/search.html',
                    {'answer': answer}
                )
            else:
                answer = Vehicule.objects.get(nom__icontains=query)
                return detail(request, answer.id, '')
        else:
            message = f"Aucun résultat trouvé pour {query}."
            return page_not_found(request, message)
    return render(request, "redline_car/index.html", {'vehicules': vehicules})


def search(request, category_id):
    answer = Vehicule.objects.filter(categorie=category_id)
    return render(
        request,
        'redline_car/search.html',
        {'answer': answer}
    )


def detail(request, vehicule_id, *args):
    vehicule = Vehicule.objects.filter(id__exact=vehicule_id)
    return render(
        request,
        'redline_car/detail.html',
        context={'vehicule': vehicule, 'msg': args},
    )


def vehicule(request):
    category = Categorie.objects.all()
    return render(
        request,
        'redline_car/vehicule.html',
        {'category': category}
    )


def page_not_found(request, message):
    return render(
        request,
        'redline_car/404.html',
        {'message': message}
    )


@login_required(login_url='log_in')
def order(request):
    if request.method == 'POST':
        car = request.POST.get('vehicule_id')
        car_ordered = Vehicule.objects.get(id__exact=car)
        user = request.user
        discord = Discord.objects.get(user=user)
        url = os.environ.get('DISCORDURL')  # noqa
        embed = {
            "description": f"{user.username} ({discord.discord_id}"
                           f") a commandé {car_ordered.nom} qui "
                           f"est une {car_ordered.categorie.nom}",
            "title": "Nouvelle commande",
        }
        data = {
            "username": "Commande ",
            "embeds": [
                embed
            ]
        }
        result = requests.post(url, json=data)
        print(result.status_code)
        if 200 <= result.status_code < 300:
            print(f"Webhook sent {result.status_code}")
            msg = 'Votre commande à bien été prise en ' \
                  'compte, un concessionaire vous ' \
                  'contactera pour la suite.'
            return detail(request, car, msg)
        else:
            print(f"Not sent with {result.status_code},"
                  f" response:\n{result.json()}")
            return HttpResponse(status=400)


@login_required(login_url='log_in')
def my_account(request):
    user = request.user
    identified_user = User.objects.get(username=user)
    username = str(user).replace('_', ' ')
    car_bought = Sales.objects.filter(buyer=identified_user)
    if car_bought.exists():
        return render(
            request,
            'redline_car/my_account.html',
            {'username': username, 'car_bought': car_bought},
        )
    else:
        message = "Vous n'avez pas encore acheté de véhicule " \
                  "chez nous.\n" \
                  "Nous sommes à votre disposition pour " \
                  "discuter de votre projet automobile."
        return render(
            request,
            'redline_car/my_account.html',
            {'username': username, 'message': message}
        )


def legal_mention(request):
    return render(request, 'redline_car/legal_mention.html')
