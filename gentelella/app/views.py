from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .regr_model.run_regr import predict
from django.views.decorators.csrf import csrf_exempt

def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


def gentella_html(request):
    context = {'abc':'abc'}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))

@csrf_exempt
def regr(request):
    test_x = request.POST
    result = predict(test_x)


    return JsonResponse(result, safe=False)