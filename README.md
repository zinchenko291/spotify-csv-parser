# spotify-csv-parser

Программа ищет на YTMusic музыку из csv файла, а затем формирует список ссылок на эту музыку.

Программа использует информацию из файла, полученного на [spotlistr](https://www.spotlistr.com/). Нужно выбрать раздел [export playlist](https://www.spotlistr.com/export/spotify-playlist). Файл должен содержать поля: `Arist(s) Name`, `Track Name`, `Album Name`, а сепаратором служит знак `;`.