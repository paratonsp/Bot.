import time
import requests
import pandas

count = 0

excel_data = pandas.read_excel('List Data.xlsx', sheet_name='Data')
API_ENDPOINT_SEND = "http://103.183.75.212:3000/api/sendText"

for column in excel_data['Name'].tolist():
    message = excel_data['Message'][0]
    person = str(excel_data['Contact'][count])
    message = message.replace('{customer_name}', column)
    contact = person + '@c.us'

    data = {'chatId': contact, 'text': message, 'session': 'default'}

    res = requests.post(url=API_ENDPOINT_SEND, data=data)
    print('STATUS: ' + str(res.status_code) + ' | Send to ' + column)

    count = count + 1
    time.sleep(3)

print('TOTAL: ' + str(count))
