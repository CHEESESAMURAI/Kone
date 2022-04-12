import sqlite3
from aiogram import Bot, Dispatcher, executor, types
import time

import config
import markups as kb

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)


kur_id = [405968842,405968842,405968842]
meto_id = [1659228199]

dialog1=[]
dialog2=[]
dialog3=[]

kur_user=[]

idd=0
pas = 0
b = 0
ran = 0
nextbackkur=0
nextback = 0

base3 = sqlite3.connect('admin.db')
cur3 = base3.cursor()

base2 = sqlite3.connect('messages.db')
cur2 = base2.cursor()

base = sqlite3.connect('table.db')
cur = base.cursor()


base3.execute('CREATE TABLE IF NOT EXISTS {}(idd,id,username,role,state,dop)'.format('data3'))
base3.commit()


base2.execute('CREATE TABLE IF NOT EXISTS {}(idd,id,username,role,answer,question,rate,comment)'.format('data2'))
base2.commit()

base.execute('CREATE TABLE IF NOT EXISTS {}(id PRIMARY KEY,username,number,firstname,lastname,login ,password,state,aut,reg,otv)'.format('data'))
base.commit()


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    us_id = message.from_user.id
    user = message.from_user.username
    firstname = cur.execute('SELECT firstname FROM data WHERE id == ?', (us_id,)).fetchone()

    if message.from_user.username == None:
        user = '0'


    if firstname==None:
        await bot.send_message(message.chat.id, 'Перед началом использования бота,'
                                                ' Зарегистрируйтесь или Авторизуйтесь', reply_markup=kb.main)
        await bot.delete_message(message.chat.id, message.message_id)
        cur.execute('INSERT INTO data VALUES(?,?,?,?,?,?,?,?,?,?,?)',
                    (message.from_user.id, user, '0', 'ученик', '0', '0', '0', '0', '0', '0', '0'))
        base.commit()
    if str(firstname[0]) == 'куратор':
        await bot.send_message(message.chat.id, 'Перед началом использования бота,'
                                                ' Зарегистрируйтесь или Авторизуйтесь', reply_markup=kb.mainkur)
    if str(firstname[0]) == 'наставник':
        await bot.send_message(message.chat.id, 'Перед началом использования бота,'
                                                ' Зарегистрируйтесь или Авторизуйтесь', reply_markup=kb.mainknast)
    if str(firstname[0]) == 'ученик':
        await bot.send_message(message.chat.id,'Перед началом использования бота,'
                                               ' Зарегистрируйтесь или Авторизуйтесь',reply_markup=kb.main)
        await bot.delete_message(message.chat.id, message.message_id)






@dp.callback_query_handler(text='aut')
async def ask(message: types.Message):
    us_id = message.from_user.id
    aut = cur.execute('SELECT aut FROM data WHERE id == ?', (us_id,)).fetchone()
    if int(aut[0]) >= 2:
        await bot.delete_message(message.from_user.id, message.message.message_id)
        await bot.send_message(message.from_user.id, 'Вы уже автиризировались', reply_markup=kb.main)
    else:
        await bot.delete_message(message.from_user.id,message.message.message_id)
        await bot.send_message(message.from_user.id,'Выберети , что хотите ввести ?',reply_markup=kb.logpass)


@dp.callback_query_handler(text='log')
async def ask(message: types.Message):
    us_id = message.from_user.id
    log = cur.execute('SELECT login FROM data WHERE id == ?', (us_id,)).fetchone()
    if log[0] == '0':
        await bot.delete_message(message.from_user.id, message.message.message_id)
        await bot.send_message(message.from_user.id,'Вы еще не зарегестрировались',reply_markup=kb.main)
    else:
        await bot.delete_message(message.from_user.id,message.message.message_id)
        await bot.send_message(message.from_user.id,'Введите ваш логин')


    cur.execute('UPDATE data SET state == ? WHERE id == ?', (1,us_id))
    base.commit()


