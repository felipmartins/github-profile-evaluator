# Classifica o perfil de github das pessoas estudantes de acordo com alguns critérios

## Pré-Requisitos

1. Python 3 funcionando na máquina. (Como nem todas as versões foram testadas, podem haver problemas de compatibilidade.) 

2. Para se utilizar de acordo com o que foi pensado é necessário colocar o arquivo .csv que vai ser utilizado na pasta target_data, esse arquivo precisa ter as colunas (cohort_name, github_username, name) tais informações podem ser encontradas na question 5452.


## Execução da aplicação
---

1. Crie o ambiente virtual

```bash
python3 -m venv .venv
```

2. Ative o ambiente virtual

```bash
source .venv/bin/activate
```

3. Instale os requerimentos para a aplicação

```bash
pip install -r requirements.txt
```

4. Altere o arquivo main.py colocando o caminho para o csv que se encontra na pasta /target_data/

```bash
group_evaluation(get_usernames("coloque_aqui_o_caminho_relativo_para_o_csv"))
```

5. Execute o arquivo main.py 

```bash
python3 main.py
```

6. Se tudo ocorreu como esperado você deve encontrar um outro arquivo CSV com o nome da turma na pasta /results/ nele costam as notas do github para cada uma das pessoas estudantes


## Critérios de Avaliação (Nota máxima = 100)

- É identificado um rosto na foto da pessoa (+10)
- É encontrado um email no perfil do GitHub (+10)
- É encontrado o linkedin no perfil do Github (+10)
- Possui readme de perfil (+10)
- Possui pelo menos 5 tecnologias/frameworks que domina no perfil (+10)
- Possui pelo menos 10 tecnologias/frameworks que domina no perfil (+10)
- Possui pelo menos 5 repositórios no GitHub (+10)
- Possui pelo menos 10 repositórios no GitHub (+10)
- Possui pelo menos 2 repositórios pinados no GitHub (+10)
- Possui pelo menos 4 repositórios pinados no GitHub (+10)
