from django.template.response import TemplateResponse


def index(request):
    return TemplateResponse(request, "index.html")


def process(request, action):
    return TemplateResponse(
        request,
        f"index.html#{action}-button",
        headers={"HX-Trigger-After-Swap": "trigger-edit"},
    )
