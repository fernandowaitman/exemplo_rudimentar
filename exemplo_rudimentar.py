from datetime import datetime

from dateutil.relativedelta import relativedelta
from xmltodict import parse
from pprint import pprint

xml_exemplo = '''
    <tag_externa atributo="1">
        valor externo
        <tag_intermediaria atributo="2">
            valor intermediario
            <tag_interna atributo="3">
                valor interno
            </tag_interna>
        </tag_intermediaria>
    </tag_externa>
    '''

def desloca_data_por_uma_quantidade_de_meses(qtde_meses, data=None):
    """Desloca uma determinada data pela quantidade de meses informada.

    Args:
        qtde_meses: int contendo a quantidade de meses que se deseja deslocar a data.
        data: datetime.date opcional contendo a data base. Caso nao informado, assume a data atual.

    Return:
        datetime.date contendo a data base deslocada pela quantidade de meses informada.
    """
    data = data or datetime.now().date()

    data_modificada = data + relativedelta(months=qtde_meses)
    
    print(data_modificada.strftime("%d/%m/%Y"))
    return data_modificada

def gera_e_imprime_dicionario_a_partir_de_xml(xml=xml_exemplo):
    """Gera e imprime um dicionario a partir de um xml.

    Args:
        xml: str opcional contendo um xml.

    Return:
        dict criado a partir do xml passado por parâmetro, ou do xml de exemplo, caso nenhum parâmetro for passado.
    """
    dicionario = parse(xml)
    
    pprint(dicionario)
    return dicionario


print('\nInvocando a função desloca_data_por_uma_quantidade_de_meses, com parâmetro 6: \n')
print('----')
desloca_data_por_uma_quantidade_de_meses(6)
print('----\n')

print('\nInvocando a função gera_e_imprime_dicionario_a_partir_de_xml: \n')
print('----')
gera_e_imprime_dicionario_a_partir_de_xml()
print('----\n')
