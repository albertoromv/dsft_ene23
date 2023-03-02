import pandas as pd
from marvel import Marvel

def llamar_api(priv_key,pub_key, name_start, offset=0): ### Versión corta librería marvel
    m = Marvel(pub_key, priv_key)
    characters = m.characters
    if name_start == None:
       all_characters = characters.all(limit = 100, offset = offset)
    else:
       all_characters = characters.all(nameStartsWith="m", limit = 100, offset = offset) 

    return all_characters

def json_to_df(respuesta_json):
    marvel_dict = {"id": [],
                    "name": [],
                    "picture_url": []
                    }

    for elem in respuesta_json['data']['results']:
        marvel_dict['id'].append(elem.get('id','no_id'))
        marvel_dict['name'].append(elem.get('name','no_name'))
        url_pic = elem.get('thumbnail', 'no_thumbnail').get('path', 'no_path') + '.' + elem.get('thumbnail','no_thumbnail').get('extension', 'no_extension')
        marvel_dict['picture_url'].append(url_pic)

    df_results = pd.DataFrame(marvel_dict)
    return df_results