# Contribuindo para o Monitor de Internet

Obrigado por considerar contribuir para este projeto! Aqui estão algumas diretrizes para ajudar você a começar.

## Como contribuir

1. **Fork este repositório** e clone o fork para sua máquina local.
2. Crie uma nova branch para sua contribuição:
   ```bash
   git checkout -b minha-contribuicao
   ```
3. Faça suas alterações e adicione testes, se necessário.
4. Commit suas alterações:
   ```bash
   git commit -m "Descrição clara da alteração"
   ```
5. Envie suas alterações para o GitHub:
   ```bash
   git push origin minha-contribuicao
   ```
6. Abra um Pull Request explicando suas alterações.

## Requisitos de código

- Certifique-se de que seu código está limpo e legível.
- Evite comentários excessivos.
- Siga o estilo de código existente.

## Testando suas alterações

### Backend

- Certifique-se de que o servidor Flask está funcionando corretamente:
  ```bash
  python server.py
  ```
- Teste os endpoints usando ferramentas como Postman ou cURL.

### Frontend

- Abra o arquivo `frontend/index.html` em um navegador.
- Verifique se as funcionalidades, como exportação de gráficos e download de CSV, estão funcionando corretamente.

## Reportando problemas

Se você encontrar um problema, abra uma issue descrevendo o problema e, se possível, como reproduzi-lo.

## Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a licença MIT deste projeto.
