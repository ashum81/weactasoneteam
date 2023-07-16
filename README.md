# Работаем как одна команда

## Компоненты

### votebot

Бот, который спрашивает вопросы (используется для тестирования, для самой викторины не нужен).  
Вопросы берет из файла questions.json.  
Токен от бота положить в файл .env.example и переименовать файл в .env.

### client

Клиент для участия в викторине, пересылает вопросы client2.  
Для авторизации нужны api_id и api_hash.

* votebot - имя бота викторины (для теста использовать бота из предыдущего абзаца, потом поменять на реального бота викторины).

* tmp_client - имя вспомогательного аккаунта для пересылки вопросов.

### client2

Клиент для получения правильных ответов, отвечает на присланный вопрос и отправляет правильный ответ client.  
Для авторизации нужны api_id и api_hash.

* main_client - имя основного аккаунта для отправки правильных ответов.

## Как получить api_id и api_hash

Логинимся на <https://my.telegram.org>.  
Переходим на <https://my.telegram.org/apps>.  
Заполняем поля и получаем api_id и api_hash.

При первом запуске скрипта запросится телефон, код и пароль если есть двухфакторная авторизация:  
Please enter your phone (or bot token): +79021234567  
Please enter the code you received: 12345  
Please enter your password:  
Signed in successfully as Иван Иванов

После этого сессия сохранится в файле *.session.

## Пример установки на <https://vds.selectel.ru>

Ubuntu 22.04, 200руб/мес, Москва

``` bash
# для aiogram нужен python 3.7
apt update
apt install git
git clone https://github.com/ashum81/weactasoneteam.git
cd weactasoneteam
apt install python3-pip
pip3 install --upgrade setuptools
pip3 install -r votebot/requirements.txt
pip3 install -r client/requirements.txt
mv votebot/.env.example votebot/.env
nano votebot/.env
nano client/client.py
nano client2/client2.py
cd votebot
python3 votebot.py

# terminal2
cd weactasoneteam/client
python3 client.py

# terminal3
cd weactasoneteam/client2
python3 client2.py
```
