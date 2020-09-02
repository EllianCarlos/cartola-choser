# Uma função greedy baseado na média de pontos e em um budget fixo
# Essa função retorna o custo de uma função
import math


def greedy(df, row = 0, paramToMaximize = "score_mean", budget = 100):
    ## Primeiro alguns filtros
    actual_row = df.illoc[[row]]
    
    if(actual_row["status"] != "Provável"):
        return math.inf
    # if(actual_row["stat;:us"] != ""):
