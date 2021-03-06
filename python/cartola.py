import pandas as pd
import requests
import asyncio

async def atualizar_files():
    csv_file = requests.get('https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/2020/2020-medias-jogadores.csv').text
    try:
        f = open("../data/medias.csv", "w")
        f.write(csv_file)
        f.close()
    except:
        print("Erro ao salvar o arquivo")

async def generate_file():
    atualizar_files()
    data = pd.read_csv("medias.csv")
    data = data.sort_values(by=['score_mean', 'status'], ascending=[False, False])
    print(data[["player_nickname", "score_mean", "price_cartoletas", "status"]])
    return data

asyncio.run(generate_file())
