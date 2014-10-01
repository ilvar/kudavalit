def evil(request):
    return {
        'evil': 'pizd.uy' in request.get_host() or 'evil' in request.GET,
    }