def downloadImages(query, num=1):

    from google_images_search import GoogleImagesSearch

    key = 'AIzaSyAVOyVYHvDOTNJQ9X_sJl9S3QTTYm77F94'
    cx = '010616554259021102261:ywlgqeepufu'
    gis = GoogleImagesSearch(key, cx)

    _search_params = {
        'q': query,
        'num': num,
    }

    print(_search_params)

    gis.search(search_params=_search_params, path_to_dir='images')
