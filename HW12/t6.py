import requests

query = 94485
while True:
    url = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?'
    response = requests.get(url, params={'nothing': f'{query}'})
    print(response.text)
    response_list = response.text.split()
    len_response_list = len(response_list)
    query = int(response_list[len_response_list - 1])
    print(query)

