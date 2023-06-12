from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/working_hours')
b2 = KeyboardButton('/contacts')
b3 = KeyboardButton('/menu')
# b4 = KeyboardButton('Share my number', request_contact=True)
# b5 = KeyboardButton('Send my location', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

# kb_client.add(b1).add(b2).insert(b3)
kb_client.add(b1).row(b2, b3)
# kb_client.row(b4, b5)
