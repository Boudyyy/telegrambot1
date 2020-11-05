import telebot
from telebot import types
from config import Bot_Token

bot = telebot.TeleBot(Bot_Token)


@bot.message_handler(commands=["start"])
def start(m):
    msg = bot.send_message(m.chat.id, "Hi! Type or click.")
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('Statistics', 'Schedule')
    keyboard.row('Reshuffle', 'About bot')
    bot.send_message(m.chat.id,
                     'You\'ve got your options!',
                     reply_markup=keyboard)


@bot.message_handler(commands=["links"])
def links(m):
    msg = bot.send_message(m.chat.id,
                           "Here are the links that might be useful:")
    bot.send_message(m.chat.id, '''[HLTV](https://www.hltv.org/team/4608/natus-vincere)
[Instagram](https://www.instagram.com/natus_vincere_official/)
[YouTube](https://www.youtube.com/c/navicsgo/featured)
[Twitter](https://twitter.com/natusvincere?lang=ru)
[Facebook](https://www.facebook.com/NatusVincere/)
[NaVi official website](https://navi.gg/en/)
    ''', parse_mode='Markdown')


@bot.message_handler(commands=["events"])
def links(m):
    bot.send_message(m.chat.id,
                     'Ongoing events: ')
    bot.send_message(m.chat.id,
                     '[EM Beijing-Haidian 2020 Europe]'
                     '(https://www.hltv.org'
                     '/events/5524/'
                     'iem-beijing-haidian-2020-europe)\n'
                     '[BLAST Premier Fall 2020 Finals]'
                     '(https://www.hltv.org/events'
                     '/5209/blast-premier-fall-2020-finals)',
                     parse_mode='Markdown')
    bot.send_photo(m.chat.id,
                   'http://prntscr.com/ve19id.png')
    bot.send_photo(m.chat.id,
                   'http://prntscr.com/ve19vg.png')


