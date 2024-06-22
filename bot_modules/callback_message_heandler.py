from aiogram.types import CallbackQuery
from .dispatcher_bot import dispatcher
from .keyboard_bot import main_keyboard, main_inline_keyboard
from .buttons_bot import button_delete_user, button_is_admin
from .create_bot import bot
import sqlite3

number_thread_user = 2

@dispatcher.callback_query()
async def callback_handler(callback: CallbackQuery):

    data_base = sqlite3.connect(database = 'flask_cookie_test/project/data.db' )
    cursor = data_base.cursor()
    try:
        if callback.data == 'users':

            for count in callback:
                print(count)

            cursor.execute('SELECT * FROM user')
            data_users = cursor.fetchall()
            main_inline_keyboard.inline_keyboard[0] = [button_delete_user, button_is_admin]

            for user in data_users:
                # user = [1, 'Nick', '0000', 0]
                button_delete_user.callback_data = f'delete-{user[0]}'
                if int(user[3]) == 0:

                    button_is_admin.callback_data = f"is_admin-{user[0]}" # 'admin-1'
                    button_is_admin.text = "IS ADMIN"
                else:
                    button_is_admin.text = 'NOT ADMIN'
                    button_is_admin.callback_data = f"remove_admin-{user[0]}" # 'notadmin-1'

                await bot.send_message(
                    chat_id= callback.message.chat.id,
                    message_thread_id= number_thread_user,
                    text= f'ID: {user[0]}\nNAME: {user[1]}\nPASSWORD: {user[2]}\nIS_ADMIN: {user[3]}\n',
                    reply_markup = main_inline_keyboard
                )
        elif 'delete' in callback.data:
            user_id = callback.data.split('-')[-1] # user_id = ['delete', '2'] => user_id = '2'
            button_delete_user.text = "NO"
            button_delete_user.callback_data = f'no-{user_id}'

            button_is_admin.text = "YES"
            button_is_admin.callback_data = f'yes-{user_id}'
            main_inline_keyboard.inline_keyboard[0] = [button_delete_user, button_is_admin]

            await callback.message.edit_reply_markup(inline_message_id= callback.inline_message_id,reply_markup= main_inline_keyboard)

        elif 'yes' in callback.data:
            user_id = int(callback.data.split('-')[-1])
            cursor.execute('DELETE FROM user WHERE id = ?', [user_id])
            await callback.message.delete()
            button_delete_user.text = 'DELETE USER'  
            button_delete_user.callback_data = f'delete-{user_id}'
            
        elif 'no' in callback.data:

            user_id = int(callback.data.split('-')[-1])

            cursor.execute("SELECT * FROM user WHERE id = ?", [user_id])
            user = cursor.fetchall()[0] # => user = [1, 'Nick', 0000, 1]

            button_delete_user.text = 'DELETE USER'
            button_delete_user.callback_data = f'delete-{user_id}'

            if int(user[3]) == 0:

                button_is_admin.text = 'IS ADMIN'
                button_is_admin.callback_data = f'is_admin-{user_id}'
            else:

                button_is_admin.text = 'NOT ADMIN'
                button_is_admin.callback_data = f'remove_admin-{user_id}'

            main_inline_keyboard.inline_keyboard[0] = [button_delete_user, button_is_admin]
            await callback.message.edit_reply_markup(inline_message_id= callback.inline_message_id,reply_markup= main_inline_keyboard)

        elif "is_admin" in callback.data:
            user_id = int(callback.data.split('-')[-1])
            cursor.execute('UPDATE user SET is_admin = ? WHERE id = ?', [1, user_id])
            button_is_admin.text = 'NOT ADMIN'
            button_is_admin.callback_data = f'remove_admin-{user_id}'

            cursor.execute('SELECT * FROM user WHERE id =?', [user_id])
            user = cursor.fetchall()[0] # => user = [1, 'Nick', 0000, 1]
            await callback.message.edit_text(
                text =  f'ID: {user[0]}\nNAME: {user[1]}\nPASSWORD: {user[2]}\nIS_ADMIN: {user[3]}\n', 
                reply_markup = main_inline_keyboard
            )
        # 
        elif "remove_admin" in callback.data:

            user_id = int(callback.data.split('-')[-1])
            cursor.execute("UPDATE user SET is_admin = ? WHERE id = ?", [0, user_id])

            button_is_admin.text = "IS ADMIN"
            button_is_admin.callback_data = f"is_admin-{user_id}"

            cursor.execute('SELECT * FROM user WHERE id =?', [user_id])
            user = cursor.fetchall()[0]
            await callback.message.edit_text(
                text =  f'ID: {user[0]}\nNAME: {user[1]}\nPASSWORD: {user[2]}\nIS_ADMIN: {user[3]}\n', 
                reply_markup = main_inline_keyboard
            )
    except Exception as e:
        await callback.message.answer(text = f"{e}")
    
    data_base.commit()
    data_base.close()
      
      
      
      
        

