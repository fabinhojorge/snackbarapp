from django import template
from django.urls import reverse
from django.template import loader, Node, Variable

register = template.Library()


@register.simple_tag
def is_active(request, url):
    """Tag responsible to return if the path match with the current url"""
    if (reverse(url) in request.path and reverse(url) != '/') or request.path == reverse(url):
        return "active"
    return ""


@register.tag
def breadcrumb_url(parser, token):

    params = token.split_contents()
    params = [p.replace("'", "") for p in params[1:]]
    print(params)
    if len(params) % 2 == 0:
        raise ValueError('Number of arguments need to be Odd, in the format:'
                         ' \'breadcrumb_url title1 url1 title2 url2 title3\'')

    params.append(None)
    params = zip(params[::2], params[1::2])

    return BreadcrumbNode(params)


class BreadcrumbNode(Node):
    def __init__(self, params):
        self.crumb = params

    def render(self, context):
        breadcrumb = ""
        for c in self.crumb:
            tittle = c[0]
            url = c[1]
            try:
                tittle = Variable(tittle).resolve(context)
            except template.VariableDoesNotExist:
                pass
            breadcrumb = breadcrumb + str(create_crumb(tittle, url))
        return breadcrumb


def create_crumb(tittle, url):
    """" Helper function to design the Breadcrumb links"""
    if url:
        crumb = """<li class="breadcrumb-item"><a href="{1}">{0}</a></li>""".format(tittle, reverse(url))
    else:
        crumb = """<li class="breadcrumb-item active" aria-current="page">{0}</li>""".format(tittle)

    return crumb
