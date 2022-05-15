from pyrogram import Client, Filters
from pyrogram.api import functions
import datetime
import time
import pytz
api_id = apiid #my.telegram.org dan olgan apiidni qoying
api_hash = "Apihash" #my.telegram.org dan olgan apihash ni qoying
app = Client("my_account",api_id,api_hash)
app.start()
while True:
    ok = pytz.timezone("Asia/Tashkent")
    x = datetime.datetime.now(tz=ok)
    x = x.strftime("%H:%M")
    app.send(functions.account.UpdateProfile(
    first_name="꧁♡࿆𝐵𝑎𝑑𝑟𝑖𝑑𝑑𝑖𝑛 𝑆𝑎𝑣𝑟𝑖𝑦𝑒𝑣♡࿆꧂" str(x),
    about="Meni bilgan biladi, Bilmagan o'zi biladi👌😏➢ " +str(x)
    ))
    time.sleep(30)
