README.md
Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
git clone git@github.com:morongod/api_final_yatube.git
cd yatube_api

Cоздать и активировать виртуальное окружение:
python -m venv venv
source venv/Scripts/activate

Установить зависимости из файла requirements.txt:
python -m pip install --upgrade pip
pip install -r requirements.txt

Выполнить миграции:
python manage.py migrate

Запустить проект:
python3 manage.py runserver