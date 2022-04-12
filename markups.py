from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

main = InlineKeyboardMarkup(row_width=2)
btn1 = InlineKeyboardButton(text='Авторизация',callback_data='aut')
btn2 = InlineKeyboardButton(text='Регистрация',callback_data='reg')
btn3 = InlineKeyboardButton(text='Личный кабинет',callback_data='lkn')
btn4 = InlineKeyboardButton(text='Список вопросов и ответов',callback_data='spisok')
btn5 = InlineKeyboardButton(text='Задать вопрос',callback_data='ask')
main.insert(btn1)
main.insert(btn2)
main.insert(btn3)
main.insert(btn4)
main.insert(btn5)

mainkur = InlineKeyboardMarkup(row_width=2)
btn1 = InlineKeyboardButton(text='Авторизация',callback_data='aut')
btn2 = InlineKeyboardButton(text='Регистрация',callback_data='reg')
btn3 = InlineKeyboardButton(text='Личный кабинет',callback_data='lkn')
btn4 = InlineKeyboardButton(text='Список вопросов и ответов',callback_data='spisok')
btn5 = InlineKeyboardButton(text='Включить\выключить активность',callback_data='aktiv')
mainkur.insert(btn1)
mainkur.insert(btn2)
mainkur.insert(btn3)
mainkur.insert(btn4)
mainkur.insert(btn5)

mainknast = InlineKeyboardMarkup(row_width=2)
btn1 = InlineKeyboardButton(text='Авторизация',callback_data='aut')
btn2 = InlineKeyboardButton(text='Регистрация',callback_data='reg')
btn3 = InlineKeyboardButton(text='Личный кабинет',callback_data='lkn')
btn4 = InlineKeyboardButton(text='Список всех вопросов и ответов',callback_data='kurspisok')
mainknast.insert(btn1)
mainknast.insert(btn2)
mainknast.insert(btn3)
mainknast.insert(btn4)


logpass = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton(text='Ввести логин',callback_data='log')
logpass.insert(btn1)


ask = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton(text='Задать вопрос',callback_data='ask')
btn2 = InlineKeyboardButton(text='Список вопросов и ответов',callback_data='spisok')
ask.insert(btn1)
ask.insert(btn2)

spisok = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton(text='Список вопросов и ответов',callback_data='spisok')
spisok.insert(btn1)

otv = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton(text='Ответить на вопрос',callback_data='otv')
otv.insert(btn1)


rate = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton(text='Поставить оценку',callback_data='rate')
rate.insert(btn1)


feedback = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton(text='Оставить отзыв',callback_data='feedback')
feedback.insert(btn1)


star = InlineKeyboardMarkup(row_width=2)
btn1 = InlineKeyboardButton(text='1',callback_data='1')
btn2 = InlineKeyboardButton(text='2',callback_data='2')
btn3 = InlineKeyboardButton(text='3',callback_data='3')
btn4 = InlineKeyboardButton(text='4',callback_data='4')
btn5 = InlineKeyboardButton(text='5',callback_data='5')
star.insert(btn1)
star.insert(btn2)
star.insert(btn3)
star.insert(btn4)
star.insert(btn5)

nextback = InlineKeyboardMarkup(row_width=2)
btn1 = InlineKeyboardButton(text='Дальше',callback_data='next')
btn2 = InlineKeyboardButton(text='Назад',callback_data='back')
nextback.insert(btn1)
nextback.insert(btn2)

end = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton(text='Завершить вопрос',callback_data='endit')
end.insert(btn1)

nextbackkur = InlineKeyboardMarkup(row_width=2)
btn1 = InlineKeyboardButton(text='Дальше',callback_data='nextkur')
btn2 = InlineKeyboardButton(text='Назад',callback_data='backkur')
nextbackkur.insert(btn1)
nextbackkur.insert(btn2)

nast_otv = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton(text='Ответить вместо куратора или добавить ответ',callback_data='nast_otv')
nast_otv.insert(btn1)