from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
from django.views.generic import View

# Create your views here.


# def citizen_kane(request):
#     # content = """{{movie}} was released in {{year}}"""
#     # template = Template(content)
#     # context = Context({"movie": "Citizen Kane", "year": 1941})
#     # result = template.render(context)
#     # return HttpResponse(result)
#     return


class CitizenKane(View):
    def get(self, request):
        context = {"movie": "Citizen Kane", "year": 1941}
        template_name = "simple.txt"
        return render(request, template_name=template_name, context=context)


def casablanca(request):
    return render(request, "simple.txt", {"movie": "Casablanca", "year": 1942})


def falcon(request):
    return render(
        request, "falcon.html", context={"movie": "Maltese Falcon", "year": 1941}
    )


def psycho(request):
    data = {
        "movie": "Psycho",
        "year": 1960,
        "is_scary": True,
        "color": False,
        "tomato_meter": 96,
        "tomato_audience": 95,
    }
    return render(request, "psycho.html", data)


# data as list of tuples, template renders as {{movie.0}}, and {{movie.1}} for name and year
def listing(request):
    data = {
        "movies": [
            (
                "citizen kane",
                1941,
            ),
            (
                "casablanca",
                1942,
            ),
            (
                "psycho",
                1960,
            ),
        ],
        "confectionaries": [("hot dog", 4), ("shake", 5)],
    }
    return render(request=request, template_name="listing.html", context=data)


# #data as list of dicts, template renders as {{movie.name}}, {{movie.year}}
# def listing(request):
#     data = {
#         "movies": [
#             {
#                 "name": "Citizen Kane",
#                 "year": 1941,
#             },
#             {
#                 "name": "Casablanca",
#                 "year": 1942,
#             },
#             {
#                 "name": "Psycho",
#                 "year": 1960,
#             },
#         ]
#     }
#     return render(request=request, template_name="listing.html", context=data)
