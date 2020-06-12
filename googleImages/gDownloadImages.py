def downloadImages(query, num=1):

    from google_images_search import GoogleImagesSearch
    from json import load

    with open('credentials.json') as f:
        j = load(f)
    key = j['key']
    cx = j['cx']

    gis = GoogleImagesSearch(key, cx)

    _search_params = {
        'q': query,
        'num': num,
    }

    # assumes there is a folder with name images/query/
    gis.search(search_params=_search_params, path_to_dir='images/'+query)
