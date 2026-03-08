from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

portfolio_data = {
    'name': 'Любовь Алексеева',
    'title': 'Начинающий специалист по тестированию',
    'location': 'Саратов',
    'bio': 'Привет! Меня зовут Любовь, я начинающий специалист по тестированию из Саратова. В своей работе я использую Python, MySQL, Flask и Telegram API. Увлекаюсь созданием проектов, которые помогают мне оттачивать навыки поиска несоответствий и улучшения качества продуктов.',
    'interests': ['Python', 'Тестирование', 'MySQL', 'VS Code'],
    'interests_description': 'Я использую AI как инструмент для ускорения обучения и решения задач. Важно не просто получить код, а понять его. Именно так я строю свою практику.',
    'projects': [
        {
            'title': 'Telegram Info Bot',
            'description': 'Бот-визитка с фото и кнопками на aiogram. Рассказывает о проектах и контактах.',
            'technologies': ['Python', 'aiogram', 'Telegram API'],
            'github': 'https://github.com/lexi1509/telegram-info-bot',
            'type': 'Telegram Bot',
            'status': 'Active'
        },
        {
            'title': 'My First Project',
            'description': 'Первый репозиторий на GitHub. Начало пути в Git и GitHub.',
            'technologies': ['Git', 'GitHub'],
            'github': 'https://github.com/lexi1509/my-first-project',
            'type': 'Learning Project',
            'status': 'Completed'
        }
    ],
    'social': {
        'github': 'https://github.com/lexi1509',
        'telegram': 'https://t.me/Alexi1509',
        'email': 'Volsar20141991@yandex.com'
    }
}

@app.route('/')
def index():
    return render_template('index.html', data=portfolio_data)

@app.route('/contact')
def contact():
    return render_template('contact.html', data=portfolio_data)

@app.route('/send_message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        flash('Спасибо за ваше сообщение! Я обязательно отвечу вам в ближайшее время.', 'success')
        return redirect(url_for('contact'))

@app.route('/project/<project_title>')
def project_detail(project_title):
    project = next((p for p in portfolio_data['projects'] if p['title'].lower().replace(' ', '') == project_title.lower()), None)
    if project:
        return render_template('project_detail.html', project=project, data=portfolio_data)
    else:
        flash('Project not found!', 'error')
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', data=portfolio_data), 404

if __name__ == '__main__':
    app.run(debug=True, port=5003, host='127.0.0.1')