from jinja2 import Template
import sqlite3
from reader_city_model import get_amount, get_book

amount = 3
price = 670.99

con = sqlite3.connect("store.sqlite")
f_damp = open('store.db', 'r', encoding='utf-8-sig')
damp = f_damp.read()
f_damp.close()
con.executescript(damp)
con.commit()

df_book = get_book(con, amount, price)
df_amount = get_amount(con)
con.close()

f_template = open('reader_city_templ.html', 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

template = Template(html)
result_html = template.render(
    amount=amount,
    price=price,
    combo_box=df_amount,
    book=df_book,
    len=len
)

f = open('reader_city.html', 'w', encoding='utf-8-sig')
f.write(result_html)
f.close()
