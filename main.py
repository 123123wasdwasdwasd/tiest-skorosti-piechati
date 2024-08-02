import random
import time

print("Hello world! Это программа расчета скорости печати. Вам будет выведена фраза которую вы должны напечетать, чем быстрее тем выше результат.")
mode = input("Выберите язык, EN или RU. \n")
input("Нажмите ENTER когда вы будете готовы! \n")
PhrasesRU = [
  "Привет, мир!",
  "Приветики!",
  "Здравствуйте, великоуважаемый сударь!",
  "Ку!",
  "Досвидания, мадмуазель!",
]
PhrasesEN = [
  "Hello, world!",
  "Goodbye, sir.",
  "Just kidding!",
  "What's up?",
  "You're welcome!",
]
userphrase = ""
outputphrase = ""
starttime = 0.0
endtime = 0.0
if mode.lower() == "en":
  outputphrase = random.choice(PhrasesEN)
  starttime = time.time()
  userphrase = input(f"{outputphrase} \n")
  endtime = time.time()
elif mode.lower() == "ru":
  outputphrase = random.choice(PhrasesRU)
  starttime = time.time()
  userphrase = input(f"{outputphrase} \n")
  endtime = time.time()
else:
  print("Ошибка: введен недоступный язык! Доступные языки в данной версии программы: EN и RU")
if userphrase == outputphrase:
  resulttime = endtime - starttime
  symbolspersecond = len(userphrase) / (resulttime)
  print("ваша скорость печати", symbolspersecond, "символов в год")
  print("ваше время, затраченное на печать равно", resulttime, "секундов")
else:
  print("ты неправильно ввел(а) слово!")