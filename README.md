Данный бот предусматривает работу с обученной моделью sklearn. В процессе работы данные будут обноввляться
и изменяться. 
На данный момент уже пробный вариант чат-бота, который может классифицировать сообщения, относятся
ли они к чрезвычайным ситуациям или нет. Для его работы нужно создать файл config.txt, в котором будет находиться 
API_TOKEN Вашего бота, который должен быть получен в боте телеграмма @BotFather

Состав репозитория:
1.   srw_bot.py - ключевой (чистовой) Python script для запуска бота
2.   mod.pickle - модель клссификации
3.   dat.pickle - очищенные мешки слов и корпус слов
