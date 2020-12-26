from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('sports.db', check_same_thread=False)

@app.route('/')
def greet():
    return 'BotReport API - up and running!'

@app.route('/api/live-news')
def get():
    c = conn.cursor()
    c.execute('SELECT * FROM posts')
    print(conn, c)
    li = c.fetchall()
    print(li)
    d = {'live-news': []}
    for i in li:
        print(i)
        d['live-news'].append(
            {
                'text': i[0],
                'generatedtext': i[1],
                'player': i[2],
                'match': i[3],
                'data': i[4],
                'leagua': i[5],
                'type': i[6]
            }
        )
    c.close()
    return jsonify(d)


if __name__ == "__main__":
    app.run()