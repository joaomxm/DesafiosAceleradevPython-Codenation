from main import get_temperature
from unittest import mock
from unittest.mock import patch
import pytest

'''
Valores a serem utilizados no teste off-line

lat = -14.235004
lng = -51.92528
temperature = 62
expected = 16

'''

'''
Função que define a chave que queremos acessar no JSON da Requisição
e atribui um valor especifico como temperatura.
'''

def temperature_json(temp):
    temperature = {"currently": {"temperature": temp}}
    return temperature


'''
Função para manipular e simular valor padrao como resposta da API
utilizando a biblioteca unittest.mock

Recebe como parametro:
    -Latitude
    -Longitude
    -Temperatura
'''

# definindo o tipo da requisição(get) e o local
@mock.patch('main.requests.get')  # Iniciando o patch para ciração do mock
@pytest.mark.parametrize(
    "lat, lng, temp, expected",
    [(-91, -51.92528, 62, 16)]
)
def test_get_temperature_by_lat_lng(mock_requests, lat, lng, temp, expected):

    # verificando se a temperatura é valida
    if (type(temp) == int) or type(temp) == float:

        # Chamando a função que define os dados do JSON
        expected_result = temperature_json(temp)
    # Inserindo o valor desejado no Json da requisição
        mock_requests.return_value.json.return_value = expected_result

        result = get_temperature(lat, lng)
    # result = mock(lat, lng, temp)

    # Verificando  se o resultado obtido na requisição off-line
    # é igual ao esperado
        assert expected == result

    # caso a temperatura seja invalida
    else:
        assert ("Temp", temp) == "Invalid temperatures"

'''
Função para testar valores fora do range da latitude e longitude
'''

@pytest.mark.parametrize(
    "lat, lng",
    [(-104, -20), (91, -95), (-200, 300)]
)
def test_range_lat_lng_out(lat, lng):
    expected = {'code': 400, 'error': 'The given location is invalid.'}

    response = get_temperature(lat, lng)

    assert response == expected


'''
Função para testar valores que nao são validos 
'''

@pytest.mark.parametrize(
    "lat, lng",
    [('Test', 60), (False, -95), (None, None)]
)
def test_range_lat_lng_type(lat, lng):
    expected = {'code': 400, 'error': 'Poorly formatted request'}

    response = get_temperature(lat, lng)
    print(response)
    assert response == expected
