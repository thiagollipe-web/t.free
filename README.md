

---

## 📖 Sobre o projeto

O **T.Free** é um site de **arquivo único** (`index.html`) que reúne as melhores **inteligências artificiais gratuitas** disponíveis globalmente — incluindo opções **sem censura** e **offline**.

Nada de instaladores, nada de `npm install`, nada de backend. Basta abrir o arquivo no navegador e usar. 🚀

---

## ✨ Funcionalidades

| Recurso | Descrição |
|---|---|
| 🔎 **Busca inteligente** | Filtre IAs por nome, função ou palavra-chave em tempo real |
| 🏷️ **Filtros por categoria** | Chat · Local/Offline · API/Dev · Imagem · Busca · Código |
| 🃏 **Cards de resultados** | Descrição, selos (`Grátis`, `Sem censura`, `Offline`) e link oficial |
| 🤖 **Chat bot integrado** | Responde perguntas como *"quais IA grátis?"* e *"IA sem censura"* — e filtra a página automaticamente |
| 🦙 **Integração com Ollama** | Conecte sua **chave de API do Ollama** para respostas via modelo local |
| 📱 **Mobile-first** | Layout responsivo com grid adaptável (1 → 2 → 3 colunas) |
| 🎨 **Design autêntico** | Visual editorial vibrante — sem cara de "template de IA" |

---

## 🚀 Como usar

### Opção 1 — Direto no navegador (mais rápido)

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/t-free.git
   cd t-free
   ```
2. Abra o arquivo `index.html`:
   - **Duplo clique** no arquivo, ou
   - **Arraste** para a janela do navegador, ou
   - Clique com o botão direito → *Abrir com* → Chrome / Firefox / Edge / Safari

✅ Pronto! Nenhuma dependência externa é obrigatória.

### Opção 2 — Servidor local (opcional)

```bash
# Python 3
python -m http.server 8080

# Node.js
npx serve .
```

Depois acesse: **http://localhost:8080**

---

## 🦙 Conectando o Ollama (chave de API)

O bot responde automaticamente por palavras-chave, mas você pode turbiná-lo com seu **modelo local**:

1. **Instale o Ollama**: [ollama.com](https://ollama.com) e inicie com `ollama serve`
2. **Baixe um modelo**:
   ```bash
   ollama pull llama3.1
   # ou, para uso sem censura:
   ollama pull dolphin-mixtral
   ```
3. **No site**: abra o chat (💬) → clique em **⚙️**
4. **Preencha**:

   | Campo | Valor |
   |---|---|
   | API URL | `http://localhost:11434` |
   | Chave de API | *(cole sua chave aqui)* |
   | Modelo | `llama3.1`, `mistral`, `dolphin-mixtral`… |

5. Quando aparecer **"Modo Ollama ATIVO"** ✅, o bot passa a responder com o seu modelo.
   Se a conexão falhar, ele volta automaticamente ao modo de palavras-chave.

> 💡 **Dica CORS**: se o navegador bloquear a requisição, inicie o Ollama com `OLLAMA_ORIGINS=*`.

---

## 📁 Estrutura do projeto

```
t-free/
├── index.html    → Site completo (HTML + CSS + JS embutidos)
└── README.md     → Esta documentação
```

---

## 🎨 Customização

Tudo fica dentro do `index.html`:

- **➕ Adicionar serviços** — edite o array `SERVICES` no `<script>`:
  ```js
  { name:"Minha IA", icon:"🤖", color:"#ffd9a0", cat:"Chat",
    url:"https://exemplo.com", desc:"Descrição da IA…",
    tags:["chat","gratis"], uncensored:true, local:false }
  ```
- **🎨 Cores** — altere as variáveis em `:root` (`--coral`, `--sun`, `--mint`, `--sky`…)
- **🏷️ Categorias** — edite o array `CATEGORIES`
- **💬 Respostas rápidas do bot** — edite o array `QUICK`

---

## 🗺️ Roadmap

- [ ] Modo escuro 🌙
- [ ] Favoritos salvos no `localStorage` ⭐
- [ ] Mais categorias (vídeo, voz, música) 🎬
- [ ] Sugestão de serviços pela comunidade via PR 🤝

---

## 🤝 Contribuindo

Contribuições são bem-vindas!

1. Faça um **fork** do projeto
2. Crie uma branch: `git checkout -b feat/minha-ia`
3. Adicione o serviço ao array `SERVICES` (ou faça sua melhoria)
4. Commit: `git commit -m "feat: adiciona Minha IA ao catálogo"`
5. Push: `git push origin feat/minha-ia`
6. Abra um **Pull Request** 🎉

---

## 📜 Licença

Distribuído sob a licença **MIT** — use, modifique e compartilhe à vontade.

---

<div align="center">

**Feito com ❤️ e muito ☕ pela comunidade T.Free**

⚡ *IA livre é IA grátis.* ⚡

</div>
```
