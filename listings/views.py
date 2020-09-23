from django.shortcuts import render

from .models import Listing

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    ''' Listings of all the Property with little information '''
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    ''' Single listing page for more info about particular Property '''
    return render(request, 'listings/listing.html')


def search(request):
    ''' Search with specific requirement in all the listings '''
    return render(request, 'listings/search.html')