@dp.callback_query_handler(text='reg')
async def ask(message: types.Message):
    us_id = message.from_user.id
    reg = cur.execute('SELECT reg FROM data WHERE id == ?', (us_id,)).fetchone()
    if reg == None:
        await bot.delete_message(message.from_user.id, message.message.message_id)
        await bot.send_message(message.from_user.id, 'Введите логин , который хотели бы иметь ?')

    elif int(reg[0]) == 3:
        await bot.delete_message(message.from_user.id, message.message.message_id)
        await bot.send_message(message.from_user.id,'Вы уже зарегестрировались!',reply_markup=kb.main)
    else:
        await bot.delete_message(message.from_user.id,message.message.message_id)
        await bot.send_message(message.from_user.id,'Введите логин , который хотели бы иметь ?')


    cur.execute('UPDATE data SET state == ? WHERE id == ?', (2, us_id))
    base.commit()

@dp.callback_query_handler(text='ask')
async def ask(message: types.Message):
    us_id = message.from_user.id
    # an = cur.execute('SELECT question FROM data2').fetchall()
    if idd >= 1 :
        an = cur.execute('SELECT otv FROM data WHERE id == ?', (us_id,)).fetchone()
        if '0' == an[0]:
            await bot.delete_message(message.from_user.id, message.message.message_id)
            await bot.send_message(message.from_user.id,'Сначала дождитесь ответ на свой вопрос , а потом задавайте еще')

        elif '0' != an[0]:
            await bot.delete_message(message.from_user.id, message.message.message_id)
            await bot.send_message(message.from_user.id,
                                           'Введите ваш номер телефона')
            # cur2.execute('INSERT INTO data2 VALUES(?,?,?,?,?,?,?,?)',
            #                      (idd, message.from_user.id, message.from_user.username, '0', '0', '0', '0', '0'))
            # base2.commit()
    else:
        await bot.delete_message(message.from_user.id,message.message.message_id)
        await bot.send_message(message.from_user.id,'Опишите подробнее ваш впорос в одном сообщение и отправьте сюда !')
        cur2.execute('INSERT INTO data2 VALUES(?,?,?,?,?,?,?,?)', (idd, message.from_user.id, message.from_user.username, '0', '0', '0', '0', '0'))
        base2.commit()

    us_id = message.from_user.id

    cur.execute('UPDATE data SET state == ? WHERE id == ?', (3, us_id))
    base.commit()




@dp.callback_query_handler(text='nast_otv')
async def ask(message: types.Message):
    global idd
    global ran
    us_id = message.from_user.id
    await bot.send_message(int(meto_id[0]), 'Введите ответ и я отправлю его, либо позже ответие из списка, номер в списке :'+str(idd))
    cur2.execute('UPDATE data2 SET role == ? WHERE idd == ?', (kur_id[ran], idd))
    base2.commit()
    otv = cur.execute('SELECT otv FROM data WHERE id == ?', (us_id,)).fetchone()
    print(otv)


@dp.callback_query_handler(text='otv')
async def ask(message: types.Message):
    global idd
    global ran
    us_id = message.from_user.id
    await bot.send_message(kur_id[ran], 'Введите ответ и я отправлю его, либо позже ответие из списка, номер в списке :'+str(idd))
    cur.execute('UPDATE data SET otv == ? WHERE id == ?', (1, us_id))
    base.commit()
    cur2.execute('UPDATE data2 SET role == ? WHERE idd == ?', (kur_id[ran], idd))
    base2.commit()
    otv = cur.execute('SELECT otv FROM data WHERE id == ?', (us_id,)).fetchone()
    print(otv)

    # keyboard = types.InlineKeyboardMarkup(row_width=1)
    # for i in range(idd):
    #     i = types.InlineKeyboardButton(text=i+1,callback_data=i)
    #     keyboard.add(i)
    # que = cur.execute('SELECT id FROM data2 WHERE idd == ?', (idd,)).fetchone()


@dp.callback_query_handler(text='1')
async def star(message: types.Message):
    await bot.send_message(message.from_user.id, 'Если вам , что-то не понравилось , то оставьте ОСТАВИТЬ ОТЗЫВ', reply_markup=kb.feedback)
    cur2.execute('UPDATE data2 SET rate == ? WHERE id == idd', (1, idd-1))
    base2.commit()
    cur.execute('UPDATE data SET otv == ? WHERE id == ?', (1, kur_id[0]))
    cur.execute('UPDATE data SET otv == ? WHERE id == ?', (1,message.from_user.id))
    base.commit()

