import web

db_host = 'localhost'
db_name = 'bothorarios'
db_user = 'bot'
db_pw = 'bot.2019'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )