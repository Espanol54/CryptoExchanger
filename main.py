from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
from wtforms.validators import DataRequired, Regexp
from Parser import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
reg = r'^-?\d+(?:\.{0,1}\d*)$'
crypto = cryptoValue()
currency = currencyValue()


class CryptoForm(FlaskForm):
    cryptoSelect = SelectField('CryptoS', choices=crypto.keys())
    currencySelect = SelectField('CurrencyS', choices=currency.keys())
    cryptoNum = StringField('Crypto', validators=[DataRequired(), Regexp(reg, message='Incorrect value!')])
    currencyNum = StringField('Currency')
    button = SubmitField('Ok')


class CurrencyForm(FlaskForm):
    cryptoSelect = SelectField('CryptoS', choices=crypto.keys())
    currencySelect = SelectField('CurrencyS', choices=currency.keys())
    currencyNum = StringField('Currency', validators=[DataRequired(), Regexp(reg, message='Incorrect value!')])
    cryptoNum = StringField('Crypto')
    button = SubmitField('Ok')


@app.route('/', methods=['GET', 'POST'])
@app.route('/toCurrency', methods=['GET', 'POST'])
def toCurrency():
    form = CryptoForm()
    if form.validate_on_submit():
        count = form.cryptoNum.data
        result = float(count) * crypto.get(form.cryptoSelect.data) / \
            float(currency.get(form.currencySelect.data))
        form.currencyNum.data = float('{:.3f}'.format(result))
    return render_template('cryptoToCurrency.html', form=form)


@app.route('/toCrypto', methods=['GET', 'POST'])
def toCrypto():
    form = CurrencyForm()
    if form.validate_on_submit():
        count = form.currencyNum.data
        result = float(count) * currency.get(form.currencySelect.data) / \
            float(crypto.get(form.cryptoSelect.data))
        form.cryptoNum.data = float(result)
    return render_template('currencyToCrypto.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
