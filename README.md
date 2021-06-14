# Я - Гуль (бот), новая версия, работает в чатах
## Поставь звездочку, пожалуйста!
![Работа бота](https://github.com/error1001es/teleghoul/blob/main/screenshots/bot_work.png)<br>

**После установки перейдите в раздел *Запуск*, он находится снизу**

___
## Установка на Андроид
Скачиваем приложение [Termux](https://play.google.com/store/apps/details?id=com.termux) в Play Market<br>
Открываем и пишем команды снизу поочерёдно<br>

#### Для копирования команды нажмите справа от неё

*Обновляем*

	apt-get update
*Ставим git и python*

	apt-get install git python
Если спросит `Do you want to continue? [Y/n]` отвечаем `Y` и продолжаем дальше<br>
*Устанавливаем pyrogram*

	pip install pyrogram
*Клонируем репозиторий*

	git clone https://github.com/error1001es/teleghoul.git
**После установки перейдите в раздел Запуск (*просто пролистайте вниз*)**

___
## Установка на Пк
Скачиваем [git](https://git-scm.com/downloads) и [python](https://www.python.org/downloads/)<br>
**При установке Python обязательно ставим галочку `Add to PATH`**<br>

*Устанавливаем pyrogram*

	pip install pyrogram
*Клонируем репозиторий*

	git clone https://github.com/error1001es/teleghoul.git
___
## Запуск
	python teleghoul/index.py
	
Затем вводите номер телефона привязанный к **ВАШЕМУ** телеграму<br>
В телеграм придёт код, введите его и бот заработает

![Запуск](https://github.com/error1001es/teleghoul/blob/main/screenshots/startup.png)<br>
**Если бот выдал пустую строку, значит он работает, *последующие запуски выполняются без каких-либо установок***<br>

Пишите `Я гуль` в чатах и спам начнется<br>
*Одновременно запускать лучше только в 1 чат*<br>

***Пожалуйста, не тестируйте работу на мне***<br>

Если возникли ошибки, кидайте скрины в [ЛС](https://t.me/ghoul4s)

___
## Пожертвовать
Нажми [сюда](https://www.donationalerts.com/r/ponyal), чтобы пожертвовать)

___
## Дополнительные возможности
Вы можете открыть файл *config.py* в файловом менеджере или командой `nano teleghoul/config.py`<br>
start_command - команда для запуска<br>
end_message - сообщение после конца цикла<br>
messages_per_second - ставьте число до 10 (кол-во сообщений в секунду), если поставить слишком большое значение, сообщения станут отправляться с задержкой, придется менять его и перезапускать бота