@dp.callback_query_handler(text='2')
async def star(message: types.Message):
    await bot.send_message(message.from_user.id, 'Если вам , что-то не понравилось , то нажмите ОСТАВИТЬ ОТЗЫВ', reply_markup=kb.feedback)
    cur2.execute('UPDATE data2 SET rate == ? WHERE idd == ?', (2,idd-1))
    base2.commit()
    print(idd)
    cur.execute('UPDATE data SET otv == ? WHERE id == ?', (1, kur_id[0]))
    cur.execute('UPDATE data SET otv == ? WHERE id == ?', (1,message.from_user.id))
    base.commit()

@dp.callback_query_handler(text='lkn')
async def lkn(message: types.Message):
    us_id = message.from_user.id
    log = cur.execute('SELECT login FROM data WHERE id == ?', (us_id,)).fetchone()
    number = cur.execute('SELECT number FROM data WHERE id == ?', (us_id,)).fetchone()
    firstname = cur.execute('SELECT firstname FROM data WHERE id == ?', (us_id,)).fetchone()
    await bot.delete_message(message.from_user.id,message.message.message_id)
    await bot.send_message(message.from_user.id, 'Ваши данные:\n'
                                                 'Ваш id в Телеграме:'+str(message.from_user.id)+'\n'
                                                                                            'Ваш логин для ваход :' +str(log[0] +'\nВаш номер телефона \n' + str(number[0]) + '\nВаш статус\n'+str(firstname[0])),reply_markup=kb.main)


@dp.callback_query_handler(text='3')
async def star(message: types.Message):
    await bot.send_message(message.from_user.id,'Благодарим за оценку',reply_markup=kb.ask)
    cur2.execute('UPDATE data2 SET rate == ? WHERE idd == ?', (3,idd-1))
    base2.commit()
    cur.execute('UPDATE data SET otv == ? WHERE id == ?', (1, kur_id[0]))
    cur.execute('UPDATE data SET otv == ? WHERE id == ?', (1,message.from_user.id))
    base.commit()

@dp.callback_query_handler(text='4')
async def star(message: types.Message):
    await bot.send_message(message.from_user.id, 'Благодарим за оценку', reply_markup=kb.ask)
    cur2.execute('UPDATE data2 SET rate == ? WHERE idd == ?', (4,idd-1))
    base2.commit()
    cur.execute('UPDATE data SET otv == ? WHERE id == ?', (1, kur_id[0]))
    cur.execute('UPDATE data SET otv == ? WHERE id == ?', (1,message.from_user.id))
    base.commit()

@dp.callback_query_handler(text='5')
async def star(message: types.Message):
    await bot.send_message(message.from_user.id, 'Благодарим за оценку', reply_markup=kb.ask)
    cur2.execute('UPDATE data2 SET rate == ? WHERE idd == ?', (5,idd-1))
    base2.commit()
    cur.execute('UPDATE data SET otv == ? WHERE id == ?', (1, kur_id[0]))
    cur.execute('UPDATE data SET otv == ? WHERE id == ?', (1,message.from_user.id))
    base.commit()

@dp.callback_query_handler(text='feedback')
async def star(message: types.Message):
    await bot.send_message(message.from_user.id,'Введите подробно , что вам не понравилось и мы исправим это')
    cur.execute('UPDATE data SET state == ? WHERE id == ?', (4, message.from_user.id))
    base.commit()
    cur.execute('UPDATE data SET lastname == ? WHERE id == ?', ('0', kur_id[0]))
    base.commit()
    cur.execute('UPDATE data SET lastname == ? WHERE id == ?', ('0', message.from_user.id))
    base.commit()

@dp.callback_query_handler(text='endit')
async def star(message: types.Message):
    global ran
    global idd
    us_id = message.from_user.id
    await bot.send_message(message.from_user.id,'Спасибо за обращение !\nОцените ответ от куратора по пятибаольной шкале :\n1-очень плохо \n5-Превосходно',reply_markup=kb.star)
    cur.execute('UPDATE data SET otv == ? WHERE id == ?', (0, kur_id[0]))
    cur.execute('UPDATE data SET otv == ? WHERE id == ?', (0, us_id))
    base.commit()
    await bot.send_message(kur_id[0],'Ученик закончил ваш диалог и все !',reply_markup=kb.mainkur)
    print(dialog1)

    ran += 1
    if ran == 3:
        ran = 0
