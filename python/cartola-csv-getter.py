import pandas as pd
import requests
import asyncio

async def generate_file():
    csv_file = requests.get('https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/2020/2020-medias-jogadores.csv').text
    try:
        f = open("../medias.csv", "w")
        f.write(csv_file)
        f.close()
    except:
        print("Erro ao salvar o arquivo")

    data = pd.read_csv("medias.csv")
    data = data.sort_values(by=['score_mean', 'status'], ascending=[False, False])
    #print(data.columns)
    #print(data.tail)
    #print(data.columns)
    print(data[["player_nickname", "score_mean", "price_cartoletas", "status"]])
    return data

asyncio.run(generate_file())
