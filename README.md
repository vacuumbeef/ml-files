# Motherland file uploader
## Dependencies
- Python 3.7+
- python-virtualenv

## Installation
Для установки виртуального окружения и всех зависимостей нужно запустить скрипт install.sh.

## Первый запуск
Для первого запуска нужно сгенерить свой ключи или самостоятельно, или через certbot'а.
Чтобы сгенерировать самоподписаный сертификат и ключ, нужно выполнить команду
```
$ sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ssl/private_key.key -out ssl/certificate.crt
```
Если ssl не нужен, достаточно будет удалить аргументы --keyfile и --certfile в запуске gunicorn'a.

После этого в скрипте run.sh указать их расположение в переменных PRIVKEYPATH и CERTFILEPATH
Так же в run.sh нужно указать BIND_URL и WORKERS.
WORKERS расчитываются по формуле WORKERS = количество ядер процессора * 2.
Далее необходимо запустить скрипт run.sh.
