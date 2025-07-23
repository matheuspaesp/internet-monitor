install:
	pip install -r requirements.txt

docker-build:
	docker build -t internet-monitor .

docker-run:
	docker run -p 5000:5000 internet-monitor

run:
	python server.py

clean:
	rm -rf __pycache__ 
	rm -f dados_velocidade.csv

.PHONY: install docker-build docker-run run clean