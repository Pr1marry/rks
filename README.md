# Апи и связанный html/js шаблон с сортировкой по url.
## Тех. cтек: django, drf, psql, docker, html, js.
<img width="269" alt="Снимок экрана 2022-11-01 в 20 33 56" src="https://user-images.githubusercontent.com/104326167/199299815-1ef7208e-7cc3-45e3-9fef-8fd141204d01.png">
<img width="258" alt="Снимок экрана 2022-11-01 в 20 34 14" src="https://user-images.githubusercontent.com/104326167/199299877-cfbae129-1336-4891-baa4-a2bea8f80bf2.png">


### Создал эндпоинт:
##### http://localhost:8000/api/table_list : Возвращает список объектов таблицы

<img width="1440" alt="Снимок экрана 2022-11-01 в 20 32 48" src="https://user-images.githubusercontent.com/104326167/199299468-3141235c-bac3-40c2-9842-203fa8523844.png">

##### Передаем параметр сортировки в этот эндпоинт и получаем сортировку по элементу
##### Пример - http://localhost:8000/api/table_list?sort=artist

<img width="1440" alt="Снимок экрана 2022-11-01 в 20 33 33" src="https://user-images.githubusercontent.com/104326167/199299753-cc9bf823-b6af-4048-b5eb-927270978528.png">



# Инструкция по установке проекта:

### 1: Клонируем проект к себе командой: git clone https://github.com/Pr1marry/rks
### 2: Запускаем контейнеры командой: docker-compose up -d
### 3: Приложение будет доступно на 8000 порту в Debug-моде.<img width="1438" alt="Снимок экрана 2022-11-01 в 20 32 32" src="https://user-images.githubusercontent.com/104326167/199299333-a95d5894-a677-4c61-adba-3b0031951f61.png">
