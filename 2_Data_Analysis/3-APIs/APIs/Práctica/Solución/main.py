import pandas as pd
import variables as v
import functions as f
import math
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df_results_final = pd.DataFrame({'id':[],
                            'name':[],
                            'picture_url':[]})

letra_inicial = None # None para ver todos los personajes
response = f.llamar_api(v.priv_key,v.pub_key, letra_inicial)
number_requests = math.ceil(response["data"]["total"] / 100)

for n_requests in range(number_requests):
    response = f.llamar_api(v.priv_key,v.pub_key, letra_inicial,  offset= n_requests * 100)
    df = f.json_to_df(response)

    df_results_final = pd.concat([df_results_final, df], axis=0)
    print("Iteración no:", n_requests + 1)

df_results_final.reset_index(drop=True, inplace=True)
df_results_final.to_csv("marvel_characthers_final.csv")