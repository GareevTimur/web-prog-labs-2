from random import choice


def greeting7(user):
    return f'Дед Мороз и Снегурочка поздравляют тебя c новым, 2025 годом!!'

def greeting17(user):
    return f'Дед Мороз и Снегурочка поздравляют тебя, {user["name"]}, c новым, 2025 годом!!'

def greeting(user):
    return f'Поздравляю вас,  {user["name"]}, c новым, 2025 годом! Ура!'

def end(user):
    r = ' Пожелания приняты, 2025 год будет удачливым и счастливым! '
    r = r + f'Вы, {user["name"]}, любите {user["choice1"]} и {user["choice2"]}. Что ж, '
    wishlist = user["choice1"] + '_' + user["choice2" ]
    r = r + wishes[ wishlist ]
    return r

def end7(user):
    r = ''
    r = r + f'Ты, {user["name"]}, любишь {user["choice1"]} и {user["choice2"]}. '
    wishlist = user["choice1"] + '_' + user["choice2" ]
    r = r + wishes7[ wishlist ]
    return r

def make_shorts(short, gender, name):
    r = choice(short[gender])
    r = r.replace( '[Тег пользователя]', name)
    return r

def getGrats(user):
    grats = {}

    # категории возраста
    name = user['name']
    age = int(user['age'])
    gender = {'Парень': 'male', 'Девушка': 'female'}[user['gender']]

    if 0 <= age < 7:
        age_category = '0-7'
    elif 7 <= age < 17:
        age_category = '7-17'
    elif 17 <= age < 25:
        age_category = '17-25'
    elif 25 <= age < 30:
        age_category = '25-30'
    else:
        age_category = '30+'


    if age_category == '0-7':
        grats['begin'] = greeting7(user)
        grats['body'] = make_shorts(short7, gender, name)
        grats['user'] = end7(user) 
        grats['end'] = 'Слушайся маму и папу и все будет хорошо!'

        grats['giftpic'] = gender[0] + choice( ['1','2','3'] ) + '.jpeg'
 
    elif age_category == '7-17':
        grats['begin'] = greeting17(user)
        grats['body'] = make_shorts(short17, gender, name) 
        grats['user'] = end(user) 
        grats['end'] = ' Пусть этот год принесет удачу, успех и благополучие!'
 
        grats['giftpic'] = ''
    else:
        grats['begin'] = greeting(user)
        grats['body'] = make_shorts(short30, gender, name)
        if user['age'] >= '30':
            grats['body'] += choice(work)
        grats['user'] = end(user) 
        grats['end'] = ' Пусть этот год принесет удачу, успех и благополучие!'

        grats['giftpic'] = ''
        
        print(age_category)
    return grats

choice1= [
    { 'value': 'вкусное', 'label': 'Что-то вкусное' },
    { 'value': 'красивое', 'label': 'Что-то красивое' },
]
choice2 = {
    'вкусное' : [
        { 'value': 'сладкое', 'label': 'Это сладкое?' },
        { 'value': 'сытное', 'label': ' может сытное?' }
    ],
    'красивое' : [
        { 'value': 'нарядное', 'label': 'Что-то нарядное' },
        { 'value': 'полезное', 'label': 'Что-то полезное' }
    ]
} 
wishes7 = {
    'вкусное_сладкое': 'Пироженые и эклеры каждый день! ',
    'вкусное_сытное': 'Пусть в новом году будут вкусно кормить!',
    'красивое_нарядное': 'Да ты просто красавишна в этих новых нарядах!',
    'красивое_полезное': 'Подарки всегда будут красивыми и полезными!',
}

wishes = {
    'вкусное_сладкое': 'Пироженые и эклеры каждый день! ',
    'вкусное_сытное': 'Пусть в новом году вас будут вкусно кормить!',
    'красивое_нарядное': 'Вы просто неотразимы в этих новых нарядах!',
    'красивое_полезное': 'Ваши покупки всегда будут красивыми и полезными!',
}

work =[
'''
Желаю в наступающем году невероятных успехов и карьерного взлета! Пусть коллеги станут верными соратниками, а начальство ценит ваши старания.
''',
'''
Пусть сбудется любое желание, загаданное под бой курантов! Даже если вы захотите получать в три раза больше, приходя на работу на три часа позже!
''',
'''
Пусть в наступающем году понедельники вызывают прилив бодрости, а в пятницу охватывает легкая грусть по интересной, важной, высокооплачиваемой работе, на которой вас любят и ценят.
''',
'''
Удачи, успехов, реализации самых смелых амбиций… я вам не желаю. Я констатирую факт: в новом году все будет именно так!
''',
]

short7 = {
    'male' : [
'''Поздравляю с Новым Годом, [Тег пользователя]! В следующем году постарайся быть хорошим мальчиком и не сильно кидаться черепашками, они этого не любят!
''',
'''Поздравляю с Новым Годом, [Тег пользователя]! Не забудь в следующем году чистить зубы перед сном, неряха! У тебя из-за рта уже пахнуть начало!
''',
    ],
    'female' : [
'''С Новым годом, моя маленькая волшебница [Тег пользователя]! Пусть этот год принесет тебе столько радости, сколько снежинок на зимнем небе!
''',
'''С Новым годом, моя маленькая мечтательница [Тег пользователя]! Пусть в этом году Дед Мороз исполнит все твои желания, а каждый день будет как подарок, полный сюрпризов и радости!
''',
    
    ]
}

