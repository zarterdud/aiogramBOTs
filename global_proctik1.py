from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
import sqlite3


bot = Bot("6714704690:AAGusdRE_2A8n77Lr8h-UBl6t6_KQcEZFKc")
dp = Dispatcher(bot)

help_text = """
<b>/start_test</b> - начать тест
<b>/show_results</b> - узнать результаты теста
"""

con = sqlite3.connect("bd.sqlite3")
cur = con.cursor()


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    text_start = """Этот профориентационный тест <b>поможет определить</b> подходящий вам тип будущей профессии. Вам нужно выбрать предпочитаемую деятельность из 20 пар видов деятельности. Выполнение онлайн теста займет <b>не более 4-5 минут</b>.
Автор методики: А.Е.Климов"""
    rkb = ReplyKeyboardMarkup(resize_keyboard=True)
    rkb.add(KeyboardButton(text="/help")).add(KeyboardButton(text="/start_test"))
    await bot.send_message(
        chat_id=message.from_user.id,
        text=text_start,
        reply_markup=rkb,
        parse_mode="HTML",
    )


@dp.message_handler(commands=["help"])
async def help_ans(message: types.Message):
    help_text = """
<b>/start_test</b> - начать тест
<b>/show_results</b> - узнать результаты теста
"""
    await bot.send_message(
        chat_id=message.from_user.id,
        text=help_text,
        parse_mode="HTML",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message_handler(commands=["auth"])
async def auth_user(message: types.Message):
    pass


@dp.message_handler(commands=["start_test"])
async def start(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    ikb.add(
        InlineKeyboardButton(text="Мужской", callback_data="M"),
        InlineKeyboardButton(text="Женский", callback_data="F"),
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text="<b>Чтобы начать тест, выберите ваш пол</b>",
        reply_markup=ikb,
        parse_mode="HTML",
    )


d = {
    "Человек-природа": 0,
    "Человек-техника": 0,
    "Человек-человек": 0,
    "Человек-знаковая система": 0,
    "Человек-художественный образ": 0,
}
d_rec = {}
ans = ""
d_description = {
    "Человек-природа": """Если вы любите работать в саду, огороде, ухаживать за растениями, животными, любите предмет биологию, то ознакомьтесь с профессиями типа «человек-природа».

Предметом труда для представителей большинства профессий типа «человек природа» являются:

• животные, условия их роста, жизни;
• растения, условия их произрастания.

Специалистам в этой области приходится выполнять следующие виды деятельности:

• изучать, исследовать, анализировать состояние, условия жизни растений или животных (агроном, микробиолог, зоотехник, гидробиолог, агрохимик, фитопатолог);
• выращивать растения, ухаживать за животными (лесовод, полевод, цветовод, овощевод, птицевод, животновод, садовод, пчеловод);
• проводить профилактику заболеваний растений и животных (ветеринар, врач карантинной службы).

Психологические требования профессий «человек-природа»:

• развитое воображение, наглядно-образное мышление, хорошая зрительная память, наблюдательность, способность предвидеть и оценивать изменчивые природные факторы;
• поскольку результаты деятельности выявляются по прошествии довольно длительного времени, специалист должен обладать терпением, настойчивостью, должен быть готовым работать вне коллективов, иногда в трудных погодных условиях, в грязи и т. п.""",
    "Человек-техника": """ Если вам нравятся лабораторные работы по физике, химии, электротехнике, если вы делаете модели, разбираетесь в бытовой технике, если вы хотите создавать, эксплуатировать или ремонтировать машины, механизмы, аппараты, станки, то ознакомьтесь с профессиями «человек-техника».

Предметом труда для представителей большинства профессий типа «человек техника» являются:

• технические объекты (машины, механизмы);
• материалы, виды энергии.

Специалистам в этой области приходится выполнять следующие виды деятельности:

• создание, монтаж, сборка технических устройств (специалисты проектируют, конструируют технические системы, устройства, разрабатывают процессы их изготовления. Из отдельных узлов, деталей собирают машины, механизмы, приборы, регулируют и налаживают их);
• эксплуатация технических устройств (специалисты работают на станках, управляют транспортом, автоматическими системами);
• ремонт технических устройств (специалисты выявляют, распознают неисправности технических систем, приборов, механизмов, ремонтируют, регулируют, налаживают их).

Психологические требования профессий «человек-техника»:

• хорошая координация движений;
• точное зрительное, слуховое, вибрационное и кинестетическое восприятие;
• развитое техническое и творческое мышление и воображение;
• умение переключать и концентрировать внимание;
• наблюдательность.""",
    "Человек-знаковая система": """Если вы любите выполнять вычисления, чертежи, схемы, вести картотеки, систематизировать различные сведения, если вы хотите заниматься программированием, экономикой или статистикой и т. п., то знакомьтесь с профессиями типа «человек -знаковая система». Большинство профессий этого типа связано с переработкой информации.

Предметом труда для представителей большинства профессий типа «человек знаковая система» являются:

• тексты на родном или иностранном языках (редактор, корректор, машинистка, делопроизводитель, телеграфист, наборщик);
• цифры, формулы, таблицы (программист, оператор ЗВМ, экономист, бухгалтер, статистик);
• чертежи, схемы, карты (конструктор, инженер-технолог, чертежник, копировальщик, штурман, геодезист);
• звуковые сигналы (радист, стенографист, телефонист, звукооператор).

Психологические требования профессий «человек-знаковая система»:

• хорошая оперативная и механическая память;
• способность к длительной концентрации внимания на отвлеченном (знаковом) материале;
• хорошее распределение и переключение внимания;
• точность восприятия, умение видеть то, что стоит за условными знаками;
• усидчивость, терпение;
• логическое мышление.""",
    "Человек-художественный образ": """Предметом труда для представителей большинства профессий типа «человек знаковая система» является:

• художественный образ, способы его построения.

Специалистам в этой области приходится выполнять следующие виды деятельности:

• создание, проектирование художественных произведений (писатель, художник, композитор, модельер, архитектор, скульптор, журналист, хореограф);
• воспроизведение, изготовление различных изделий по образцу (ювелир, реставратор, гравер, музыкант, актер, столяр-краснодеревщик);
• размножение художественных произведений в массовом производстве (мастер по росписи фарфора, шлифовщик по камню и хрусталю, маляр, печатник).

Психологические требования профессий «человек-художественный образ»:

• художественные способности; развитое зрительное восприятие;
• наблюдательность, зрительная память; наглядно-образное мышление; творческое воображение;
• знание психологических законов эмоционального воздействия на людей.""",
    "Человек-человек": """Предметом труда для представителей большинства профессий типа «человек человек» являются:

• люди.

Специалистам в этой области приходится выполнять следующие виды деятельности:

• воспитание, обучение людей (воспитатель, учитель, спортивный тренер);
• медицинское обслуживание (врач, фельдшер, медсестра, няня);
• бытовое обслуживание (продавец, парикмахер, официант, вахтер);
• информационное обслуживание (библиотекарь, экскурсовод, лектор);
• защита общества и государства (юрист, милиционер, инспектор, военнослужащий).

Психологические требования профессий «человек-человек»:

• стремление к общению, умение легко вступать в контакт с незнакомыми людьми;
• устойчивое хорошее самочувствие при работе с людьми;
• доброжелательность, отзывчивость;
• выдержка;
• умение сдерживать эмоции;
• способность анализировать поведение окружающих и свое собственное, понимать намерения и настроение других людей, способность разбираться во взаимоотношениях людей, умение улаживать разногласия между ними, организовывать их взаимодействие;
• способность мысленно ставить себя на место другого человека, умение слушать, учитывать мнение другого человека;
• способность владеть речью, мимикой, жестами;
• развитая речь, способность находить общий язык с разными людьми;
• умение убеждать людей;
• аккуратность, пунктуальность, собранность;
• знание психологии людей.""",
}


@dp.callback_query_handler()
async def callback(callback: types.CallbackQuery):
    text_ = "Предположим, что после соответствующего обучения Вы сможете выполнить любую работу. Но если бы Вам пришлось выбирать только из двух возможностей, что бы Вы предпочли?"
    if callback.data == "M":
        gender = "Мужчина"
        ans = ""
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="1a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="1b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text=text_,
            reply_markup=ReplyKeyboardRemove(),
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 1:
1) Ухаживать за животными

2) Обслуживать машины, приборы (следить, регулировать)""",
            reply_markup=ikb,
        )
    elif callback.data == "F":
        gender = "Женщина"
        ans = ""
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="1a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="1b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text=text_,
            reply_markup=ReplyKeyboardRemove(),
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 1:

1) Ухаживать за животными

2) Обслуживать машины, приборы (следить, регулировать)""",
            reply_markup=ikb,
        )
    elif callback.data == "1a":
        d["Человек-природа"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="2a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="2b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 2:
1) Помогать больным

