import vk
import time

def getStart():
    TOKEN = '' # НЕОБХОДИМО ПОЛУЧИТЬ ТОКЕН!!!
    session = vk.Session(access_token=TOKEN)
    #можно использовать эту авторизацию
    #session = vk.AuthSession(app_id='', user_login='*****', user_password='******', scope='messages')
    vk_api = vk.API(session)

    listIDs = []

    while True:
        time.sleep(3)

        msg = vk_api.messages.get(out='0')
        msg = msg[1:]

        for amsg in msg:
            if(amsg['title']==' ... '): #если наше сообщение лежит не в группе
                if(amsg['read_state']==0):
                   #получаем фамилию и имя того кто отправил нам сообщение
                   if listIDs.count(amsg['uid'])==0:
                        listIDs.append(amsg['uid'])
        for id in listIDs:
            nowP = vk_api.users.get(user_ids=id)
            people = nowP[0]['first_name']+' '+nowP[0]['last_name']
            
            print(people)
            #отвечаем
            vk_api.messages.send(message=people+", it's a bot. Wait my answ.",user_id=id)
            listIDs.remove(id)
getStart()
