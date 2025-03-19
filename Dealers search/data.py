regions = {'Алтайский край': '22', 'Амурская область': '28', 'Архангельская область': '29',
            'Астраханская область': '30', 'Белгородская область': '31', 'Брянская область': '32',
            'Владимирская область': '33', 'Волгоградская область': '34', 'Вологодская область': '35',
            'Воронежская область': '36', 'Еврейская автономная область': '79', 'Забайкальский край': '75',
            'Ивановская область': '37', 'Иркутская область': '38', 'Кабардино-Балкарская Республика': '07',
            'Калининградская область': '39', 'Калужская область': '40', 'Камчатский край': '41', 
            'Карачаево-Черкесская Республика': '09', 'Кемеровская область': '42', 'Кировская область': '43', 
            'Костромская область': '44', 'Краснодарский край': '23', 'Красноярский край': '24', 'Крым': '91', 
            'Курганская область': '45', 'Курская область': '46', 'Ленинградская область': '47', 'Липецкая область': '48', 
            'Магаданская область': '49', 'Москва': '77', 'Московская область': '50', 'Мурманская область': '51', 
            'Ненецкий автономный округ': '83', 'Нижегородская область': '52', 'Новгородская область': '53', 
            'Новосибирская область': '54', 'Омская область': '55', 'Оренбургская область': '56', 
            'Орловская область': '57', 'Пензенская область': '58', 'Пермский край': '59', 'Приморский край': '25', 
            'Псковская область': '60', 'Республика Адыгея': '01', 'Республика Алтай': '04', 
            'Республика Башкортостан': '02', 'Республика Бурятия': '03', 'Республика Дагестан': '05', 
            'Республика Ингушетия': '06', 'Республика Калмыкия': '08', 'Республика Карелия': '10', 
            'Республика Коми': '11', 'Республика Марий Эл': '12', 'Республика Мордовия': '13', 
            'Республика Саха (Якутия)': '14', 'Республика Северная Осетия — Алания': '15', 
            'Республика Татарстан': '16', 'Республика Тыва': '17', 'Республика Хакасия': '19', 
            'Ростовская область': '61', 'Рязанская область': '62', 'Самарская область': '63', 
            'Санкт-Петербург': '78', 'Саратовская область': '64', 'Сахалинская область': '65', 
            'Свердловская область': '66', 'Севастополь': '92', 'Смоленская область': '67', 
            'Ставропольский край': '26', 'Тамбовская область': '68', 'Тверская область': '69', 
            'Томская область': '70', 'Тульская область': '71', 'Тюменская область': '72', 
            'Удмуртская Республика': '18', 'Ульяновская область': '73', 'Хабаровский край': '27', 
            'Ханты-Мансийский автономный округ — Югра': '86', 'Челябинская область': '74', 
            'Чеченская Республика': '20', 'Чувашская Республика': '21', 'Чукотский автономный округ': 
            '87', 'Ямало-Ненецкий автономный округ': '89', 'Ярославская область': '76'}

