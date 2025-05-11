# 🦑 Hollow Knight - API de Personagens Não Jogáveis

Uma API REST feita em Python que fornece informações sobre personagens não jogáveis (NPCs) do jogo **Hollow Knight**. Os personagens estão organizados por categoria, como Comerciantes, Guerreiros dos Sonhos, Andarilhos, entre outros.

## 🌐 Endpoints

Cada endpoint retorna uma lista de personagens com os seguintes campos:

- `nome`: Nome do personagem
- `genero`: Masculino, Feminino ou Indefinido
- `vivo`: true ou false
- `locais`: Lista dos locais onde o personagem aparece

### Categorias:

| Categoria              | Rota                      |
|------------------------|---------------------------|
| Comerciantes           | `/comerciantes`           |
| Guerreiros dos Sonhos  | `/guerreiros_dos_sonhos`   |
| Andarilhos             | `/andarilhos`             |
| Espíritos              | `/espiritos`              |
| Mestres do Ferrão      | `/mestres_do_ferrao`      |
| Variados               | `/variados`               |
| Missões                | `/missoes`                |

* Para buscar um personagem específico, coloque *classe*/<"int:id">
* A contagem do id começa do 1 e reinicia a cada classe

Exemplo de resposta:

```json
[
  {
    "id" : 1,
    "nome" : "Elder Hu",
    "genero" : "Feminino",
    "vivo" : false,
    "locais" : "Ermos Fúngicos"
  }
]
