# Monitor de Internet

Este projeto tem como objetivo monitorar a estabilidade e entrega da internet, registrando métricas como velocidade de download, upload, ping, e discrepâncias entre aferições.

## Funcionalidades

- Coleta automática de métricas de internet.
- Registro das métricas em um arquivo CSV.
- Exibição das métricas em um frontend interativo.
- Exportação de gráficos em JPG.
- Download do histórico detalhado em CSV.
- Opção para apagar o histórico completo.

Gráfico de acompanhamento das medições:
<img width="1818" height="925" alt="image" src="https://github.com/user-attachments/assets/64d33023-9da3-4241-953a-2cf67f942174" />

Medições detalhadas:
<img width="1887" height="678" alt="image" src="https://github.com/user-attachments/assets/c0625528-70fa-47fb-8084-ea47eef0f218" />


## Como usar

1. Clone este repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o servidor Flask:
   ```bash
   python server.py
   ```

4. Abra o navegador e acesse:
   ```
   http://127.0.0.1:5000/
   ```

## Dependências

- **Backend**:
  - Python 3.x
  - Flask
  - speedtest-cli

- **Frontend**:
  - Chart.js

## Contribuindo

Veja o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para saber como contribuir com este projeto.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
