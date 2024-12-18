import json

def valor_veiculo(tipo,marca,modelo,ano,consumo,):
    with open("db/db.json", "r", encoding="utf-8") as db_file:
        db = json.load(db_file)    
    
    if tipo not in db:
        return None        
    
    for veiculo in db[tipo]:
        if (veiculo['marca'] == marca and 
            veiculo['modelo'] == modelo and 
            veiculo['ano'] == ano and 
            veiculo['consumo'] == consumo):
            return veiculo['valor']
    
    return None
    
def calculo_depreciacao(
        tipo, 
        marca, 
        modelo, 
        ano,
        consumo,
    ):
    pass

def calculo_financiamento(
        valor_financiado, 
        taxa_de_juros_ao_ano, 
        numero_de_parcelas,
        tipo_de_parcela="mensal",
        tabela="PRICE",
        entrada=None,
    ):
    
    if entrada is not None:
        valor_financiado -= entrada
        
    taxa_de_juros_aa_decimal = taxa_de_juros_ao_ano / 100
    
    match tipo_de_parcela.lower():
        case "anual":
            taxa_de_juros_aa_d_por_parcela = taxa_de_juros_aa_decimal
        case "semestral":
            taxa_de_juros_aa_d_por_parcela = taxa_de_juros_aa_decimal / 2 
        case "trimestral":
            taxa_de_juros_aa_d_por_parcela = taxa_de_juros_aa_decimal / 4
        case "mensal":
            taxa_de_juros_aa_d_por_parcela = taxa_de_juros_aa_decimal / 12
        case _:
            raise ValueError("Tipo de parcelas inválido.")
    
    match tabela:
        case "PRICE":
            if taxa_de_juros_aa_d_por_parcela == 0:
                valor_parcela = valor_financiado / numero_de_parcelas
                parcelas = [(parcela + 1, valor_parcela) for parcela in range(numero_de_parcelas)]
            else:
                taxa_de_juros_acumulada = (taxa_de_juros_aa_d_por_parcela * (1 + taxa_de_juros_aa_d_por_parcela) ** numero_de_parcelas)
                valor_parcela = (
                    valor_financiado * 
                    (taxa_de_juros_aa_d_por_parcela * (1 + taxa_de_juros_aa_d_por_parcela) ** numero_de_parcelas) / 
                    ((1 + taxa_de_juros_aa_d_por_parcela) ** numero_de_parcelas - 1)
                    )
                parcelas = [(parcela + 1, round(valor_parcela, 2)) for parcela in range(numero_de_parcelas)]
            return tuple(parcelas)
            
        case "SAC":
            pass
        case _:
            pass