2) Составлять таблицы, схемы, программы для вычислительных машин""",
            reply_markup=ikb,
        )
    elif callback.data == "1b":
        d["Человек-техника"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="2a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="2b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 2:
1) Помогать больным

2) Составлять таблицы, схемы, программы для вычислительных машин""",
            reply_markup=ikb,
        )

    elif callback.data == "2a":
        d["Человек-художественный образ"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="3a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="3b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 3:
1) Следить за качеством книжных иллюстраций, плакатов, художественных открыток, грампластинок

2) Составлять таблицы, схемы, программы для вычислительных машин""",
            reply_markup=ikb,
        )
    elif callback.data == "2b":
        d["Человек-природа"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="3a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="3b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 3:
1) Следить за качеством книжных иллюстраций, плакатов, художественных открыток, грампластинок

2) Составлять таблицы, схемы, программы для вычислительных машин""",
            reply_markup=ikb,
        )

    elif callback.data == "3a":
        d["Человек-техника"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="4a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="4b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 4:
1) Обрабатывать материалы (дерево, ткань, металл, пластмассу и т.п.)

2) Доводить Товары до потребителя, рекламировать, продавать""",
            reply_markup=ikb,
        )
    elif callback.data == "3b":
        d["Человек-человек"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="4a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="4b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 4:
1) Обрабатывать материалы (дерево, ткань, металл, пластмассу и т.п.)

2) Доводить Товары до потребителя, рекламировать, продавать""",
            reply_markup=ikb,
        )

    elif callback.data == "4a":
        d["Человек-знаковая система"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="5a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="5b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 5:
1) Обсуждать научно-популярные книги, статьи

