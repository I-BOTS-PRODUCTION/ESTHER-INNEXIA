from Innexia.modules.buttons.userhelp import *



__help__ = """We promise to keep you latest up-date with the latest technology on telegram. 
we updradge alicia everyday to simplifie use of telegram and give a better exprince to users.
Click on below buttons and check amazing tools for users.
"""  # no help string

__button__ = [ InlineKeyboardButton(text="Horoscope", callback_data="innexiauser_"),
            InlineKeyboardButton(text="AFK", callback_data="innexiauserafk_"),
            InlineKeyboardButton(text="About", callback_data="innexiauserabout_"),

] 
__buttons__ = [InlineKeyboardButton(text="Info", callback_data="innexiauserinfo_"),               
              InlineKeyboardButton(text="Extra", callback_data="innexiauserextra_"),
]


__mod_name__ = "User"


dispatcher.add_handler(user_callback_handler)
dispatcher.add_handler(user_afk_callback_handler)
dispatcher.add_handler(user_about_callback_handler)
dispatcher.add_handler(user_info_callback_handler)
dispatcher.add_handler(user_extra_callback_handler)
