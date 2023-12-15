import pandas as pd


def get_amount(conn):
    return pd.read_sql('''
        SELECT
            amount,
            price
        FROM book
    ''', conn)


def get_book(conn, amount, price):
    return pd.read_sql('''
        SELECT
            title AS Название,
            name_author AS Автор,
            name_genre AS Жанр
        FROM book
            JOIN author USING (author_id)
            JOIN genre USING (genre_id)
        WHERE amount = :amount AND price = :price
    ''', conn, params={"amount": amount, "price": price})
