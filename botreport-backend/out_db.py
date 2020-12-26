import sqlite3
import datetime


conn = sqlite3.connect('sports.db')

def new():
    c = conn.cursor()
    c.execute('''
        CREATE TABLE posts
        (text_event text, text_trivia text, player text, match text, date_event text, league text, type_event text)
    ''')
    c.close()

def post(text: str, trivia: str, player: str, match: str, league: str, type_event: str):
    c = conn.cursor()
    c.execute(f'''
        INSERT INTO posts
        (text_event, text_trivia, player, match, date_event, league, type_event)
        VALUES
        (?, ?, ?, ?, ?, ?, ?)
    ''', (text, trivia, player, match, str(datetime.datetime.now().strftime("%m-%d-%Y, %H:%M")), league, type_event))
    conn.commit()
    c.close()