icon = 'iVBORw0KGgoAAAANSUhEUgAAAB8AAAAgCAYAAADqgqNBAAAABGdBTUEAALGPC/xhBQAAAAlwSFlzAAAOwwAADsMBx2+oZAAACHBJREFUWEfV' \
       'VglQVFcWfd1NA60iIIvsuJABQUAgiqKI475k4haHmIyjoGFcMMQFkEbiwkgcsRyjCC4RQTQKKAphaTYVFAUVUVFciSBEFsG23QG7z9z//TVV' \
       'bokm1lTN6XrVv3//e85997+7sP8rGDKmH9K7u9OP4waPOji8/+RdXvZTo/pYjg806OTaixnqC499OHgwZrzNyWx+2jSX/LRZzk1Z8wagcJ4H' \
       'jvn3xRG/Psijb0WAOxRfOTdn+7oWbujVOWgiY9aC+e/DRGZovdNWuu7YzD7NJQt6I2OSNTY7GSDSqAtCJQwhjCFYzBCmLUYU3dvqYoCsiT1' \
       'xTu6JQn+Hh3HmXePns8FOAt27YoVWVDcWrphmeV+VHQqoLyElKBALSCyESbFUrIVlIjGCRbpYJtFBiJYUoWIdfMMkWErPXM7KBHAFLbmByJ' \
       'li3ba9q96/GFuoI5C/HcHGH3nv7tft7O0tY6BR5uM50XCrtaEWK80tsIzI5dq0W3JgITmwRCJBmJYW5Dp0Tf/FDx8BjVqNNrLRENStxbi1eQ' \
       'IS++uVx1p42Qsyb4Kt7jZ748Z7RXOgwSMyJwL6dGg4eeBoXBztjmGVRIwgJsamfhZYb2dG0dAiB8QIZSLUFB/nn9U87yBxNdR03Y77UB7yw1' \
       'Zbg0xB6HWMZCP1k7wMWp79ksYTULxpaaAmcTXnRFsbYry8sZgc2DvOFBXrB6FinQMSvI3xDxLeN82Xt3rOi5I4b6Xh77Wc24s4B71iQep1+L' \
       'GxJqkeXVVtdWm87H9BZCRNOwAupiYg0ccExYE9UJfxZ9QfGIgCfyvsGW+JqtwUeorE1RSpF5r87jk8vZyCePfuFYLU6/Bm7ubbBho9elC1mzd' \
       '4FZx4U2UersW64PwGByjm2qFwjiMqNzrg5s5+aLym4M/HS44T2p91oKVwAzZ/bFRDMtov1F6BNzM23znM8tGhv9lhx9QvUZmdgbYO7ugAqu' \
       'ZbUF7Yh+bzaWgo8ENjgTfihxgjYaQZmgsH4U5uABoq0tFaHouHd6p4G+WdWzi+dRu+cx+ITF87OowWDSbMpIsg9zL6s05mSSMsHqb+RQ/z6' \
       'b1y73aD0wCUbwlHy7ERuJ3siEfKajyhENxIn4hLa3rg8kZ7tBz+nL+nul+H+mQ3qBSjULR2NlYZ2vK1IJBWznQbJI6xarJjdl0FuZcxhJmZ' \
       'xA81V2V/YUJpQ/lMp3iFiOFqnAeU6fao3j8ctWV5UFUX4tS3rtg/cwRi3a1xOtIHylvZqC5NQ/WeCWhM7oXre12woivlv7aUMkQMxXRr7Bpt' \
       '1mTP7PUEuZfhwT7pFD/YtD5jOicuoqJCJ3iyLZ6d64e6VBfcTfHCz0nOOLveGlt8PFGZU4wL+w/gyL/X4Ow6ZzSkuKHpkCtqDzrjaakrsvx6' \
       'krAu7V6CTOKkg1pvxQbKBLlXAdEON8NrCn9zfE0/wkXaOLvGFfeKPVB3mFaGHVry3HBlhyNSP/8rTsbG4PKJfBTHbMSlH/pDme+Nhgxv3DncF' \
       '6qjrqj63h5yqQ6f/wWzTLBnqOVVTkMQex0bPzItKZpjhkUUqshuXdCk8MTD05/SoQpAVcpw3Eh0R03qEJREL0BFYQHOJCejYN1c1B8ch1+SfX' \
       'A9YSgac+dAdXw8Hpzoi01/MqUoinEiwBxx/bu/Pc85RFgZJZxaYI4wet9xA8zx5Kw37p38BLczl+Jm+XFUZSfhxk9RKIsejN2TJyBnVSjOxI3' \
       'FzYIo3KT/6spOorpgFZrzB6D9vCfSp9gimLjKFpohxtEmUZB5M8K1TZaVLOyBCDpo6b7WRDCBGsQ4KCu3U8GgPL+qwI1Df8fN3LUoXTcVRd8M' \
       'peISjaoDgWgs24pnlGL3agrRmDMaT0564tRKa8oaMc4H2SBK34z6zq8gkHUb+dMUC+TJp+DaVg80532G1p8L+YL19HETbueGoXy1Ba7t/wJ3' \
       'Tgbjbv5s1KYFoizSFLWHZ0DVdIUvNMrW62g6Ohc1+1xRGv0VjszuiZlMZ5gg82ZwqRDnqNf8+IIcDZcPUl7f5ck48WcPmqGqPYrogW5InWSI' \
       'xxXTobowHSWRTlhuZoSa0kNou1fHNyKuILe3aygK+dDcSsCeMcZKw3eZdCJ0pbHVMaPJ/Dlfq6mzQE2LQ5UiD0FiMbVWMSq+HwFVmT/khjrw' \
       'p2OcuYh6P4F7VKPu4LsBZ9WaMw/RlnppAv2vw5dp90ny6qRpr0niybjGwqGj/TGiXT0oE7jqJ8aWQTbIDBjAF5EQWst0Zai7ePpFbaeezvUC' \
       'PC6HYrYl5jLtTwX630YI67q7cqUjtaiGFySEUz9sJxIaJKh3B0u06BQzEhbRtRThNFRwvT5p/FjaLRczDhooc2djbU/Z1QDGpAL1b2M469v9' \
       'n2ailuas+TzRA9UTrO5hw9f7EBJfIhVTAZFCzr0CbmlJsFwk4qeZi2kHeOlHtXH4cZiMbAzHCLTvjplMMmnnxzKoa3YgfZWcpheGCNrhUkr' \
       'DRRIRL8gL05LTKBVBTnG7X93LCQ/rD6J0jiU5I9kk0L0/5jHdb9PHWqFosTvtVspXvlByYAmNUnKxCGH0HUKvIIxCv1Rbi3dw3wRbnAnqje' \
       'UyWYkPO6olUP0++DHRmoxRdtTJhiLKXJ+v+1wEIiQ0vVLtlktF1AFFCBXpIGeGPcoXOSNMJrs4ubOLqUDxx0D9/evdbjS3RXkiYTDXeLRpdK' \
       'awc1EgZ9bY6KEs3AlZvraQM92CxczDWDD9MJjFJKMijWQ3Tsy1x4lAJ3xnoccLc/PbpeWO2OVuoFnCZKvp1ts71x+BD9M3WMykWxI9jVAa7I' \
       'DSFX1R9KUVvpXJzs3g5pH/BSaRH8s7dy6O6WHYFMrElPLvkccfCp8x1k24fE8w9h/tyan+u757owAAAABJRU5ErkJggg=='
