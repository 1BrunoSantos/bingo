Aqui está um exemplo de README para o seu aplicativo de bingo automático:

---

# Bingo Automático

Um aplicativo simples e interativo de bingo, construído com Python e a biblioteca `customtkinter`. Este aplicativo permite que você sorteie números de um bingo e exiba animações e frases motivacionais associadas aos números sorteados.

## Funcionalidades

- **Escolha de Faixa de Números:** Selecione se o bingo deve conter até 75 ou 90 números.
- **Sorteio de Números:** Sorteie números aleatórios da faixa selecionada, com animações e frases associadas.
- **Histórico de Sorteios:** Mantenha um histórico dos números já sorteados.
- **Interface Gráfica:** Layout intuitivo com botões grandes e fontes legíveis.

## Requisitos

- Python 3.x
- customtkinter

Você pode instalar a biblioteca `customtkinter` usando o seguinte comando:

```bash
pip install customtkinter
```

## Estrutura do Projeto

O projeto contém o seguinte script principal:

### `bingo_automatico.py`

- **Função `animacao_sorteio(numero)`**: Exibe uma animação de números aleatórios antes de mostrar o número final sorteado.
- **Função `sortear_numero()`**: Sorteia um número da faixa selecionada e atualiza a frase e o histórico.
- **Função `atualizar_historico()`**: Atualiza a lista de números sorteados no histórico.
- **Função `escolher_max_numero(n)`**: Define a faixa máxima de números e desativa os botões de seleção após a escolha.
- **Configuração da Interface**: Cria a janela principal, rótulos, caixa de texto rolável e botões.

## Uso

1. **Inicie o aplicativo**:
   Execute o script `bingo_automatico.py` para abrir a interface gráfica.

2. **Escolha a Faixa de Números**:
   Clique em "Até 75" ou "Até 90" para definir a quantidade máxima de números.

3. **Sorteie um Número**:
   Clique em "Sortear" para sortear um número e ver a animação e a frase associada.

4. **Visualize o Histórico**:
   O histórico dos números sorteados será exibido na área à direita da interface.

## Contribuição

Se você deseja contribuir com melhorias ou correções, fique à vontade.
