# API's REST DDM

Atividade avaliatíva para a matéria de Desenvolvimento de Aplicações para WEB mestrada pelo Prof. [Cezar Mezzalira](https://github.com/cezarmezzalira)

## Integrantes da equipe

- [Samuel Rodrigues](https://github.com/Sammus-s)
- [Vinicius Lourenzoni](https://github.com/viniciusLourenzoni)
- [João Goroncy](https://github.com/Goroncy)
- [Daniel Brisch Cibolli](https://github.com/DanielBrisch)

---
### 1 - API de Controle de pátio aeroportuário

O Aeroporto de Pato Branco recebe aeronaves  diariamente e atualmente faz o controle de pátio via formulário de papel. Para melhorar o processo, foi solicitada a criação de um sistema com uma API REST que deve ter um CRUD (Create, Retrieve, Update e Delete) do registro da aeronave ao chegar no pátio, atualizando a data e horário de saída da aeronave do pátio, a listagem de aeronaves no pátio no momento da busca e também a possibilidade de excluir um registro com problema. Os dados devem ser gravados em memória e vão existir enquanto a aplicação existir.

---
##### Sumário
| Função | Método | Endereço |
|--------|--------|----------|
| [Novo Registro](#novo-registro) | POST   | /aeronaves |
| [Listar](#listar) | GET   | /aeronaves/listar |
| [Atualizar](#atualizar) | PATCH   | /aeronaves/{nome}/partida|
| [Deletar](#deletar) | DELETE   | /aeronaves/{nome}/deletar |

---
#### Novo Registro

Desc: Inclui novo registro de chegada de aeronave no pátio

**POST** (/aeronaves/...)
```json
BODY
{
  "nome": "string",
  "data_entrada": "datetime" //opcional
}
```

##### Respostas
| código | Descrição |
|--------|--------|
| 200 | OK |
| 400 | Aeronave já registrada |
| 422 | Validation Error |
---

#### Listar

Desc: Lista aeronaves presentes no pátio

**GET** (/aeronaves/listar)
```json
BODY
{    }
```
---

#### Atualizar

Desc: Registra a partida das aeronaves do pátio

**PATCH** (/aeronaves/{nome}/partida)

##### Respostas
| código | Descrição |
|--------|--------|
| 200 | OK |
| 404 | Aeronave não encontrada |
| 422 | Validation Error |

---
#### Deletar

Desc: 

**DELETE** (/aeronaves/{nome}/deletar)
```json
BODY
{    }
```