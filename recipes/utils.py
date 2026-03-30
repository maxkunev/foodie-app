from django.core.paginator import Paginator

def get_pagination(recipes, page_number, recipe_number=10, N=2):
    paginator = Paginator(recipes, recipe_number)
    
    page_obj = paginator.get_page(page_number)
    
    current = page_obj.number
    total = paginator.num_pages

    start = current-N
    end = current+N
     
    if total<2*N+1:
        start = 1
        end = total
    elif start<1:
        end=1+2*N
        start=1
    elif end>total:
        start=total-2*N
        end=total
    
    window = list(range(start, end+1))
    
    return page_obj, window