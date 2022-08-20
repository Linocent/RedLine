from django.shortcuts import render
from .models import Categorie, Vehicule


def index(request):
    query = request.GET.get('query')
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
                detail(request, answer.id)
        else:
            message = f"Aucun résultat trouvé pour {query}."
            return page_not_found(request, message)
    return render(request, "redline_car/index.html")


def search(request, category_id):
    answer = Vehicule.objects.filter(categorie=category_id)
    print(answer)
    return render(
        request,
        'redline_car/search.html',
        {'answer': answer}
    )


def detail(request, vehicule_id):
    vehicule = Vehicule.objects.filter(id__exact=vehicule_id)
    print(vehicule)
    return render(
        request,
        'redline_car/detail.html',
        context={'vehicule': vehicule},
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
