from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Fase 05 - Grupo 3 (Antonio Calazans, Chrystiano Bezerra, José Mario Mester e Leandro Nunes) - 7ASO - FIAP 2021/2022"

if __name__ == '__main__':
    app.run()