from django.shortcuts import render, get_object_or_404

from .models import Listing

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import state_choices, price_choices, bedroom_choices


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

    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    ''' Search with specific requirement in all the listings '''

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'listings/search.html', context)


