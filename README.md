# Мой Дом Онлайн

### Технологии:

- Python 3.10
- Django 4.2
- DRF 3.14.0
- PostgreSQL 15
- Docker

## Как запустить

- В директории с проектом создать файл .env и заполнить по образцу .env.example

- В папке с проектом в терминале прописать:

```shell
docker-compose up -d
```

> Проект будет доступен по ссылке
> ***[http://localhost/admin/](http://localhost/admin/)***

По адресу [http://localhost/swagger/](http://localhost/swagger/) доступна документация по API.

- Как остановить и очистить контейнеры:

- В папке с проектом в терминале прописать:

```shell
docker-compose down
```