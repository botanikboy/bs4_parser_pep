
# Проект парсинга pep на основе beautifulsoup4

Установите зависимости командой:
```
pip install -r requirements.txt
```
Предусмотрено три режима работы парсера:
- ## whats_new
Собирает данные со страницы https://docs.python.org/3/whatsnew/.
выводит перечень ссылок на статьи и авторов публикаций.

Команда для запуска:
```
python .\src\main.py whats-new
```
- ## latest_versions
Получает список ссылок на все версии Python со страницы https://docs.python.org/3/.
Выводит ссылку на документацию, версию и статус версии.

Команда для запуска:
```
python .\src\main.py latest-versions
```
- ## download
Скачивает актуальную документацию со страницы https://docs.python.org/3/download.html в формате А4 файлом .pdf и сохраняет в папке ./downloads/

Команда для запуска:
```
python .\src\main.py download
```
- ## pep
Собирает данные о стандартах PEP со страницы https://peps.python.org/.
Производит подсчет найденных стандартов, и количество стандартов по статусам.

Команда для запуска:
```
python .\src\main.py pep
```

Для всех режимов кроме download предусмотрены три варианта вывода данных в зависимости от опционального аргумента --output.

pretty - вывод в терминал через модуль prettytable
file - вывод в файл .csv сохраняется в папке ./results/
без аргумента - вывод в терминал

## Технологии
- [Python](https://www.python.org/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

## Об авторе
Разработано:
[Илья Савинкин](https://www.linkedin.com/in/ilya-savinkin-6002a711/)
