import mysql.connector
import app
import config


def inserir_imobiliaria(nome, endereco):
    (cursor, db) = None, None
    try:
        db = mysql.connector.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.database
        )
        cursor = db.cursor()
        sql = "INSERT INTO imobiliarias (nome, endereco) VALUES (%s, %s)"
        valores = (nome, endereco)
        cursor.execute(sql, valores)
        db.commit()
    except Exception:
        app.retornar_erro(0, 'Ocorreu um erro no banco de dados.')
    finally:
        cursor.close()
        db.close()


def inserir_imovel(nome, endereco, descricao, status, tipo, imobiliaria_id, caracteristicas, finalidade):
    (cursor, db) = None, None
    try:
        db = mysql.connector.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.database
        )
        cursor = db.cursor()
        sql = "INSERT INTO imoveis (nome, endereco, descricao, status, caracteristicas, tipo, finalidade, imobiliaria_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (nome, endereco, descricao, status, caracteristicas, tipo, finalidade, imobiliaria_id)
        cursor.execute(sql, valores)
        db.commit()
    except Exception:
        app.retornar_erro(0, 'Ocorreu um erro no banco de dados.')
    finally:
        cursor.close()
        db.close()


def alterar_imovel(imovel_id, nome, endereco, descricao, status, tipo, imobiliaria_id, caracteristicas, finalidade):
    (cursor, db) = None, None
    try:
        db = mysql.connector.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.database
        )
        cursor = db.cursor()
        sql = "UPDATE imoveis SET nome = %s, endereco = %s, descricao = %s, status = %s, caracteristicas = %s, tipo = %s, finalidade = %s, imobiliaria_id = %s WHERE imovel_id = %s"
        valores = (nome, endereco, descricao, status, caracteristicas, tipo, finalidade, imobiliaria_id, imovel_id,)
        cursor.execute(sql, valores)
        db.commit()
    except Exception:
        app.retornar_erro(0, 'Ocorreu um erro no banco de dados.')
    finally:
        cursor.close()
        db.close()


def deletar_imobiliaria(imobiliaria_id):
    (cursor, db) = None, None
    try:
        db = mysql.connector.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.database
        )
        cursor = db.cursor()
        sql = "DELETE FROM imobiliarias WHERE imobiliaria_id = %s"
        valor = (imobiliaria_id,)
        cursor.execute(sql, valor)
        db.commit()
    except Exception:
        app.retornar_erro(0, 'Ocorreu um erro no banco de dados.')
    finally:
        cursor.close()
        db.close()


def deletar_imovel(imovel_id):
    (cursor, db) = None, None
    try:
        db = mysql.connector.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.database
        )
        cursor = db.cursor()
        sql = "DELETE FROM imoveis WHERE imovel_id = %s"
        valor = (imovel_id,)
        cursor.execute(sql, valor)
        db.commit()
    except Exception:
        app.retornar_erro(0, 'Ocorreu um erro no banco de dados.')
    finally:
        cursor.close()
        db.close()


def listar_imobiliarias(nome, pagina, itens):
    (cursor, db) = None, None
    try:
        db = mysql.connector.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.database
        )
        cursor = db.cursor()
        if nome is not None:
            if pagina is not None and itens is not None:
                offset = (int(pagina) - 1) * int(itens)
                sql = "SELECT * FROM imobiliarias where nome like %s LIMIT %s, %s"
                valor = ('%' + nome + '%', offset, int(itens))
            else:
                sql = "SELECT * FROM imobiliarias where nome like %s"
                valor = ('%'+nome+'%',)
            cursor.execute(sql, valor)
        else:
            if pagina is not None and itens is not None:
                offset = (int(pagina) - 1) * int(itens)
                sql = "SELECT * FROM imobiliarias LIMIT %s, %s"
                valor = (offset, int(itens))
                cursor.execute(sql, valor)
            else:
                sql = "SELECT * FROM imobiliarias"
                cursor.execute(sql)
        results = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
        return results
    except Exception:
        app.retornar_erro(0, 'Ocorreu um erro no banco de dados.')
    finally:
        cursor.close()
        db.close()


def listar_imoveis(nome, pagina, itens):
    (cursor, db) = None, None
    try:
        db = mysql.connector.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.database
        )
        cursor = db.cursor()
        if nome is not None:
            if pagina is not None and itens is not None:
                offset = (int(pagina) - 1) * int(itens)
                sql = "SELECT * FROM imoveis where nome like %s LIMIT %s, %s"
                valor = ('%' + nome + '%', offset, int(itens))
            else:
                sql = "SELECT * FROM imoveis where nome like %s"
                valor = ('%'+nome+'%',)
            cursor.execute(sql, valor)
        else:
            if pagina is not None and itens is not None:
                offset = (int(pagina) - 1) * int(itens)
                sql = "SELECT * FROM imoveis LIMIT %s, %s"
                valor = (offset, int(itens))
                cursor.execute(sql, valor)
            else:
                sql = "SELECT * FROM imoveis"
                cursor.execute(sql)
        results = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
        return results
    except Exception:
        app.retornar_erro(0, 'Ocorreu um erro no banco de dados.')
    finally:
        cursor.close()
        db.close()