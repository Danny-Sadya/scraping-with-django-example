<h2 align="center">SiteSoftTest</h2>

Скрейпер Хабра.

### Инструменты разработки

**Стек для веба:**
- Django
- Postgres
- Celery
- RabbitMQ

**Стек для парсера:**
- aiohttp
- asyncio
- Bs4

## Старт

#### 1) Создать образ

    sudo docker-compose build

##### 2) Запустить контейнер

    sudo docker-compose up
    
##### 3) Найти CONRAINER ID образа, который хранит комманду запуска сервера (Python manage.py runserver)

    sudo docker ps
    
##### 4) Создать суперпользователя, сделать миграции

    sudo docker exec -it <CONTAINER_ID> python manage.py makemigrations
    sudo docker exec -it <CONTAINER_ID> python manage.py migrate
    sudo docker exec -it <CONTAINER_ID> python manage.py createsuperuser
    
## Что внутри проекта?

* Внутри проекта реализован скрейпер, у которого есть две основные функции: сбор статей с главной страницы хабра и их последующий парсинг (***run_base_scraper***), 
  либо парсинг статей, по заданному списку URL (***run_specific_posts_scraper(ulr_list)***). Обе эти функции **возвращают** список с данными, которые были собраны за свою работу
  <h6>Данный скрипт можно найти по пути /src/posts/services/habr_scraper.py и запустить его отдельно от Django (например, для проверок)</h6>
* Внутри проекта реализована планировка задач с помощью Celery + RabbitMQ. Планировщик задач с некоторой периодичностью (можно настроить) вызывают две вышеописанные функции скрейпера
  и сохраняют результаты работы в **Postgres** через модели от **DjangoORM**
  <h6>Селери видит два таска. логика в обоих тасках была прописана так, чтобы модели с одинаковым post_url не были перезаписаны или пересозданы.
  
  
  Расположение файла с настройками Celery: /config/celery.py
  
  Расположение файла с логикой тасков: /src/posts/tasks.py</h6>
 
* Реализованы две модели: модель самого поста (PostModel), которая включает в себя header, author_name, e.t.c, и модель поста, который нужно будет отскрейпить (PostToScrapeModel), включающий два поля:
  post_url и scraped:bool
* Когда экземпляры модели PostToScrapeModel попадают к планировщику задач, таск менеджер отбирает инстансы, которые еще не обходил (=> scraped=False)
  и после отдачи их скрейперу, устанавливает sсraped=True и создает модели PostModel на основании данных, полученных от скрейпера
* Внутри проекта реализована **Django-Admin**, которая позволяет следить за инстансами, которые уже были созданы, а также создавать инстансы постов, которые нужно отскрейпить.


<h2 align="center">Наверное, на этом все. Спасибо за просмотр :)</h2>