short17 = {
    'male' : [
'''Поздравляю с Новым Годом, [Тег пользователя]! Желаю, чтобы все проблемы забрал старый год, а Новый принёс только радости!
''',
'''Поздравляю с Новым Годом, [Тег пользователя]! Желаю тебе счастья в следующем году, и постарайся не сжигать школу. P.s.: Если всё-таки сожжёшь, сделай так, чтобы на тебя никто не подумал!
''',
'''Поздравляю с Новым Годом, [Тег пользователя]! Старый год уходит, а Новый наступает! Так что пользуйся своими шансами с умом, они вечно ждать не будут!
''',
    ],
    'female' : [
'''Поздравляю с Новым Годом, [Тег пользователя]! В этом Нового году желаю быть тебе самой красивой!
''',
'''С Новым Годом, дорогая [Тег пользователя]! Желаю, чтобы каждый день был как страница из сказки, полной чудес и удивительных приключений!
''',
'''С Новым годом, моя креативная натура [Тег пользователя]! Пусть этот год станет для тебя источником вдохновения, новых идей и творческих свершений
''',
    ]
}

short30 = {
    'male' : [
'''
В год Змеи желаю мудрости, гибкости и проницательности. Пусть этот год принесет удачу, успех и благополучие!
''',
'''
В год Змеи желаю гибкости в принятии решений, мудрости в достижении целей и грациозности в преодолении трудностей. Пусть этот год принесет процветание и гармонию.
''',
'''
Пусть в новом году ваша жизнь будет наполнена любовью и счастьем. Желаю, чтобы намеченные планы и загаданные мечты исполнились лучшим образом. 
''',
'''
В год Змеи пусть ваш путь будет отмечен ясностью мысли и решительными действиями. Желаю, чтобы год принес вам изобилие возможностей и удачу, которая будет следовать за вами, как змея за своей добычей.
''',
'''
Пусть год будет полон неожиданных поворотов, как след змеи на песке, и принесет столько же удовольствия, сколько ощущает змея, которая греется на солнышке. С Новым годом!
''',
'''
В этот год желаю, чтобы удача обвивалась вокруг тебя, как питон вокруг добычи, а деньги заползали в карманы, как удавы в террариум. Пусть каждый день будет полон сюрпризов — неожиданных, как укус гадюки, но приятных, как блеск змеиной чешуи на солнце. И пусть все проблемы решаются так же легко, как змея сбрасывает кожу. С Новым годом!
''',
'''
В наступающий год Змеи желаю тебе быть таким же гибким, как она, и уметь находить выход из любой ситуации. Пусть твой язык будет острым, но только для того, чтобы рассказывать смешные анекдоты, а не для сплетен. Желаю тебе двигаться по жизни с грацией и изяществом, обходя все препятствия на пути. И пусть твой год будет таким же ярким, как чешуя змеи!
''',
'''
В новом году желаю тебе быть таким же мудрым, как старая змея, таким же гибким, как молодая змейка, и таким же удачливым, как кобра, которая нашла мышиную норку! Пусть этот год будет полон приятных сюрпризов и неожиданных поворотов. Желаю тебе здоровья, как у змеи, которая сбрасывает кожу, и силы, как у Змея Горыныча. С Новым годом!
''',
'''
Желаю, чтобы в год Змеи ваш кошелек был как змеиная кожа — постоянно обновлялся и становился все толще! А удача пусть обвивается вокруг вас, как змея вокруг ветки, и не отпускает ни на шаг. Будьте такими же мудрыми и умейте находить выход из любых ситуаций. Пусть ваши враги будут безвредны, как плюшевые удавы, а друзья 一 верны, как питоны!
''',
'''
Поздравляю с годом Змеи! Желаю, чтобы ваша жизнь была такой же яркой и многогранной, как окрас этого животного. Пусть каждый день приносит новые приключения и неожиданные повороты, но все они будут заканчиваться благополучно, как у змеи, которая всегда находит путь к своей цели!
''',
'''
Желаю тебе не убирать елку до следующего декабря, потому что весь твой год будет ярким, праздничным, красочным и веселым. А какой же праздник без елочки?
''',
        
    ],
    'female' : [
'''Моя дорогая подруга! Я даже не знаю, чего для тебя на этот раз попросить у Деда Мороза. Ты добрее и красивей, чем Снегурочка, легче, чем снежинка, и ярче, чем звездочка, сияющая на елке! Поэтому будь просто счастлива и улыбайся почаще!
''',
'''Поздравляю с Новым Годом, [Тег пользователя]! В этом Нового году желаю быть тебе самой красивой и желанной!
''',
'''С Новым годом, моя светлая звезда [Тег пользователя]! Пусть все твои мечты сверкают, как новогодние огоньки, а жизнь будет полна ярких моментов и счастливых событий. 
''',
'''С Новым годом, прекрасная [Тег пользователя]! Желаю, чтобы каждый день был наполнен светом и теплом!
''',
'''С Новым годом, моя гармония [Тег пользователя]! Желаю, чтобы каждый день начинался с улыбки, а вечера были полны тепла и уюта!
''',
'''Новым годом, моя вдохновляющая [Тег пользователя]! Пусть в этом году ты будешь смело идти к своим целям и мечтам! 
''',

]
}    



# В этот шипящий год Змеи желаем вам:

# умения извиваться вокруг проблем, словно змея в траве;
# гибкости в принятии решений, как у змеи, меняющей кожу;
# ядовитого остроумия, чтобы держать завистников на расстоянии;
# мудрости, как у старой змеи, чтобы видеть обман;
# способности заворожить всех своим обаянием, как удав гипнотизирует кролика.