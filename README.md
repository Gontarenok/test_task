Проект разработан на:  
Python 3.10.1  
PyCharm 2022.1.3 (Professional Edition)  

Для установки проекта необходимо развернуть все библиотеки из файла requirements.txt командой в терминале:  
python -m pip install -r requirements.txt

Для запуска API использовать команду:  
python manage.py runserver

В API можно использовать следующие URL:

admin/  - авторизация  
api/v1/task_2 /create/  - для создания записи в БД  
api/v1/task_2 /all/  - для получения всех записей из БД  
api/v1/task_2 /edit/<int:pk>/  - для редактирования записей в БД  
api/v1/task_2 /upload/  

Разработчик: Гонтаренко Виктория