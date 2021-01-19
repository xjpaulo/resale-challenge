# !/usr/bin/env python3
# -*- coding: utf-8 -*

import db
from flask import Flask, request, abort, jsonify, make_response
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route("/")
def mensagem_padrao():
    return jsonify({"mensagem": "Utilize um dos endpoints para o funcionamento correto da aplicação."})


@app.route('/imobiliarias/', methods=['GET'])
def listar_imobiliarias():
    if request.method == 'GET':
        nome = request.args.get('nome', None)
        pagina = request.args.get('pagina', None)
        itens = request.args.get('itens', None)
        validar(nome)
        validar_num(pagina, itens)
        resultado = db.listar_imobiliarias(nome, pagina, itens)
        if not resultado:
            resultado = {'mensagem': 'Não há imobiliárias para exibir.'}
        response = jsonify(resultado)
        response.status_code = 200
        return response


@app.route('/imobiliarias/imoveis/', methods=['GET'])
def listar_imoveis():
    if request.method == 'GET':
        nome = request.args.get('nome', None)
        pagina = request.args.get('pagina', None)
        itens = request.args.get('itens', None)
        validar(nome)
        validar_num(pagina, itens)
        resultado = db.listar_imoveis(nome, pagina, itens)
        if not resultado:
            resultado = {'mensagem': 'Não há imóveis para exibir.'}
        response = jsonify(resultado)
        response.status_code = 200
        return response
        

@app.route('/imobiliarias/<int:imobiliaria_id>/imoveis/', methods=['GET'])
def listar_imoveis_imobiliaria(imobiliaria_id):
    if request.method == 'GET':
        nome = request.args.get('nome', None)
        pagina = request.args.get('pagina', None)
        itens = request.args.get('itens', None)
        validar(nome)
        validar_num(pagina, itens)
        resultado = db.listar_imoveis_imobiliaria(nome, pagina, itens, imobiliaria_id)
        if not resultado:
            resultado = {'mensagem': 'Não há imóveis para exibir.'}
        response = jsonify(resultado)
        response.status_code = 200
        return response


@app.route('/imobiliarias/<int:imobiliaria_id>/imoveis/<int:imovel_id>/', methods=['GET'])
def listar_imovel_imobiliaria(imobiliaria_id, imovel_id):
    if request.method == 'GET':
        resultado = db.listar_imovel_imobiliaria(imobiliaria_id, imovel_id)
        if not resultado:
            resultado = {'mensagem': 'Não há imóvel para exibir.'}
        response = jsonify(resultado)
        response.status_code = 200
        return response


@app.route('/imobiliarias/<int:imobiliaria_id>/', methods=['GET'])
def listar_imobiliaria(imobiliaria_id):
    if request.method == 'GET':
        resultado = db.listar_imobiliaria(imobiliaria_id)
        if not resultado:
            resultado = {'mensagem': 'Não há imobiliária para exibir.'}
        response = jsonify(resultado)
        response.status_code = 200
        return response


@app.route('/imobiliarias/', methods=['POST'])
def adicionar_imobiliaria():
    if request.method == 'POST':
        nome = request.args['nome']
        endereco = request.args.get('endereco', None)
        validar(nome)
        db.inserir_imobiliaria(nome, endereco)
        response = jsonify({'mensagem': 'Imobiliária {} adicionada com sucesso!'.format(nome)})
        response.status_code = 201
        return response


@app.route('/imobiliarias/', methods=['PUT'])
def alterar_imobiliaria():
    if request.method == 'PUT':
        imobiliaria_id = request.args['imobiliaria_id']
        nome = request.args['nome']
        endereco = request.args.get('endereco', None)
        validar_num(imobiliaria_id)
        validar(nome)
        db.inserir_imobiliaria(nome, endereco)
        response = jsonify({'mensagem': 'Imobiliária ID {} alterada com sucesso!'.format(imobiliaria_id)})
        response.status_code = 200
        return response


@app.route('/imobiliarias/', methods=['DELETE'])
def apagar_imobiliaria():
    if request.method == 'DELETE':
        imobiliaria_id = request.args['imobiliaria_id']
        validar_num(imobiliaria_id)
        db.deletar_imobiliaria(imobiliaria_id)
        response = jsonify({'mensagem': 'Imobiliária ID {} removida com sucesso!'.format(imobiliaria_id)})
        response.status_code = 200
        return response


