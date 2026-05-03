from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def get_url_with_pag(context, page_number):
    request = context.get("request")
    query_get = request.GET
    
    query_new = query_get.copy()
    query_new['page']=page_number

    return query_new.urlencode()

