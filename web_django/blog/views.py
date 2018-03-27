from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Hh_vacancy, Vacancy

def index(request):
    latest_vacancy_list = Hh_vacancy.objects.order_by('id')[:100]
    template = loader.get_template('blog/index.html')
    context = {
        'latest_vacancy_list': latest_vacancy_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, id):
    try:
        vacancy = Vacancy.objects.get(vacancy_id=id)
    except Vacancy.DoesNotExist:
        raise Http404("Vacnacy does not exist")
    return render(request, 'blog/detail.html', {'vacancy': vacancy})


def listing(request):
    vacancy_list =Hh_vacancy.objects.all()
    paginator = Paginator(vacancy_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    vacancy_p = paginator.get_page(page)
    return render(request, 'blog/index.html', {'vacancy_p': vacancy_p})