from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Fase 05 - Grupo 3 (Antonio Calazans, Chrystiano Bezerra, José Mario Mestre e Leandro Nunes) - 7ASO - FIAP 2021/2022."

if __name__ == '__main__':
    app.run()