2) Обсуждать художественные книги (или пьесы, концерты)""",
            reply_markup=ikb,
        )
    elif callback.data == "4b":
        d["Человек-художественный образ"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="5a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="5b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 5:
1) Обсуждать научно-популярные книги, статьи

2) Обсуждать художественные книги (или пьесы, концерты)""",
            reply_markup=ikb,
        )

    elif callback.data == "5a":
        d["Человек-природа"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="6a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="6b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 6:
1) Выращивать молодняк (животных какой-либо породы)

2) Тренировать товарищей (или младших) в выполнении каких-либо действий (трудовых, учебных, спортивных)""",
            reply_markup=ikb,
        )
    elif callback.data == "5b":
        d["Человек-техника"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="6a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="6b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 6:
1) Выращивать молодняк (животных какой-либо породы)

2) Тренировать товарищей (или младших) в выполнении каких-либо действий (трудовых, учебных, спортивных)""",
            reply_markup=ikb,
        )

    elif callback.data == "6a":
        d["Человек-художественный образ"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="7a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="7b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 7:
1) Копировать рисунки, изображения (или настраивать музыкальные инструменты)

2) Управлять каким-либо грузовым (подъемным или транспортным) средством – подъемным краном, трактором, тепловозом и др.)""",
            reply_markup=ikb,
        )
    elif callback.data == "6b":
        d["Человек-техника"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="7a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="7b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 7:
1) Копировать рисунки, изображения (или настраивать музыкальные инструменты)

2) Управлять каким-либо грузовым (подъемным или транспортным) средством – подъемным краном, трактором, тепловозом и др.)""",
            reply_markup=ikb,
        )

    elif callback.data == "7a":
        d["Человек-человек"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="8a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="8b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 8:
1) Сообщать, разъяснять людям нужные им сведения (в справочном бюро, на экскурсии и т.д.)

2) Оформлять выставки, витрины (или участвовать в подготовке пьес, концертов)""",
            reply_markup=ikb,
        )
    elif callback.data == "7b":
        d["Человек-художественный образ"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="8a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="8b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 8:
1) Сообщать, разъяснять людям нужные им сведения (в справочном бюро, на экскурсии и т.д.)

2) Оформлять выставки, витрины (или участвовать в подготовке пьес, концертов)""",
            reply_markup=ikb,
        )

    elif callback.data == "8a":
        d["Человек-природа"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="9a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="9b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 9:
1) Ремонтировать вещи, изделия (одежду, технику), жилище

2) Искать и исправлять ошибки в текстах, таблицах, рисунках""",
            reply_markup=ikb,
        )
    elif callback.data == "8b":
        d["Человек-знаковая система"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="9a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="9b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 9:
1) Ремонтировать вещи, изделия (одежду, технику), жилище

2) Искать и исправлять ошибки в текстах, таблицах, рисунках""",
            reply_markup=ikb,
        )

    elif callback.data == "9a":
        d["Человек-природа"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="10a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="10b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 10:
1) Лечить животных

2) Выполнять вычисления, расчеты""",
            reply_markup=ikb,
        )
    elif callback.data == "9b":
        d["Человек-знаковая система"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="10a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="10b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 10:
1) Лечить животных

2) Выполнять вычисления, расчеты""",
            reply_markup=ikb,
        )

    elif callback.data == "10a":
        d["Человек-природа"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="11a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="11b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 11:
1) Выводить новые сорта растений

