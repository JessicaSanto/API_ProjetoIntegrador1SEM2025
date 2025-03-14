from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Inicializando o aplicativo Flask
app = Flask('projeto')

# Configuração do banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Corrigido para False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:senai%40134@127.0.0.1:3306/projetoIntegrador'

# Inicializando o SQLAlchemy
mybd = SQLAlchemy(app)

# Modelo da tabela 'Valor'
class Emissao(mybd.Model):
    __tablename__ = 'emissaoco2'
    id = mybd.Column(mybd.Integer, primary_key=True)
    ano = mybd.Column(mybd.String(100))
    mes = mybd.Column(mybd.String(50))
    transporte = mybd.Column(mybd.String(100))
    energia = mybd.Column(mybd.String(50))
    residuos = mybd.Column(mybd.String(100))
    agropecuaria = mybd.Column(mybd.String(50))    
    processos_industriais = mybd.Column(mybd.String(100))  # Incluído no método to_json

    def to_json(self):
        return {"id": self.id, "ano": self.ano, "mes": self.mes, "transporte": self.transporte, "energia": self.energia, "residuos": self.residuos, "agropecuaria": self.agropecuaria, "processos_industriais": self.processos_industriais}

# Rota para obter todos os valores
@app.route("/dados", methods=["GET"])
def seleciona_valor():
    valor_objetos = Emissao.query.all()
    valor_json = [valor.to_json() for valor in valor_objetos]

    return jsonify({"status": 200, "valores": valor_json})

# Executando o aplicativo
if __name__ == "__main__":
    app.run(port=5000, host='127.0.0.1', debug=True)  # Alterado host para 127.0.0.1