@dp.callback_query_handler(text='kurspisok')
async def star(message: types.Message):
    global nextbackkur
    nextbackkur = 0
    otv = cur2.execute('SELECT answer FROM data2 WHERE idd == ?', (nextbackkur,)).fetchone()
    vop = cur2.execute('SELECT question FROM data2 WHERE idd == ?', (nextbackkur,)).fetchone()
    rat = cur2.execute('SELECT rate FROM data2 WHERE idd == ?', (nextbackkur,)).fetchone()
    otz = cur2.execute('SELECT comment FROM data2 WHERE idd == ?', (nextbackkur,)).fetchone()
    await bot.send_message(message.from_user.id, 'Список сообщений !\n' + 'Вопрос\n' + str(vop[0]) +'\nОтвет на данный вопрос\n'+ str(otv[0])+'\nОценка данного ответа\n'+ str(rat[0])+'\nОтзыв на ответ\n'+ str(otz[0]),
                               reply_markup=kb.nextbackkur)


@dp.callback_query_handler(text='nextkur')
async def star(message: types.Message):
    global nextbackkur
    nextbackkur+=1
    otv = cur2.execute('SELECT answer FROM data2 WHERE idd == ?', (nextbackkur,)).fetchone()
    vop = cur2.execute('SELECT question FROM data2 WHERE idd == ?', (nextbackkur,)).fetchone()
    rat = cur2.execute('SELECT rate FROM data2 WHERE idd == ?', (nextbackkur,)).fetchone()
    otz = cur2.execute('SELECT comment FROM data2 WHERE idd == ?', (nextbackkur,)).fetchone()
    await bot.send_message(message.from_user.id,
                           'Список сообщений !\n' + 'Вопрос\n' + str(vop[0]) + '\nОтвет на данный вопрос\n' + str(
                               otv[0]) + '\nОценка данного ответа\n' + str(rat[0]) + '\nОтзыв на ответ\n' + str(otz[0]),
                           reply_markup=kb.nextbackkur)


@dp.callback_query_handler(text='backkur')
async def star(message: types.Message):
    global nextbackkur
    nextbackkur-=1
    otv = cur2.execute('SELECT answer FROM data2 WHERE idd == ?', (nextbackkur,)).fetchone()
    vop = cur2.execute('SELECT question FROM data2 WHERE idd == ?', (nextbackkur,)).fetchone()
    rat = cur2.execute('SELECT rate FROM data2 WHERE idd == ?', (nextbackkur,)).fetchone()
    otz = cur2.execute('SELECT comment FROM data2 WHERE idd == ?', (nextbackkur,)).fetchone()
    await bot.send_message(message.from_user.id,
                           'Список сообщений !\n' + 'Вопрос\n' + str(vop[0]) + '\nОтвет на данный вопрос\n' + str(
                               otv[0]) + '\nОценка данного ответа\n' + str(rat[0]) + '\nОтзыв на ответ\n' + str(otz[0]),
                           reply_markup=kb.nextbackkur)

@dp.callback_query_handler(text='spisok')
async def star(message: types.Message):
    global nextback
    moe_id = message.from_user.id
    moe = cur2.execute('SELECT id FROM data2 WHERE idd == ?', (nextback,)).fetchone()
    print(int(moe[0]))

    while int(moe[0]) != moe_id:
        nextback+=1
    if int(moe[0]) == moe_id:
        a = []
        otv = cur2.execute('SELECT answer FROM data2 WHERE idd == ?', (nextback,)).fetchone()
        vop = cur2.execute('SELECT question FROM data2 WHERE idd == ?', (nextback,)).fetchone()
        a.append(otv)
        a.append(vop)
        await bot.send_message(message.from_user.id, 'Список сообщений !\n' + 'Вопрос\n' + str(vop[0]) +'\nОтвет на данный вопрос\n'+ str(otv[0]),
                               reply_markup=kb.nextback)