2) Конструировать, проектировать новые виды промышленных изделий (машины, одежду, дома, продукты питания и т.п.)""",
            reply_markup=ikb,
        )
    elif callback.data == "10b":
        d["Человек-техника"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="11a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="11b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 11:
1) Выводить новые сорта растений

2) Конструировать, проектировать новые виды промышленных изделий (машины, одежду, дома, продукты питания и т.п.)""",
            reply_markup=ikb,
        )

    elif callback.data == "11a":
        d["Человек-человек"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="12a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="12b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 12:
1) Разбирать споры, ссоры между людьми, убеждать, разъяснять, наказывать, поощрять

2) Разбираться в чертежах, схемах, таблицах (проверять, уточнять, приводить в порядок)""",
            reply_markup=ikb,
        )
    elif callback.data == "11b":
        d["Человек-знаковая система"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="12a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="12b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 12:
1) Разбирать споры, ссоры между людьми, убеждать, разъяснять, наказывать, поощрять

2) Разбираться в чертежах, схемах, таблицах (проверять, уточнять, приводить в порядок)""",
            reply_markup=ikb,
        )

    elif callback.data == "12a":
        d["Человек-художественный образ"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="13a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="13b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 13:
1) Наблюдать, изучать работу кружков художественной самодеятельности

2) Наблюдать, изучать жизнь микробов""",
            reply_markup=ikb,
        )
    elif callback.data == "12b":
        d["Человек-природа"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="13a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="13b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 13:
1) Наблюдать, изучать работу кружков художественной самодеятельности

2) Наблюдать, изучать жизнь микробов""",
            reply_markup=ikb,
        )

    elif callback.data == "13a":
        d["Человек-техника"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="14a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="14b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 14:
1) Обслуживать, налаживать медицинские приборы, аппараты

2) Наблюдать, изучать жизнь микробов""",
            reply_markup=ikb,
        )
    elif callback.data == "13b":
        d["Человек-человек"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="14a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="14b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 14:
1) Обслуживать, налаживать медицинские приборы, аппараты

2) Наблюдать, изучать жизнь микробов""",
            reply_markup=ikb,
        )

    elif callback.data == "14a":
        d["Человек-знаковая система"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="15a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="15b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 15:
1) Составлять точные описания-отчеты о наблюдаемых явлениях, событиях, измеряемых объектах и др.

2) Художественно описывать, изображать события (наблюдаемые и представляемые)""",
            reply_markup=ikb,
        )
    elif callback.data == "14b":
        d["Человек-художественный образ"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="15a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="15b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 15:
1) Составлять точные описания-отчеты о наблюдаемых явлениях, событиях, измеряемых объектах и др.

2) Художественно описывать, изображать события (наблюдаемые и представляемые)""",
            reply_markup=ikb,
        )

    elif callback.data == "15a":
        d["Человек-природа"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="16a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="16b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 16:
1) Делать лабораторные анализы в больнице

2) Принимать, осматривать больных, беседовать с ними, назначать лечение""",
            reply_markup=ikb,
        )
    elif callback.data == "15b":
        d["Человек-человек"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="16a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="16b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 16:
1) Делать лабораторные анализы в больнице

2) Принимать, осматривать больных, беседовать с ними, назначать лечение""",
            reply_markup=ikb,
        )

    elif callback.data == "16a":
        d["Человек-художественный образ"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="17a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="17b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 17:
1) Красить или расписывать стены помещений, поверхность изделий

2) Осуществлять монтаж или сборку машин, приборов""",
            reply_markup=ikb,
        )
    elif callback.data == "16b":
        d["Человек-техника"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="17a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="17b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 17:
1) Красить или расписывать стены помещений, поверхность изделий

2) Осуществлять монтаж или сборку машин, приборов""",
            reply_markup=ikb,
        )

    elif callback.data == "17a":
        d["Человек-человек"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="18a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="18b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 18:
1) Организовать культпоходы сверстников или младших в театры, музеи, экскурсии, туристические походы и т.п.

2) Играть на сцене, принимать участие в концертах""",
            reply_markup=ikb,
        )
    elif callback.data == "17b":
        d["Человек-художественный образ"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="18a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="18b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 18:
1) Организовать культпоходы сверстников или младших в театры, музеи, экскурсии, туристические походы и т.п.

2) Играть на сцене, принимать участие в концертах""",
            reply_markup=ikb,
        )
    elif callback.data == "18a":
        d["Человек-техника"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="19a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="19b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 19:
1) Изготовлять по чертежам детали, изделия (машины, одежду), строить здания

