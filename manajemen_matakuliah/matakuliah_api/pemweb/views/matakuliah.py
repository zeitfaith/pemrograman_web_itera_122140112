from pyramid.view import view_config
from pyramid.response import Response
from ..models import Matakuliah

@view_config(route_name='matakuliah_list', renderer='json', request_method='GET')
def get_matakuliah(request):
    matakuliah = request.dbsession.query(Matakuliah).all()
    return [
        {
            'id': m.id,
            'kode_mk': m.kode_mk,
            'nama_mk': m.nama_mk,
            'sks': m.sks,
            'semester': m.semester
        } for m in matakuliah
    ]

@view_config(route_name='matakuliah_list', renderer='json', request_method='POST')
def add_matakuliah(request):
    data = request.json_body
    mk = Matakuliah(
        kode_mk=data['kode_mk'],
        nama_mk=data['nama_mk'],
        sks=data['sks'],
        semester=data['semester']
    )
    request.dbsession.add(mk)
    return {'status': 'success', 'message': 'Matakuliah ditambahkan'}

@view_config(route_name='matakuliah_detail', renderer='json', request_method='GET')
def get_matakuliah_detail(request):
    id = int(request.matchdict['id'])
    mk = request.dbsession.query(Matakuliah).filter_by(id=id).first()
    if mk:
        return {
            'id': mk.id,
            'kode_mk': mk.kode_mk,
            'nama_mk': mk.nama_mk,
            'sks': mk.sks,
            'semester': mk.semester
        }
    return Response(json_body={'error': 'Not found'}, status=404)

@view_config(route_name='matakuliah_detail', renderer='json', request_method='PUT')
def update_matakuliah(request):
    id = int(request.matchdict['id'])
    data = request.json_body
    mk = request.dbsession.query(Matakuliah).filter_by(id=id).first()
    if mk:
        mk.kode_mk = data['kode_mk']
        mk.nama_mk = data['nama_mk']
        mk.sks = data['sks']
        mk.semester = data['semester']
        return {'status': 'success', 'message': 'Matakuliah diperbarui'}
    return Response(json_body={'error': 'Not found'}, status=404)


@view_config(route_name='matakuliah_detail', renderer='json', request_method='DELETE')
def delete_matakuliah(request):
    id = int(request.matchdict['id'])
    mk = request.dbsession.query(Matakuliah).get(id)
    if mk:
        request.dbsession.delete(mk)
        return {'status': 'success', 'message': 'Matakuliah dihapus'}
    return Response(json_body={'error': 'Not found'}, status=404)