@dp.callback_query_handler(text='next')
async def star(message: types.Message):
    global nextback
    nextback+=1
    moe_id = message.from_user.id
    moe = cur2.execute('SELECT id FROM data2 WHERE idd == ?', (nextback,)).fetchone()
    print(int(moe[0]))
    while int(moe[0]) != moe_id:
        nextback += 1
    if int(moe[0]) == moe_id:
        otv = cur2.execute('SELECT answer FROM data2 WHERE idd == ?', (nextback,)).fetchone()
        vop = cur2.execute('SELECT question FROM data2 WHERE idd == ?', (nextback,)).fetchone()
        await bot.send_message(message.from_user.id,
                               'Список сообщений !\n' + 'Вопрос\n' + str(vop[0]) + '\nОтвет на данный вопрос\n' + str(otv[0]),
                               reply_markup=kb.nextback)


@dp.callback_query_handler(text='back')
async def star(message: types.Message):
    global nextback
    nextback-=1
    moe_id = message.from_user.id
    moe = cur2.execute('SELECT id FROM data2 WHERE idd == ?', (nextback,)).fetchone()
    print(int(moe[0]))
    while int(moe[0]) != moe_id:
        nextback += 1
    if int(moe[0]) == moe_id:
        otv = cur2.execute('SELECT answer FROM data2 WHERE idd == ?', (nextback,)).fetchone()
        vop = cur2.execute('SELECT question FROM data2 WHERE idd == ?', (nextback,)).fetchone()
        await bot.send_message(message.from_user.id,
                               'Список сообщений !\n' + 'Вопрос\n' + str(vop[0]) + '\nОтвет на данный вопрос\n' + str(otv[0]),
                               reply_markup=kb.nextback)


@dp.message_handler(content_types=types.ContentTypes.ANY)
async def all_other_messages(message: types.Message):
    global ran
    global idd
    global dialog1
    global dialog2
    global dialog
    global kur_user

    us_id = message.from_user.id

    r = cur.execute('SELECT state FROM data WHERE id == ?', (us_id,)).fetchone()
    aut = cur.execute('SELECT aut FROM data WHERE id == ?', (us_id,)).fetchone()
    reg = cur.execute('SELECT reg FROM data WHERE id == ?', (us_id,)).fetchone()
    otv = cur.execute('SELECT otv FROM data WHERE id == ?', (us_id,)).fetchone()
    lastname = cur.execute('SELECT lastname FROM data WHERE id == ?', (us_id,)).fetchone()
    firstname = cur.execute('SELECT firstname FROM data WHERE id == ?', (us_id,)).fetchone()
    number = cur.execute('SELECT number FROM data WHERE id == ?', (us_id,)).fetchone()


    mes = message.text
    mesid = message.message_id
#Отзыв
    if str(firstname[0]) == 'ученик' and int(r[0])==4 and int(reg[0])== 3 and int(aut[0])>=2:
        await bot.send_message(message.chat.id, 'Ваш отзыв записан, что бы задать еще вопрос , то нажмите "Задать вопрос", а что бы посмотреть все вопросы и ответы , то нажмите "Список вопросов и ответов"',reply_markup=kb.ask)
        print(idd)
        print(message.text)
        cur2.execute('UPDATE data2 SET comment == ? WHERE idd == ?', (message.text, idd-1))
        base2.commit()
        cur.execute('UPDATE data SET state == ? WHERE id == ?', (3, message.from_user.id))
        cur.execute('UPDATE data SET otv == ? WHERE id == ?', (0, kur_id[0]))
        cur.execute('UPDATE data SET otv == ? WHERE id == ?', (0, us_id))
        base.commit()

