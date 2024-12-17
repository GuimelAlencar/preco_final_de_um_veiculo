'''
# Controle
Arquivo responsável por gerenciar o relacionamento e o fluxo de informações entre a visualização, o processamento de dados, e a API da FIPE.
'''
from model import valor_veiculo
from model import calculo_depreciacao
from model import calculo_financiamento

def depreciacao(
        tipo_veiculo, 
        marca_veiculo, 
        modelo_veiculo, 
        ano_veiculo,
        consumo_veiculo,
    ):
    
    dados_depreciacao = calculo_depreciacao(
        tipo_veiculo, 
        marca_veiculo, 
        modelo_veiculo, 
        ano_veiculo,
        consumo_veiculo,
    )
    
    return dados_depreciacao 

def financiamento(
        tipo_veiculo, 
        marca_veiculo, 
        modelo_veiculo, 
        ano_veiculo,
        consumo_veiculo,
        taxa_de_juros_ao_ano, 
        numero_de_parcelas,
        tipo_de_parcela="mensal",
        tabela="PRICE",
        entrada=None,
    ):
    
    valor_veiculo_financiado = valor_veiculo(
        tipo_veiculo, 
        marca_veiculo, 
        modelo_veiculo, 
        ano_veiculo,
        consumo_veiculo,
    )
    
    dados_financiamento = calculo_financiamento(
        valor_veiculo_financiado,
        taxa_de_juros_ao_ano, 
        numero_de_parcelas,
        tipo_de_parcela,
        parcela, 
        entrada,
    )
    
    return dados_financiamento



