# Classifica o perfil de github das pessoas estudantes de acordo com alguns critérios

Essa aplicação pode ser encontrada no seguinte endereço: [Avaliador Git](https://avaliadorgit.com)

## Pré-Requisitos

Para rodar localmente esse projeto em sua máquina será necessário ter uma instalação do Python 3 compatível com o projeto e, além disso, fazer algumas configurações antes mesmo de conseguir executá-lo localmente. (Como nem todas as versões foram testadas, podem haver problemas de compatibilidade.)


## Execução da aplicação localmente
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

4. Certifique-se de criar as migrações (Caso seja necessário)

```bash
python3 manage.py makemigrations
```

5. Realize as migrações 

```bash
python3 manage.py migrate
```

6. Execute localmente em sua máquina a aplicação Django
```bash
python3 manage.py runserver
```

7. Acesse a aplicação na porta 8000 do seu localhost, basta ir no navegador e digitar:
```bash
127.0.0.1:8000
```


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