2) Заниматься черчением, копировать чертежи, карты""",
            reply_markup=ikb,
        )
    elif callback.data == "18b":
        d["Человек-знаковая система"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="19a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="19b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 19:
1) Изготовлять по чертежам детали, изделия (машины, одежду), строить здания

2) Заниматься черчением, копировать чертежи, карты""",
            reply_markup=ikb,
        )

    elif callback.data == "19a":
        d["Человек-природа"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="20a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="20b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 20:
1) Вести борьбу с болезнями растений, с вредителями леса, сада

2) Работать на клавишных машинах (пишущей машинке, телетайпе, наборной машине и др.)""",
            reply_markup=ikb,
        )
    elif callback.data == "19b":
        d["Человек-знаковая система"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="1", callback_data="20a")).insert(
            InlineKeyboardButton(
                text="2",
                callback_data="20b",
            )
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="""Ответ 20:
1) Вести борьбу с болезнями растений, с вредителями леса, сада

2) Работать на клавишных машинах (пишущей машинке, телетайпе, наборной машине и др.)""",
            reply_markup=ikb,
        )

    elif callback.data == "20a":
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="Сохранить результат", callback_data="save"))
        d["Человек-природа"] += 1
        d_rec = {
            "r1": "",
            "r2": "",
            "r3": "",
            "r4": "",
            "r5": "",
        }
        k = 1
        fits = max(d.values())
        ans = """Поздравляем, Вы успешно прошли тест, ваши результаты:

"""
        for i, j in sorted(d.items(), key=lambda x: (x[1] * -1, x[0])):
            if k == 1:
                ans += f"Самая предпочтительная профессия - <em>{i}</em>, подходит на <b>{round((fits/sum(d.values()))*100, 2)}%</b>"
                ans += """

"""
                ans += f"Краткое описание: {d_description[i]}"
            d_rec[f"r{k}"] = i
            k += 1
        await bot.send_message(
            chat_id=callback.from_user.id,
            parse_mode="HTML",
            reply_markup=ikb,
            text=ans
            + """

"""
            + "Остальную информацию можете посмотреть в файле:",
        )

    elif callback.data == "20b":
        d["Человек-знаковая система"] += 1
        ikb = InlineKeyboardMarkup(row_width=2)
        ikb.add(InlineKeyboardButton(text="Сохранить результат", callback_data="save"))
        d_rec = {
            "r1": "",
            "r2": "",
            "r3": "",
            "r4": "",
            "r5": "",
        }
        k = 1
        fits = max(d.values())
        ans = """Поздравляем, Вы успешно прошли тест, ваши результаты:

"""
        for i, j in sorted(d.items(), key=lambda x: (x[1] * -1, x[0])):
            if k == 1:
                ans += f"Самая предпочтительная профессия - <em>{i}</em>, подходит на <b>{round((fits/sum(d.values()))*100, 2)}%</b>"
                ans += """

"""
                ans += f"Краткое описание: {d_description[i]}"
            d_rec[f"r{k}"] = i
            k += 1
        await bot.send_message(
            chat_id=callback.from_user.id,
            parse_mode="HTML",
            reply_markup=ikb,
            text=ans
            + """

"""
            + "Остальную информацию можете посмотреть в файле:",
        )
        # with open("new_file", "w") as f:
        #     bot.send_file(chat_id=callback.from_user.id, file=f)

    elif callback.data == "save":
        name = ""
        passw = ""
        cur.execute(
            f"INSERT INTO users (name, password, gender, result) VALUES ('{name}', '{passw}', '{gender}', '{ans}')"
        )
        con.commit()
        con.close()
        await bot.send_message(
            chat_id=callback.from_user.id, text="Данные успешно сохранены"
        )


@dp.message_handler(commands=["static"])
async def show_static(message: types.Message):
    genders = cur.execute(f"SELECT gender FROM users;").fetchall()
    ma = genders.count("male")
    fe = genders.count("female")
    text = f"Количество мужчин - {ma}, {round(ma/len(genders), 2)}"
    text += """
"""
    text += f"Количество женщин - {fe}, {round(fe/len(genders), 2)}"
    await bot.send_message(
        chat_id=message.from_user.id, parse_mode="HTML", text=genders
    )


@dp.message_handler(commands=["show_results"])
async def show(message: types.Message):
    if ans != "":
        await bot.send_message(
            chat_id=message.from_user.id, text="Ваши результаты: + ans"
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id, text="Закончите прохождение теста!"
        )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
