from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aluno.Ram'

Ram = SQLAlchemy(app)


class Aluno(Ram.Model):
    id = Ram.Column(Ram.Integer(), primary_key=True, autoincrement=True)
    Materia = Ram.Column(Ram.String(255), nullable=False, index=True, unique=False)
    Matricula = Ram.Column(Ram.String(255))


    def __init__(self, Materia, Matricula):
        self.Materia = Materia
        self.Matricula = Matricula


    def __repr__(self):
        return '<Materia %r>' % self.Materia


Ram.create_all()


@app.route('/')
def home():
    result = "<h1>Tabelas</h1><br><ul>"
    for table in Ram.metadata.tables.items():
        result += "<li>%s</li>" % str(table)
    result += "</ul>"
    return result


@app.route('/add')
def add_aluno():
    test = Aluno(Materia='matematica', Matricula='20172011090212')
    Ram.session.add(test)
    Ram.session.commit()
    result = "Aluno Adicionado"
    return result


@app.route('/del/<int:id>')
def del_aluno(id):
    aluno = Aluno.query.get(id)
    Ram.session.delete(aluno)
    Ram.session.commit()
    return "Aluno Removido"


@app.route('/list')
def list():
    aluno = Aluno.query.order_by(Aluno.id).all()
    lista = "<h1>Lista de Alunos</h1><br><ul>"
    for aluno in aluno:
        lista += '<p>'
        lista += 'Id = '  + str(aluno.id)
        lista += ' Materia = ' + aluno.Materia
        lista += ' Matricula = ' + aluno.Matricula
        lista += '</p>'
    return lista


@app.route('/find/<int:id>')
def find(id):
    aluno = Aluno.query.get(id)
    result = "<h1>Aluno Encontrado</h1><br><ul>"
    result += "<p> Id=" + str(aluno.id) + "</p>"
    result += "<p> materia=" + aluno.Materia + "</p>"
    result += "<p> Matricula=" + aluno.matricula + "</p>"
    return result


@app.route('/change/<int:id>')
def change(id):
    aluno = Aluno.query.get(id)
    aluno.matricula = '100000'
    Ram.session.commit()
    return 'Aluno mudado'


if __name__ == '__main__':
    app.run()