#  Projeto Calculadora: Integração Shell Script & Python

Este repositório contém a segunda etapa do projeto prático de automação em ambiente Linux. O objetivo é integrar um script de inicialização em Shell (`.sh`) com a lógica de processamento desenvolvida em Python (`.py`).


##  Estrutura do Repositório

* `calculadora.sh`: Script executável responsável por preparar o ambiente e chamar o interpretador Python.
* `calculadora.py`: Arquivo contendo a lógica matemática e o tratamento de dados.
* `README.md`: Documentação completa do projeto.

---

##  Como executar o arquivo .sh

Para garantir que o script funcione corretamente no seu terminal Linux, siga os passos abaixo de configuração de permissões e execução:

1.  **Definir Permissões:**
    Conforme os requisitos de segurança do módulo (Proprietário com permissão de escrita/execução e outros apenas com leitura), utilize o comando:
    ```bash
    chmod 744 calculadora.sh
    ```

2.  **Verificar Permissões:**
    Você pode confirmar se as permissões foram aplicadas corretamente com o comando:
    ```bash
    ls -l calculadora.sh
    ```
    *(A saída deve iniciar com `-rwxr--r--`)*

3.  **Executar o Script:**
    Para iniciar a calculadora, basta rodar o comando:
    ```bash
    ./calculadora.sh
    ```

---

##  Explicação do Código Python

O arquivo `calculadora.py` foi desenvolvido para ser uma ferramenta  de cálculos básicos. Abaixo estão os pontos principais da sua implementação:

* **Entrada Dinâmica:** O código utiliza a função `input()` para capturar dados do usuário em tempo real.
* **Conversão de Tipos:** Os dados inseridos são convertidos para `float`, permitindo operações com números decimais.
* **Estrutura Decisória:** Utiliza blocos `if`, `elif` e `else` para identificar qual operação matemática (+, -, *, /) o usuário deseja realizar.
* **Tratamento de Erros (Divisão por Zero):** O código inclui uma verificação de segurança: caso o usuário tente dividir um número por 0, o programa exibe uma mensagem de erro amigável em vez de interromper o sistema abruptamente.
* **Bloco Try-Except:** Garante que, caso o usuário digite letras ou símbolos onde deveriam estar números, o programa informe o erro de entrada sem "quebrar".

---

## 👤 Autor

**Iago Rosado**  

ATIVIDADE EBAC