@app.route('/imobiliarias/imoveis/', methods=['POST'])
def adicionar_imovel():
    if request.method == 'POST':
        nome = request.args['nome']
        endereco = request.args['endereco']
        descricao = request.args['descricao']
        imobiliaria_id = request.args['imobiliaria_id']
        caracteristicas = request.args.get('caracteristicas', None)
        finalidade = request.args.get('finalidade', None)
        status = request.args['status']
        tipo = request.args['tipo']
        validar(nome, status, tipo, finalidade)
        validar_num(imobiliaria_id)
        if status not in {'Ativo', 'Inativo'}:
            retornar_erro('400', 'Campo inválido! O atributo status tem que ser Ativo ou Inativo.')
        if tipo not in {'Apartamento', 'Casa'}:
            retornar_erro('400', 'Campo inválido! O atributo tipo tem que ser Apartamento ou Casa.')
        if finalidade is not None and finalidade not in {'Residencial', 'Escritorio'}:
            retornar_erro('400', 'Campo inválido! O atributo finalidade tem que ser Residencial ou Escritorio')
        db.inserir_imovel(nome, endereco, descricao, status, tipo, imobiliaria_id, caracteristicas, finalidade)
        response = jsonify({'mensagem': 'Imóvel {} adicionado com sucesso!'.format(nome)})
        response.status_code = 201
        return response


@app.route('/imobiliarias/imoveis/', methods=['PUT'])
def alterar_imovel():
    if request.method == 'PUT':
        nome = request.args['nome']
        endereco = request.args['endereco']
        descricao = request.args['descricao']
        imovel_id = request.args['imovel_id']
        imobiliaria_id = request.args['imobiliaria_id']
        caracteristicas = request.args.get('caracteristicas', None)
        finalidade = request.args.get('finalidade', None)
        status = request.args['status']
        tipo = request.args['tipo']
        validar(nome, endereco, status, tipo, finalidade)
        validar_num(imobiliaria_id, imovel_id)
        if status not in {'Ativo', 'Inativo'}:
            retornar_erro('400', 'Campo inválido! O atributo status tem que ser Ativo ou Inativo.')
        if tipo not in {'Apartamento', 'Casa'}:
            retornar_erro('400', 'Campo inválido! O atributo tipo tem que ser Apartamento ou Casa.')
        if finalidade is not None and finalidade not in {'Residencial', 'Escritorio'}:
            retornar_erro('400', 'Campo inválido! O atributo finalidade tem que ser Residencial ou Escritorio')
        db.alterar_imovel(imovel_id, nome, endereco, descricao, status, tipo, imobiliaria_id, caracteristicas, finalidade)
        response = jsonify({'mensagem': 'Imóvel ID {} alterado com sucesso!'.format(imovel_id)})
        response.status_code = 200
        return response


@app.route('/imobiliarias/imoveis/', methods=['DELETE'])
def apagar_imovel():
    if request.method == 'DELETE':
        imovel_id = request.args['imovel_id']
        validar_num(imovel_id)
        db.deletar_imovel(imovel_id)
        response = jsonify({'mensagem': 'Imóvel id {} removido com sucesso!'.format(imovel_id)})
        response.status_code = 200
        return response


def retornar_erro(status, mensagem):
    if status != 0:
        abort(make_response(jsonify(status=status, erro_msg=mensagem), status))
    else:
        abort(make_response(jsonify(erro_msg=mensagem), 400))


def validar(*campos):
    for x in campos:
        if x is None:
            continue
        if not all(caracter.isalnum() or caracter.isspace() for caracter in x):
            retornar_erro('400', 'Campo com caracteres inválidos! Utilize apenas caracteres alfanuméricos e espaços.')


def validar_num(*campos):
    for x in campos:
        if x is None:
            continue
        if not all(caracter.isnumeric() for caracter in x):
            retornar_erro('400', 'Campo com caracteres inválidos! Utilize apenas números para o valor ' + x)


@app.errorhandler(404)
def erro_404(error=None):
    message = {
        'status': 404,
        'mensagem': 'URL não encontrada: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response


@app.errorhandler(400)
def erro_400(error=None):
    message = {
        'status': 400,
        'mensagem': 'Request inválido. Verifique os valores dos atributos enviados.',
    }
    response = jsonify(message)
    response.status_code = 400
    return response


@app.errorhandler(405)
def erro_405(error=None):
    message = {
        'status': 405,
        'mensagem': 'Método não permitido para URL: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 405
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')

