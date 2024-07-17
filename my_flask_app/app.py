from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/sum/<int:a>/<int:b>')
def sum(a, b):
    res = a+b
    return str(res)





@app.route('/min/<int:a>/<int:b>')
def min(a, b):
    res = a-b
    return str(res)


@app.route('/mult/<int:a>/<int:b>')
def mult(a, b):
    res = a*b
    return str(res)


@app.route('/dell/<int:a>/<int:b>')
def dell(a, b):
    if b == 0:
        return "Ошибка"

    res = a/b
    return str(res)


@app.route('/sqr/<int:a>')
def sqr(a):
    res = a**2
    return str(res)

@app.route('/sqr3/<int:a>')
def sqr3(a):
    res = a**3
    return str(res)


@app.route('/sqr4/<int:a>')
def sqr4(a):
    res = a**4
    return str(res)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)


#password = "sd-hsbWDfeWy-m1200"

#token = hvuxTUV87QT2O-WKX-W
''' SSH = git@github.com:dimafominykh/calculate.git 
API key: kcdnCDNcmJScnJSNCoibuyfthtwgeig13r1ukyfb
Apple ID: qvadrt@icloud.com
'''

