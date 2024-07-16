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
#Finding:     "export BUNDLE_ENTERPRISE__CONTRIBSYS__COM=cafebabe:deadbeef",
#Secret:      cafebabe:deadbeef
#RuleID:      sidekiq-secret
#Entropy:     2.609850
#File:        cmd/generate/config/rules/sidekiq.go
#Line:        23
#Commit:      cd5226711335c68be1e720b318b7bc3135a30eb2
#Author:      John
#Email:       john@users.noreply.github.com
#Date:        2022-08-03T12:31:40Z
#Fingerprint: cd5226711335c68be1e720b318b7bc3135a30eb2:cmd/generate/config/rules/sidekiq.go:sidekiq-secret:23


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)