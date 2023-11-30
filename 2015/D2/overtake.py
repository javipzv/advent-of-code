import requests
import json
import time
 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'appToken': 'none',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/json;charset=utf-8',
    'Origin': 'https://www.riddle.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.riddle.com/embed/a/496744',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}
 
json_data = {
    'riddleId': 496744,
    'data': {
        'riddle': {
            'id': 496744,
            'title': 'VOTE FOR YOUR CRYPTO.COM OVERTAKE OF THE MONTH WINNER',
            'type': 'poll',
        },
        'answers': [
            {
                'question': 'VOTE FOR YOUR CRYPTO.COM OVERTAKE OF THE MONTH WINNER',
                'answer': 'Fernando Alonso (Brazil, vs Perez)',
                'questionId': 1,
                'answerId': 1,
            },
        ],
        'resultData': {
            'countAnswers': [
                None,
                1,
            ],
            'started': 1,
            'finished': 1,
            'resultId': 1,
            'resultIndex': 1,
        },
        'embed': {
            'parentLocation': 'https://www.formula1.com/en/latest/article.crypto-com-overtake-of-the-month-award.4NSk8Aciia1hOZ9QEmmSjq.html',
        },
        'timeTaken': 1,
    },
}
 
url = 'https://www.riddle.com/creator/integration/webhook/request'
 
# Función para realizar un número específico de tareas con un retraso entre ellas
def realizar_tareas_con_retraso(num_tareas, delay_ms):
    for i in range(num_tareas):
        try:
            response = requests.post(url, headers=headers, json=json_data)
            print('Tarea', i + 1, '- Código de estado:', response.status_code)
            print('Texto de la respuesta:', response.text)
            time.sleep(delay_ms / 1000)  # Convertir los milisegundos a segundos
        except requests.exceptions.RequestException as e:
            print('Error en la tarea', i + 1, ':', e)
 
# Especificar cuántas tareas realizar y el retraso entre ellas (en milisegundos)
num_tareas_a_realizar = 10000  # Cambiar al número deseado de tareas
retraso_entre_tareas_ms = 200  # Cambiar al retraso deseado entre tareas en milisegundos
 
# Llamar a la función para realizar las tareas con el retraso especificado
realizar_tareas_con_retraso(num_tareas_a_realizar, retraso_entre_tareas_ms)