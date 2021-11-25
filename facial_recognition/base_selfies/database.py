PHOTOS = [{
        'id': 0,
        'name': 'Thalys',
        'dir': './base_selfies/files/thalys.jpeg'
    }, {
        'id': 1,
        'name': 'Laura',
        'dir': './base_selfies/files/laura.jpeg'
    }

]

def get_db_images():
    return list(map(lambda x: x['id'], PHOTOS)), list(map(lambda x: x['dir'], PHOTOS))

def get_name_by_id(id: int):
    photos = list(filter(lambda x: x['id'] == id, PHOTOS))
    return photos[0]['name']

