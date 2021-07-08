from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

liver = {'ad':'https://nijisanji.ichikara.co.jp/member/Saku-Sasaki/',
             'ae':'https://nijisanji.ichikara.co.jp/member/Yuika-Shiina/',
             'bd':'https://nijisanji.ichikara.co.jp/member/Ritsuki-Sakura/',
             'be':'https://www.hololive.tv/portfolio/items/336351',
             'cd':'https://nijisanji.ichikara.co.jp/member/Rion-Takamiya/',
             'ce':'https://nijisanji.ichikara.co.jp/member/era-otogibara/'}

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def recieve_post():
    first = request.form['q1']
    second = request.form['q2']

    result_word = first + second
    result = liver[result_word]

    return redirect(result)

if __name__ == '__main__':
    app.run(debug=True)