#Ответ куратора

    if str(firstname[0]) == 'куратор' and int(otv[0])==1 and int(reg[0]) == 3 and int(aut[0])>=2:


        # keyboard = types.InlineKeyboardMarkup(row_width=1)
        # for i in kur_user:
        #     i = types.InlineKeyboardButton(text=kur_user[i],callback_data=kur_user[i])
        # keyboard.add(i)

        cur2.execute('UPDATE data2 SET question == ? WHERE idd == ?', (message.text, idd))
        base2.commit()

        g = list(message.text)

        g2 = g[0]
        print(g2)
        id_who = cur2.execute('SELECT id FROM data2 WHERE idd == ?', (int(g2),)).fetchone()
        print(id_who)
        # who_id = cur2.execute('SELECT id FROM data2').fetchall()
        # who = cur2.execute('SELECT answer FROM data2').fetchall()
        # print(list(who))
        # print(list(who_id))
        # kring={}
        # for i in range(0, len(who)):
        #     kring[who[i]] = who_id[i]
        # print(kring)
        # keyboard = types.InlineKeyboardMarkup(row_width=1)
        # for i in who:
        #     i = types.InlineKeyboardButton(text=who[i], callback_data=who[i])
        # keyboard.add(who[i])

        await bot.send_message(kur_id[0],
                               'Напишите в начало ответа сначала цифру обозначающую номер пользователя .Пример ответа, если у пользователя id = 1: "1Все решим , дорого"')

        await bot.send_message(int(id_who[0]),
                               'Ответ от куратора :\n' + message.text + '\nЧто бы завершить диалог , нажмите "Завершить вопрос"',
                               reply_markup=kb.end)
        dialog1.append(message.text)