# from bs4 import BeautifulSoup
# from pprint import pprint
# a = '''<select name="customerregion" class="form-control" id="id_customerregion">
#   <option value="" selected=""></option>

#   <option value="22">Алтайский край</option>

#   <option value="28">Амурская область</option>

#   <option value="29">Архангельская область</option>

#   <option value="30">Астраханская область</option>

#   <option value="31">Белгородская область</option>

#   <option value="32">Брянская область</option>

#   <option value="33">Владимирская область</option>

#   <option value="34">Волгоградская область</option>

#   <option value="35">Вологодская область</option>

#   <option value="36">Воронежская область</option>

#   <option value="79">Еврейская автономная область</option>

#   <option value="75">Забайкальский край</option>

#   <option value="37">Ивановская область</option>

#   <option value="38">Иркутская область</option>

#   <option value="07">Кабардино-Балкарская Республика</option>

#   <option value="39">Калининградская область</option>

#   <option value="40">Калужская область</option>

#   <option value="41">Камчатский край</option>

#   <option value="09">Карачаево-Черкесская Республика</option>

#   <option value="42">Кемеровская область</option>

#   <option value="43">Кировская область</option>

#   <option value="44">Костромская область</option>

#   <option value="23">Краснодарский край</option>

#   <option value="24">Красноярский край</option>

#   <option value="91">Крым</option>

#   <option value="45">Курганская область</option>

#   <option value="46">Курская область</option>

#   <option value="47">Ленинградская область</option>

#   <option value="48">Липецкая область</option>

#   <option value="49">Магаданская область</option>

#   <option value="77">Москва</option>

#   <option value="50">Московская область</option>

#   <option value="51">Мурманская область</option>

#   <option value="83">Ненецкий автономный округ</option>

#   <option value="52">Нижегородская область</option>

#   <option value="53">Новгородская область</option>

#   <option value="54">Новосибирская область</option>

#   <option value="55">Омская область</option>

#   <option value="56">Оренбургская область</option>

#   <option value="57">Орловская область</option>

#   <option value="58">Пензенская область</option>

#   <option value="59">Пермский край</option>

#   <option value="25">Приморский край</option>

#   <option value="60">Псковская область</option>

#   <option value="01">Республика Адыгея</option>

#   <option value="04">Республика Алтай</option>

#   <option value="02">Республика Башкортостан</option>

#   <option value="03">Республика Бурятия</option>

#   <option value="05">Республика Дагестан</option>

#   <option value="06">Республика Ингушетия</option>

#   <option value="08">Республика Калмыкия</option>

#   <option value="10">Республика Карелия</option>

#   <option value="11">Республика Коми</option>

#   <option value="12">Республика Марий Эл</option>

#   <option value="13">Республика Мордовия</option>

#   <option value="14">Республика Саха (Якутия)</option>

#   <option value="15">Республика Северная Осетия — Алания</option>

#   <option value="16">Республика Татарстан</option>

#   <option value="17">Республика Тыва</option>

#   <option value="19">Республика Хакасия</option>

#   <option value="61">Ростовская область</option>

#   <option value="62">Рязанская область</option>

#   <option value="63">Самарская область</option>

#   <option value="78">Санкт-Петербург</option>

#   <option value="64">Саратовская область</option>

#   <option value="65">Сахалинская область</option>

#   <option value="66">Свердловская область</option>

#   <option value="92">Севастополь</option>

#   <option value="67">Смоленская область</option>

#   <option value="26">Ставропольский край</option>

#   <option value="68">Тамбовская область</option>

#   <option value="69">Тверская область</option>

#   <option value="70">Томская область</option>

#   <option value="71">Тульская область</option>

#   <option value="72">Тюменская область</option>

#   <option value="18">Удмуртская Республика</option>

#   <option value="73">Ульяновская область</option>

#   <option value="27">Хабаровский край</option>

#   <option value="86">Ханты-Мансийский автономный округ — Югра</option>

#   <option value="74">Челябинская область</option>

#   <option value="20">Чеченская Республика</option>

#   <option value="21">Чувашская Республика</option>

#   <option value="87">Чукотский автономный округ</option>

#   <option value="89">Ямало-Ненецкий автономный округ</option>

#   <option value="76">Ярославская область</option>

# </select>'''
# soup = BeautifulSoup(a, 'html.parser')
# b = soup.find_all('option')
# c={}
# for i in b:
#     c[i.string] = i.attrs['value']

# print(c)