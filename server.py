from flask import Flask, request, jsonify, send_from_directory
import threading
import time
from datetime import datetime
import csv
import speedtest

app = Flask(__name__)

ARQUIVO_SAIDA = "dados_velocidade.csv"
medicao_ativa = False
intervalo_segundos = 300
contratado_download = 100
contratado_upload = 50

@app.route('/configurar', methods=['POST'])
def configurar():
    global contratado_download, contratado_upload, intervalo_segundos
    dados = request.json
    contratado_download = dados.get('contratado_download', contratado_download)
    contratado_upload = dados.get('contratado_upload', contratado_upload)
    intervalo = dados.get('intervalo', 5)
    unidade = dados.get('unidade', 'minutos')
    intervalo_segundos = intervalo * (60 if unidade == 'minutos' else 3600)
    return jsonify({"status": "configurado"})

@app.route('/iniciar', methods=['POST'])
def iniciar():
    global medicao_ativa
    medicao_ativa = True
    threading.Thread(target=monitorar_internet).start()
    return jsonify({"status": "medição iniciada"})

@app.route('/pausar', methods=['POST'])
def pausar():
    global medicao_ativa
    medicao_ativa = False
    return jsonify({"status": "medição pausada"})

@app.route('/sair', methods=['POST'])
def sair():
    global medicao_ativa
    medicao_ativa = False
    return jsonify({"status": "medição pausada ao sair da página"})

@app.route('/dados', methods=['GET'])
def obter_dados():
    with open(ARQUIVO_SAIDA, 'r') as arquivo:
        linhas = arquivo.readlines()
    return jsonify({"dados": linhas})

@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@app.route('/download_csv', methods=['GET'])
def download_csv():
    return send_from_directory('.', ARQUIVO_SAIDA, as_attachment=True)

@app.route('/apagar_historico', methods=['POST'])
def apagar_historico():
    global ARQUIVO_SAIDA
    with open(ARQUIVO_SAIDA, 'w') as arquivo:
        arquivo.write('')
    return jsonify({"status": "histórico apagado"})

def medir_velocidade():
    st = speedtest.Speedtest()
    st.get_servers()
    servidor = st.get_best_server()

    download = round(st.download() / 1_000_000, 2)
    upload = round(st.upload() / 1_000_000, 2)
    ping = round(servidor['latency'], 2)

    servidor_nome = servidor['sponsor']
    servidor_local = servidor['name']
    servidor_dist = round(servidor['d'], 2)

    return download, upload, ping, servidor_nome, servidor_local, servidor_dist

def salvar_dados(timestamp, download, upload, ping, nome, local, dist):
    nome = nome or 'N/A'
    local = local or 'N/A'
    dist = dist or 'N/A'
    with open(ARQUIVO_SAIDA, mode='a', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([timestamp, download, upload, ping, nome, local, dist, contratado_download, contratado_upload])

def monitorar_internet():
    global medicao_ativa
    while medicao_ativa:
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            if not medicao_ativa:
                break
            download, upload, ping, nome, local, dist = medir_velocidade()
            salvar_dados(agora, download, upload, ping, nome, local, dist)
        except Exception as e:
            print(f"Erro ao medir: {e}")
        time.sleep(intervalo_segundos)

if __name__ == '__main__':
    app.run(debug=True)
