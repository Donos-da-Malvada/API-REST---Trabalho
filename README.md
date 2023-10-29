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
| [Atualizar](#atualizar) | PATCH   | /endereço/:param/... |
| [Deletar](#deletar) | DELETE   | /endereço/:param/... |

---
#### Novo Registro

Desc: Inclui novo registro de chegada de aeronave no pátio

**POST** (/aeronaves/...)
```json
BODY
{
  "nome": "Nome"
}
```
---

#### Listar

Desc: Lista aeronaves presentes no pát

**GET** (/aeronaves/listar)
```json
BODY
{    }
```
---

#### Atualizar

Desc: 

**PATCH** (/endereço/:param/...)
```json
BODY
{  
    "parâmetro 1": "UPDATE",  
}
```
---
#### Deletar

Desc: 

**DELETE** (/endereço/:param/...)
```json
BODY
{    }
```