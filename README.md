# Classifica o perfil de github das pessoas estudantes de acordo com alguns critérios

Essa aplicação pode ser encontrada no seguinte endereço: [Avaliador Git](https://avaliadorgit.com)

## Pré-Requisitos

Para rodar localmente esse projeto em sua máquina será necessário ter uma instalação do `Python 3` compatível com o projeto e, além disso, fazer algumas configurações antes mesmo de conseguir executá-lo localmente. (Como nem todas as versões foram testadas, podem haver problemas de compatibilidade.)


## Execução da aplicação localmente


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

4. Certifique-se de criar arquivo com as variáveis de ambiente (`.env`) dentro da pasta config, um arquivo exemplo, com as variáveis necessárias para execução, se encontra dentro desta mesma pasta

5. Certifique-se de criar as migrações (Caso seja necessário)

```bash
python3 manage.py makemigrations
```

6. Realize as migrações 

```bash
python3 manage.py migrate
```

7. Execute localmente em sua máquina a aplicação Django
```bash
python3 manage.py runserver
```

8. Acesse a aplicação na porta 8000 do seu localhost, basta ir no navegador e digitar:
```bash
127.0.0.1:8000
```

## Para devs:

### Rotas:

#### Route param:
```bash
https://avaliadorgit.com/grade/
```
- Retorna um `json` com o atributo `median_grade` que representa a **mediana** das notas avaliadas pela ferramenta.

#### Query param:
```bash
https://avaliadorgit.com/?refresh=true/
```
- Irá recalcular a mediana das notas avaliadas pela ferramenta.

```bash
https://avaliadorgit.com/?github_user=<username>
```
- Retornará um `json` com o atributo `grade` que representa a nota mais recente do `github_user` (3 dias), caso não encontre irá refazer a avaliação.

```bash
https://avaliadorgit.com/?github_user=<username>?refresh=true
```
- Irá forçar o avaliador a refazer a avaliçaõ do `github_user` passado e retornará um `json` com o atributo `grade` que representa a nota do `github_user`.

> 💡Dica: utilize essa rota enquanto você está adaptando o seu perfil e quer uma resposta imediata.
  
## Critérios de Avaliação (Nota máxima = 100)

- É identificado um rosto na foto da pessoa (+10)
- É encontrado um email no readme de perfil do GitHub (+10)
- É encontrado o linkedin na página da pessoa do Github (+10)
- Possui readme de perfil (+10)
- Possui pelo menos 5 tecnologias/frameworks que domina no perfil (+10)
- Possui pelo menos 10 tecnologias/frameworks que domina no perfil (+10)
- Possui pelo menos 5 repositórios no GitHub (+10)
- Possui pelo menos 10 repositórios no GitHub (+10)
- Possui pelo menos 2 repositórios pinados no GitHub (+10)
- Possui pelo menos 4 repositórios pinados no GitHub (+10)


## Sugestões de melhoria

Sinta-se à vontade para me contactar para que possamos melhorar ainda mais essa ferramenta.

> Começe criando um `fork` deste repositório, crie uma branch para sua feature e suba um pull request. 💚


![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)