@bot.message_handler(content_types=['text'])
def blabla(m):
    if m.text.lower() == 'main menu':
        msg = bot.send_message(m.chat.id,
                               "Alright, what are we going to be up to?")
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('Statistics', 'Schedule')
        keyboard.row('Reshuffle', 'About bot')
        bot.send_message(m.chat.id, 'You\'ve got your options!',
                         reply_markup=keyboard)

    elif m.text.lower() == 'reshuffle':
        bot.send_message(m.chat.id, '''Current Player Roster:
    🇷🇺  Egor "*flamie*" Vasilev
    🇺🇦  Oleksandr "*s1mple*" Kostyliev
    🇷🇺  Denis "*electronic*" Sharipov
    🇷🇺  Kirill "*Boombl4*" Mikhailov
    🇷🇺  Ilya "*Perfecto*" Zalutskiy
    🇺🇦  Andrii "*B1ad3*" Gorodenskyi(coach)
            ''', parse_mode='Markdown')
        bot.send_message(m.chat.id, '''
    Inactive Players                                        Inactive date
    🇸🇰    Ladislav "*GuardiaN*" Kovács        2020-01-24
    🇺🇦    Ioann "*Edward*" Sukhariev           2019-05-29
            ''', parse_mode='Markdown')
        bot.send_message(m.chat.id,
                         'Former Players\n'
                         '🇺🇦  Danylo *Zeus* Teslenko\n'
                         '🇺🇦    Mykhailo *kane* (Coach) Blagin\n'
                         '🇷🇺    Denis *seized* Kostin\n'
                         '🇺🇦    Andrey *Andi* (Coach) Prokhor\n'
                         '🇸🇰    Ladislav *GuardiaN* Kovács\n'
                         '🇺🇦    Sergey *starix* (Coach) Isch\n'
                         '🇺🇦    Danylo *Zeus* Teslen\n'
                         '🇷🇺    Egor *flamie* (Stand-in) Vasilev\n'
                         '🇺🇦    Sergey *starix* Isch\n'
                         '🇷🇺    Anton *kibaken* Kolesnik\n'
                         '🇺🇦    Arseniy *ceh9* Trynozhenko\n'
                         '🇺🇦    Ioann *Edward* Sukhariev\n'
                         '🇺🇦    Yegor *markeloff* Markelov',
                         parse_mode='Markdown')

    elif m.text.lower() == 'about bot':
        bot.send_message(m.chat.id,
                         'This bot is made by a freshman '
                         'for a university project. '
                         'It does nothing special, '
                         'basically it just gives some '
                         'scripted information you ask for, '
                         'but might be useful if you'
                         ' do not want to open HLTV website.')
    elif m.text.lower() == 'statistics':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('s1mple')
        keyboard.row('flamie', 'Boombl4')
        keyboard.row('Perfecto', 'electronic')
        keyboard.row('Main menu')
        bot.send_message(m.chat.id,
                         'Choose a player you want to know statistics of',
                         reply_markup=keyboard)
    elif m.text.lower() == 's1mple':
        keyboard = types.ReplyKeyboardMarkup(True)
        bot.send_photo(m.chat.id, 'http://prntscr.com/v8rc3p.png')
        bot.send_photo(m.chat.id, 'http://prntscr.com/vblgv7.png')
        bot.send_message(m.chat.id, '''*s1mple statistics* _Past 3 months_
    Role                        Main sniper
    Rating 2.0                  1.27
    Kills per round             0.86
    Headshots                   38.8%
    Maps played                 53
    Deaths per round            0.64
    Rounds contributed          72.8%
*Overall stats*
    Kills                       28219
    Deaths                      21418
    Kill / Death                1.32
    Kill / Round                0.85
    Rounds with kills           17936
    Kill - Death difference     6801
*Opening stats*
    Total opening kills         4785
    Total opening deaths        3074
    Opening kill ratio          1.56
    Opening kill rating         1.23
    First kill in won rounds    20.8 %
    Round stats 0 kill rounds   15204
    1 kill rounds               10419
    2 kill rounds               5263
    3 kill rounds               1808
    4 kill rounds               397
    5 kill rounds               49
*Weapon stats*
    Rifle kills                 12044
    Sniper kills                10120
    SMG kills                   769
    Pistol kills                4988
    Grenade                     140
    Other                       201''', parse_mode='Markdown')
        bot.send_photo(m.chat.id, 'http://prntscr.com/vblf4u.png')
    elif m.text.lower() == 'electronic':
        keyboard = types.ReplyKeyboardMarkup(True)
        bot.send_photo(m.chat.id, 'http://prntscr.com/v8rj0g.png')
        bot.send_photo(m.chat.id, 'http://prntscr.com/vblmfz.png')
        bot.send_message(m.chat.id, '''*electronic statistics* _Past 3 months_
    Role                        Rifler, A-site player
    Rating 2.0                  1.09
    Kills per round             0.70
    Headshots                   54.8%
    Maps played                 53
    Deaths per round            0.66
    Rounds contributed          70.7%
*Overall stats*
    Kills                       20004
    Deaths                      17464
    Kill / Death                1.15
    Kill / Round                0.76
    Rounds with kills           13137
    Kill - Death difference     2540
*Opening stats*
    Total opening kills         3072
    Total opening deaths        2677
    Opening kill ratio          1.15
    Opening kill rating         1.08
    First kill in won rounds    16.3%
*Round stats*
    0 kill rounds               13291
    1 kill rounds               8068
    2 kill rounds               3586
    3 kill rounds               1204
    4 kill rounds               244
    5 kill rounds               35
*Weapon stats*
    Rifle kills                 15015
    Sniper kills                186
    SMG kills                   1194
    Pistol kills                3365
    Grenade                     226
    Other                       54''', parse_mode='Markdown')
        bot.send_photo(m.chat.id, 'http://prntscr.com/vblorr.png')
    elif m.text.lower() == 'flamie':
        keyboard = types.ReplyKeyboardMarkup(True)
        bot.send_photo(m.chat.id, 'http://prntscr.com/v8rkyp.png')
        bot.send_photo(m.chat.id, 'http://prntscr.com/vbli89.png')
        bot.send_message(m.chat.id, '''*flamie statistics* _Past 3 months_
    Role                        Rifler, Lurker
    Rating 2.0                  0.97
    Kills per round             0.60
    Headshots                   55.5%
    Maps played                 53
    Deaths per round            0.65
    Rounds contributed          68.2%
*Overall stats*
    Kills                       26809
    Deaths                      25235
    Kill / Death                1.06
    Kill / Round                0.71
    Rounds with kills           18085
    Kill - Death difference     1574
*Opening stats*
    Total opening kills         3545
    Total opening deaths        3543
    Opening kill ratio          1.00
    Opening kill rating         0.98
    First kill in won rounds    13.1%
*Round stats*
    0 kill rounds               19791
    1 kill rounds               11524
    2 kill rounds               4793
    3 kill rounds               1430
    4 kill rounds               308
    5 kill rounds               30
*Weapon stats*
    Rifle kills                 19010
    Sniper kills                1530
    SMG kills                   1401
    Pistol kills                4573
    Grenade                     262
    Other                       68''', parse_mode='Markdown')
        bot.send_photo(m.chat.id, 'http://prntscr.com/vblll5.png')
    elif m.text.lower() == 'perfecto':
        keyboard = types.ReplyKeyboardMarkup(True)
        bot.send_photo(m.chat.id, 'http://prntscr.com/v8rn0y.png')
        bot.send_photo(m.chat.id, 'http://prntscr.com/vblppp.png')
        bot.send_message(m.chat.id, '''*Perfecto statistics* _Past 3 months_
    Role                        Rifler, B-site player
    Rating 2.0                  1.01
    Kills per round             0.63
    Headshots                   44.1%
    Maps played                 53
    Deaths per round            0.62
    Rounds contributed          72.6%
*Overall stats*
    Kills                       6874
    Deaths                      6641
    Kill / Death                1.04
    Kill / Round                0.64
    Rounds with kills           4790
    Kill - Death difference     233
*Opening stats*
    Total opening kills         694
    Total opening deaths        678
    Opening kill ratio          1.02
    Opening kill rating         0.88
    First kill in won rounds    9.1%
*Round stats*
    0 kill rounds               5937
    1 kill rounds               3183
    2 kill rounds               1208
    3 kill rounds               328
    4 kill rounds               64
    5 kill rounds               7
*Weapon stats*
    Rifle kills                 4908
    Sniper kills                167
    SMG kills                   545
    Pistol kills                1163
    Grenade                     92
    Other                       23''', parse_mode='Markdown')
        bot.send_photo(m.chat.id, 'http://prntscr.com/vbls6p.png')
    elif m.text.lower() == 'boombl4':
        keyboard = types.ReplyKeyboardMarkup(True)
        bot.send_photo(m.chat.id, 'http://prntscr.com/v8rp0p.png')
        bot.send_photo(m.chat.id, 'http://prntscr.com/vblt03.png')
        bot.send_message(m.chat.id, '''*Boombl4 statistics* _Past 3 months_
    Role                        Rifler, In-game leader, captain
    Rating 2.0                  1.00
    Kills per round             0.63
    Headshots                   45.1%
    Maps played                 53
    Deaths per round            0.69
    Rounds contributed          68.5%
*Overall stats*
    Kills                           14839
    Deaths                          14649
    Kill / Death                    1.01
    Kill / Round                    0.70
    Rounds with kills               9901
    Kill - Death difference         190
*Opening stats*
    Total opening kills             2584
    Total opening deaths            2784
    Opening kill ratio              0.93
    Opening kill rating             1.06
    First kill in won rounds        17.1%
*Round stats*
    0 kill rounds                   11387
    1 kill rounds                   6189
    2 kill rounds                   2684
    3 kill rounds                   849
    4 kill rounds                   160
    5 kill rounds                   19
*Weapon stats*
    Rifle kills                     9665
    Sniper kills                    401
    SMG kills                       1708
    Pistol kills                    2733
    Grenade                         204
    Other                           158''', parse_mode='Markdown')
        bot.send_photo(m.chat.id, 'http://prntscr.com/vblvtu.png')

    elif m.text.lower() == 'schedule':
        keyboard = types.ReplyKeyboardMarkup(True)
        bot.send_photo(m.chat.id, 'http://prntscr.com/v8r1kt.png')
        bot.send_message(m.chat.id,
                         'NaVi🇷🇺 will play against Ninjas In Pyjamas🇸🇪 as'
                         ' a part of Blast Premiere Fall Series 2020')

    else:
        bot.send_message(m.chat.id,
                         'Please, enter something valid '
                         'or use a integrated Telegram keyboard')

bot.polling(none_stop=True)
