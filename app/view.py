'''
# Visualização
Arquivo responsável por gerar a interação entre o usuário e o programa por meio de alguma 
biblioteca como StreamLit, Python kivy ou Plotly Dash
'''

# Chama os métodos depreciação e financiamento da controller. 
# Eles serão os únicos meios de comunicação com o back do qual vocês terão que se preocupar.
from controller import depreciacao, financiamento

# Teste da função financiamento
dados_financiamento = financiamento(
    "carro",
    "Marca",
    "Modelo",
    "Ano",
    "Consumo",
    12,
    36,
    "mensal",
    10000
)

print("Dados do financiamento: ")
for parcela in dados_financiamento:
    print(f"{parcela[0]}º parcela: R${parcela[1]}")