#Ответ наставника

    if str(firstname[0]) == 'наставник' and int(otv[0])==1 and int(reg[0]) == 3 and int(aut[0])>=2:


        # keyboard = types.InlineKeyboardMarkup(row_width=1)
        # for i in kur_user:
        #     i = types.InlineKeyboardButton(text=kur_user[i],callback_data=kur_user[i])
        # keyboard.add(i)

        cur2.execute('UPDATE data2 SET question == ? WHERE idd == ?', (message.text, idd))
        base2.commit()

        g = list(message.text)

        g2 = g[0]
        print(g2)
        id_who = cur2.execute('SELECT id FROM data2 WHERE idd == ?', (int(g2),)).fetchone()
        print(id_who)
        # who_id = cur2.execute('SELECT id FROM data2').fetchall()
        # who = cur2.execute('SELECT answer FROM data2').fetchall()
        # print(list(who))
        # print(list(who_id))
        # kring={}
        # for i in range(0, len(who)):
        #     kring[who[i]] = who_id[i]
        # print(kring)
        # keyboard = types.InlineKeyboardMarkup(row_width=1)
        # for i in who:
        #     i = types.InlineKeyboardButton(text=who[i], callback_data=who[i])
        # keyboard.add(who[i])

        await bot.send_message(kur_id[0], 'Напишите в начало ответа сначала цифру обозначающую номер пользователя .Пример ответа, если у пользователя id = 1: "1Все решим , дорого"')

        await bot.send_message(int(id_who[0]), 'Ответ от куратора :\n'+message.text+'\nЧто бы завершить диалог , нажмите "Завершить вопрос" , если хотите продолжить беседу , то просто пишите еще вопросы в чат', reply_markup=kb.end)
        dialog1.append(message.text)

    #Ответ ученика

    if str(firstname[0]) == 'ученик' and int(otv[0])==0 and int(reg[0])== 3 and int(aut[0])>=2:
        cur.execute('UPDATE data SET otv == ? WHERE id == ?', (1, kur_id[0]))
        cur.execute('UPDATE data SET otv == ? WHERE id == ?', (1, us_id))
        base.commit()
        kur_user.append(us_id)
        await bot.send_message(message.chat.id,'Введите вопрос и ближайший куратор вам ответит и обязательнно введите в конце сообщения вопросительный знак')
        await bot.send_message(message.chat.id,'Вам подбирается наставник и начнется диалог')


    if str(firstname[0]) == 'ученик' and int(otv[0]) == 1 and int(reg[0])== 3 and int(aut[0])>=2 and int(r[0])!=4:
        idd+=1
        cur2.execute('INSERT INTO data2 VALUES(?,?,?,?,?,?,?,?)',
                     (idd, message.from_user.id, message.from_user.username, kur_id[0], message.text, '0', '0', '0'))
        base2.commit()
        await bot.send_message(message.chat.id, "Ожидайте ответа от куратора")
        await bot.send_message(kur_id[0], 'Номер пользователя : \n'+number[0]+'\nВопрос : '+message.text+'\nномер вопроса\n'+str(idd) )
        await bot.send_message(kur_id[0],'Напишите в начало ответа сначала цифру обозначающую номер пользователя .Пример ответа, если у пользователя id = 1: "1Все решим , дорого"')

        print(idd)

        await bot.send_message(meto_id[0],'Номер пользователя : \n'+number[0]+'\nВопрос : '+message.text+'\nномер вопроса\n'+str(idd) )
        await bot.send_message(meto_id[0],'Напишите в начало ответа сначала цифру обозначающую номер пользователя .Пример ответа, если у пользователя id = 1: "1Все решим , дорого"')
        await bot.send_message(meto_id[0],'Вы можете сами ответить на этот вопрос',reply_markup=kb.nast_otv)

        cur.execute('UPDATE data SET lastname == ? WHERE id == ?', (us_id,kur_id[0] ))
        base.commit()
        cur.execute('UPDATE data SET lastname == ? WHERE id == ?', (kur_id[0],us_id))
        base.commit()
        await bot.send_message(kur_id[0],'Просто пишите сюда и будете общаться , пока юзер не прекратит')
        dialog1.append(message.text)
    # if str(firstname[0]) == 'наставник' and int(otv[0])==0:


    if int(r[0]) == 2:
        if int(reg[0]) == 3:
            await bot.send_message(message.chat.id,'Вы уже зарегестрировались!',reply_markup=kb.main)
        if int(reg[0]) == 0:
            await bot.delete_message(message.from_user.id, mesid - 1)
            await bot.send_message(message.chat.id,'Логин записан , теперь введите пароль')
            await bot.delete_message(message.chat.id, message.message_id)

            us_id = message.from_user.id
            cur.execute('UPDATE data SET login == ? WHERE id == ?', (mes, us_id))
            cur.execute('UPDATE data SET reg == ? WHERE id == ?', (1, us_id))

            base.commit()

        if int(reg[0]) == 1:
            await bot.delete_message(message.from_user.id, mesid - 1)
            await bot.send_message(message.chat.id,'Введите ваш телефон')
            await bot.delete_message(message.chat.id, message.message_id)
            us_id = message.from_user.id
            cur.execute('UPDATE data SET password == ? WHERE id == ?', (mes, us_id))
            cur.execute('UPDATE data SET reg== ? WHERE id == ?', (2, us_id))
            base.commit()
        if int(reg[0]) == 2:
            cur.execute('UPDATE data SET number== ? WHERE id == ?', (message.text, us_id))
            base.commit()
            await bot.delete_message(message.from_user.id, mesid - 1)
            await bot.send_message(message.chat.id,'Вы успешно зарегистрировались!',reply_markup=kb.main)
            await bot.delete_message(message.chat.id, message.message_id)
            us_id = message.from_user.id
            cur.execute('UPDATE data SET reg== ? WHERE id == ?', (3, us_id))
            base.commit()
    if int(r[0]) == 1:
        us_id = message.from_user.id
        log = cur.execute('SELECT login FROM data WHERE id == ?', (us_id,)).fetchone()
        passs = cur.execute('SELECT password FROM data WHERE id == ?', (us_id,)).fetchone()

        print(log)
        print(passs)
        if int(aut[0]) >= 2:
            await bot.delete_message(message.from_user.id, mesid - 1)
            await bot.send_message(message.chat.id,'Вы уже автиризировались',reply_markup=kb.main)
            await bot.delete_message(message.chat.id, message.message_id)
        if int(aut[0]) == 0:
            await bot.delete_message(message.from_user.id, mesid - 1)
            await bot.send_message(message.chat.id,'А теперь введите пароль')
            await bot.delete_message(message.chat.id, message.message_id)
            us_id = message.from_user.id
            cur.execute('UPDATE data SET aut == ? WHERE id == ?', (1, us_id))
            base.commit()
        if int(aut[0]) == 1:
            if mes == passs[0]:
                await bot.delete_message(message.from_user.id, mesid - 1)
                await bot.send_message(message.chat.id,'Вы успешно аторизовались',reply_markup=kb.ask)
                await bot.delete_message(message.chat.id, message.message_id)
                # await bot.delete_message(message.from_user.id,mesid-1)
                us_id = message.from_user.id
                cur.execute('UPDATE data SET aut == ? WHERE id == ?', (2, us_id))
                base.commit()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)