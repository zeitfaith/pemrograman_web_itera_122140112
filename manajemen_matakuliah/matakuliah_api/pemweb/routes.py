def includeme(config):
    config.add_static_view(name='static', path='pemweb:static')
    config.add_route('home', '/')
    config.add_route('matakuliah_list', '/api/matakuliah')
    config.add_route('matakuliah_detail', '/api/matakuliah/{id}')
