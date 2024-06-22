import aiogram

buttons_start = aiogram.types.KeyboardButton(text = 'START')

button_is_admin = aiogram.types.InlineKeyboardButton(text= "IS_ADMIN", callback_data= "is_admin")
button_delete_user = aiogram.types.InlineKeyboardButton(text= "DELETE_USER", callback_data= "delete")
button_get_users = aiogram.types.InlineKeyboardButton(text= "GET_USERS", callback_data= "users")
