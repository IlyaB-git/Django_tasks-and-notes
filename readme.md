##Это сервис, в котором можно хранить свои задачи и делать заметки
У задачи можно указать:
- название
- выбрать категорию (или создать новую)
    - у каждой категории можно изменить цвет, чтобы было удобнее ориентироваться
- добавить описание
- указать дату и время

У заметки можно указать:
- название
- добавить описание
- добавить картинку

На главной странице сразу отображаются и заметки и задачи. При желании можно отобразить только задачи или только заметки. Задачи можно отмечать выполнеными. Ненужные записи можно перемещать в корзину.

####Запуск сервера
У вас должен быть установлен ```Python``` и установленны все ```requirements.txt```

1. ```venv/Scripts/activate.bat```
2. ```Django_tasks-and-notes/python manage.py runserver```

![Скиншот](images/demo1.png)
![Скиншот](images/demo2.png)