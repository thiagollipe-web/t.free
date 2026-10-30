Aqui estão os dois arquivos completos do **T.Free**, prontos para copiar e colar:

---

### 📄 `index.html`

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>T.Free — IAs gratuitas do mundo todo</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fontsource/space-grotesk@5.0.18/index.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fontsource/inter@5.0.18/index.css">
<style>
  :root{
    --bg:#fff8f0;
    --ink:#171310;
    --ink-soft:#5c534a;
    --coral:#ff4d2e;
    --sun:#ffc93c;
    --mint:#00c48c;
    --sky:#2f6bff;
    --card:#ffffff;
    --line:#1713101a;
    --radius:18px;
    --shadow:4px 4px 0 #171310;
  }
  *{margin:0;padding:0;box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{
    font-family:'Inter',system-ui,sans-serif;
    background:var(--bg);
    color:var(--ink);
    line-height:1.55;
    min-height:100vh;
  }
  h1,h2,h3,.logo,.chip{font-family:'Space Grotesk',sans-serif}

  header{
    position:sticky;top:0;z-index:50;
    background:var(--bg);
    border-bottom:2px solid var(--ink);
  }
  .nav{
    max-width:1180px;margin:0 auto;padding:14px 20px;
    display:flex;align-items:center;gap:14px;flex-wrap:wrap;
  }
  .logo{
    font-weight:700;font-size:1.35rem;letter-spacing:-.02em;
    display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink);
  }
  .logo-dot{
    width:34px;height:34px;border-radius:10px;
    background:var(--coral);border:2px solid var(--ink);
    display:grid;place-items:center;color:#fff;font-size:1rem;
    box-shadow:2px 2px 0 var(--ink);
    transform:rotate(-4deg);
  }
  .logo .t-free{font-size:1.45rem}
  .logo .t-free span{color:var(--coral)}
  .nav-tag{
    margin-left:auto;font-size:.78rem;font-weight:600;
    background:var(--sun);border:2px solid var(--ink);
    padding:5px 12px;border-radius:999px;box-shadow:2px 2px 0 var(--ink);
  }

  .hero{
    max-width:1180px;margin:0 auto;padding:44px 20px 26px;
    display:flex;flex-direction:column;gap:18px;
  }
  .hero h1{
    font-size:clamp(1.9rem,5.5vw,3.2rem);
    font-weight:700;letter-spacing:-.03em;line-height:1.08;
    max-width:16ch;
  }
  .hero h1 em{
    font-style:normal;color:#fff;background:var(--coral);
    padding:0 .18em;border-radius:8px;transform:rotate(-1deg);display:inline-block;
    border:2px solid var(--ink);box-shadow:3px 3px 0 var(--ink);
  }
  .hero p{color:var(--ink-soft);max-width:56ch;font-size:1rem}

  .search-wrap{position:relative;max-width:640px;width:100%}
  .search-wrap svg{
    position:absolute;left:18px;top:50%;transform:translateY(-50%);
    width:20px;height:20px;stroke:var(--ink-soft);pointer-events:none;
  }
  #searchInput{
    width:100%;padding:17px 56px 17px 52px;
    font-size:1rem;font-family:inherit;
    border:2px solid var(--ink);border-radius:14px;
    background:var(--card);box-shadow:var(--shadow);
    outline:none;transition:transform .15s ease, box-shadow .15s ease;
  }
  #searchInput:focus{transform:translate(-2px,-2px);box-shadow:6px 6px 0 var(--ink)}
  #clearBtn{
    position:absolute;right:14px;top:50%;transform:translateY(-50%);
    border:none;background:var(--line);color:var(--ink);
    width:28px;height:28px;border-radius:50%;cursor:pointer;
    font-size:1rem;display:none;place-items:center;line-height:1;
  }
  #clearBtn.show{display:grid}

  .filters{
    max-width:1180px;margin:0 auto;padding:8px 20px 4px;
    display:flex;gap:10px;overflow-x:auto;scrollbar-width:none;
  }
  .filters::-webkit-scrollbar{display:none}
  .chip{
    flex:0 0 auto;font-size:.85rem;font-weight:600;
    padding:8px 16px;border-radius:999px;cursor:pointer;
    border:2px solid var(--ink);background:var(--card);
    transition:all .15s ease;user-select:none;
  }
  .chip:hover{background:var(--sun)}
  .chip.active{background:var(--ink);color:var(--bg)}

  .result-count{
    max-width:1180px;margin:0 auto;padding:14px 20px 0;
    font-size:.85rem;color:var(--ink-soft);font-weight:600;
  }

  main{max-width:1180px;margin:0 auto;padding:16px 20px 120px}
  .grid{
    display:grid;gap:18px;
    grid-template-columns:1fr;
  }
  @media(min-width:600px){.grid{grid-template-columns:repeat(2,1fr)}}
  @media(min-width:940px){.grid{grid-template-columns:repeat(3,1fr)}}

  .card{
    background:var(--card);border:2px solid var(--ink);border-radius:var(--radius);
    padding:20px;display:flex;flex-direction:column;gap:10px;
    box-shadow:var(--shadow);
    transition:transform .15s ease, box-shadow .15s ease;
    animation:pop .3s ease both;
  }
  @keyframes pop{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
  .card:hover{transform:translate(-2px,-2px);box-shadow:7px 7px 0 var(--ink)}
  .card-top{display:flex;align-items:flex-start;gap:12px}
  .card-icon{
    width:44px;height:44px;flex:0 0 44px;border-radius:12px;
    border:2px solid var(--ink);display:grid;place-items:center;
    font-size:1.25rem;font-weight:700;font-family:'Space Grotesk',sans-serif;
  }
  .card h3{font-size:1.08rem;font-weight:700;letter-spacing:-.01em}
  .card-cat{font-size:.72rem;font-weight:600;color:var(--ink-soft);text-transform:uppercase;letter-spacing:.06em}
  .card p{font-size:.9rem;color:var(--ink-soft);flex:1}
  .badges{display:flex;gap:6px;flex-wrap:wrap}
  .badge{
    font-size:.7rem;font-weight:700;padding:3px 10px;border-radius:999px;
    border:1.5px solid var(--ink);
  }
  .badge.free{background:var(--mint);color:#fff}
  .badge.uncensored{background:var(--coral);color:#fff}
  .badge.local{background:var(--sun)}
  .card-link{
    align-self:flex-start;margin-top:4px;
    font-size:.85rem;font-weight:700;text-decoration:none;color:var(--ink);
    border-bottom:2.5px solid var(--coral);padding-bottom:2px;
    transition:color .15s;
  }
  .card-link:hover{color:var(--coral)}

  .empty{
    text-align:center;padding:60px 20px;color:var(--ink-soft);
  }
  .empty strong{display:block;font-size:1.2rem;color:var(--ink);margin-bottom:6px;font-family:'Space Grotesk',sans-serif}

  #chatToggle{
    position:fixed;right:20px;bottom:20px;z-index:90;
    width:62px;height:62px;border-radius:20px;cursor:pointer;
    background:var(--coral);color:#fff;border:2.5px solid var(--ink);
    box-shadow:4px 4px 0 var(--ink);
    display:grid;place-items:center;font-size:1.6rem;
    transition:transform .15s ease;
    animation:wobble 3s ease-in-out infinite;
  }
  @keyframes wobble{0%,86%,100%{transform:rotate(0)}90%{transform:rotate(-6deg)}94%{transform:rotate(6deg)}}
  #chatToggle:hover{transform:scale(1.06)}
  #chatToggle .ping{
    position:absolute;top:-6px;right:-6px;width:18px;height:18px;
    background:var(--mint);border:2px solid var(--ink);border-radius:50%;
  }

  #chatPanel{
    position:fixed;right:20px;bottom:96px;z-index:95;
    width:min(380px,calc(100vw - 32px));
    height:min(560px,calc(100vh - 140px));
    background:var(--card);border:2.5px solid var(--ink);border-radius:20px;
    box-shadow:6px 6px 0 var(--ink);
    display:none;flex-direction:column;overflow:hidden;
  }
  #chatPanel.open{display:flex;animation:slideUp .25s ease both}
  @keyframes slideUp{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}

  .chat-head{
    background:var(--ink);color:var(--bg);
    padding:14px 16px;display:flex;align-items:center;gap:10px;
  }
  .chat-avatar{
    width:36px;height:36px;border-radius:10px;background:var(--sun);
    display:grid;place-items:center;font-size:1.1rem;border:2px solid var(--bg);
  }
  .chat-head h2{font-size:.98rem;font-weight:700}
  .chat-head small{font-size:.7rem;opacity:.75;display:block}
  .chat-head-actions{margin-left:auto;display:flex;gap:6px}
  .head-btn{
    background:transparent;border:1.5px solid var(--bg);color:var(--bg);
    width:30px;height:30px;border-radius:8px;cursor:pointer;font-size:.9rem;
    display:grid;place-items:center;transition:background .15s;
  }
  .head-btn:hover{background:#ffffff26}

  #ollamaSettings{
    display:none;padding:12px 14px;background:#fff4e8;border-bottom:2px dashed var(--ink);
    gap:8px;flex-direction:column;
  }
  #ollamaSettings.open{display:flex}
  #ollamaSettings label{font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em}
  #ollamaSettings input{
    padding:8px 10px;border:2px solid var(--ink);border-radius:8px;
    font-family:inherit;font-size:.82rem;background:#fff;outline:none;width:100%;
  }
  #ollamaStatus{font-size:.72rem;font-weight:600}
  #ollamaStatus.on{color:var(--mint)}
  #ollamaStatus.off{color:var(--coral)}

  .chat-body{
    flex:1;overflow-y:auto;padding:16px;
    display:flex;flex-direction:column;gap:10px;
    background:
      radial-gradient(circle at 15% 20%, #ffc93c14 0 60px, transparent 61px),
      radial-gradient(circle at 85% 75%, #ff4d2e10 0 80px, transparent 81px);
  }
  .msg{
    max-width:86%;padding:10px 14px;border-radius:14px;font-size:.88rem;
    border:2px solid var(--ink);animation:pop .2s ease both;word-wrap:break-word;
  }
  .msg.bot{background:#fff;border-bottom-left-radius:4px;align-self:flex-start}
  .msg.user{background:var(--sky);color:#fff;border-bottom-right-radius:4px;align-self:flex-end}
  .msg.bot a{color:var(--coral);font-weight:700}
  .msg .mini-list{margin-top:6px;display:flex;flex-direction:column;gap:4px}
  .msg .mini-item{
    font-size:.8rem;background:var(--bg);border:1.5px solid var(--ink);
    border-radius:8px;padding:5px 9px;
  }
  .msg .mini-item b{font-family:'Space Grotesk',sans-serif}
  .typing{display:flex;gap:4px;padding:12px 16px;align-self:flex-start}
  .typing span{
    width:8px;height:8px;border-radius:50%;background:var(--ink);opacity:.35;
    animation:blink 1s infinite;
  }
  .typing span:nth-child(2){animation-delay:.2s}
  .typing span:nth-child(3){animation-delay:.4s}
  @keyframes blink{0%,100%{opacity:.25;transform:translateY(0)}50%{opacity:1;transform:translateY(-3px)}}

  .quick-replies{
    padding:8px 12px;display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;
    border-top:1.5px solid var(--line);background:var(--card);
  }
  .quick-replies::-webkit-scrollbar{display:none}
  .qr{
    flex:0 0 auto;font-size:.76rem;font-weight:600;font-family:'Space Grotesk',sans-serif;
    padding:6px 12px;border-radius:999px;border:2px solid var(--ink);
    background:var(--sun);cursor:pointer;transition:transform .12s;
  }
  .qr:hover{transform:scale(1.05)}
  .qr:nth-child(even){background:#d8e6ff}

  .chat-foot{
    display:flex;gap:8px;padding:12px;border-top:2px solid var(--ink);background:var(--card);
  }
  #chatInput{
    flex:1;padding:12px 14px;border:2px solid var(--ink);border-radius:12px;
    font-family:inherit;font-size:.9rem;outline:none;background:var(--bg);
  }
  #chatInput:focus{background:#fff}
  #sendBtn{
    width:46px;flex:0 0 46px;border:2px solid var(--ink);border-radius:12px;
    background:var(--coral);color:#fff;font-size:1.15rem;cursor:pointer;
    box-shadow:2px 2px 0 var(--ink);transition:transform .12s;
  }
  #sendBtn:active{transform:translate(2px,2px);box-shadow:none}

  footer{
    border-top:2px solid var(--ink);padding:22px 20px;text-align:center;
    font-size:.8rem;color:var(--ink-soft);background:var(--card);
  }
  footer b{font-family:'Space Grotesk',sans-serif;color:var(--ink)}

  @media(max-width:480px){
    #chatPanel{right:8px;left:8px;bottom:88px;width:auto}
    #chatToggle{right:14px;bottom:14px}
  }
</style>
</head>
<body>

<header>
  <div class="nav">
    <a class="logo" href="#"><span class="logo-dot">⚡</span><span class="t-free">T<span>.</span>Free</span></a>
    <span class="nav-tag">100% gratuito · sem censura · global 🌍</span>
  </div>
</header>

<section class="hero">
  <h1>Encontre <em>IA grátis</em> de verdade, em qualquer lugar do mundo.</h1>
  <p><b>T.Free</b> é um catálogo aberto de inteligências artificiais gratuitas — chat, imagem, código e modelos locais sem filtros. Busque abaixo ou pergunte ao nosso assistente.</p>
  <div class="search-wrap">
    <svg viewBox="0 0 24 24" fill="none" stroke-width="2.4" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
    <input id="searchInput" type="search" placeholder="Buscar por nome, função… ex.: imagem, código, local, sem censura" autocomplete="off">
    <button id="clearBtn" title="Limpar">✕</button>
  </div>
</section>

<div class="filters" id="filters"></div>
<p class="result-count" id="resultCount"></p>

<main>
  <div class="grid" id="results"></div>
  <div class="empty" id="emptyState" style="display:none">
    <strong>Nada encontrado 🤔</strong>
    Tente outro termo — ou pergunte ao bot no canto da tela.
  </div>
</main>

<button id="chatToggle" aria-label="Abrir chat">💬<span class="ping"></span></button>

<div id="chatPanel" role="dialog" aria-label="Assistente T.Free">
  <div class="chat-head">
    <div class="chat-avatar">🤖</div>
    <div>
      <h2>Guia do T.Free</h2>
      <small>responde na hora · filtra a lista pra você</small>
    </div>
    <div class="chat-head-actions">
      <button class="head-btn" id="settingsBtn" title="Configurar Ollama">⚙️</button>
      <button class="head-btn" id="closeChat" title="Fechar">✕</button>
    </div>
  </div>

  <div id="ollamaSettings">
    <label>API URL (Ollama)</label>
    <input id="ollamaUrl" type="text" value="http://localhost:11434" placeholder="http://localhost:11434">
    <label>Chave de API (opcional)</label>
    <input id="ollamaKey" type="password" placeholder="cole aqui sua chave do Ollama">
    <label>Modelo</label>
    <input id="ollamaModel" type="text" value="llama3.1" placeholder="llama3.1, mistral, dolphin…">
    <span id="ollamaStatus" class="off">Modo local desativado — usando respostas automáticas.</span>
  </div>

  <div class="chat-body" id="chatBody"></div>
  <div class="quick-replies" id="quickReplies"></div>

  <form class="chat-foot" id="chatForm">
    <input id="chatInput" type="text" placeholder="Pergunte algo… ex.: quais IA grátis?" autocomplete="off">
    <button id="sendBtn" type="submit" aria-label="Enviar">➤</button>
  </form>
</div>

<footer>
  <b>T.Free</b> — catálogo comunitário de IAs gratuitas e sem censura. Os links levam aos sites oficiais de cada serviço.
</footer>

<script>
const SERVICES = [
  {name:"HuggingChat", icon:"🤗", color:"#ffd9a0", cat:"Chat", url:"https://huggingface.co/chat",
   desc:"Chat gratuito da Hugging Face com modelos abertos (Llama, Qwen, DeepSeek). Opções sem filtro ativáveis.",
   tags:["chat","gratis","codigo aberto","sem censura","conversa"], uncensored:true, local:false},
  {name:"Google AI Studio", icon:"✦", color:"#cfe0ff", cat:"Chat", url:"https://aistudio.google.com",
   desc:"Acesso gratuito aos modelos Gemini com API generosa. Ótimo para testar prompts e gerar chaves de API.",
   tags:["gemini","chat","api","gratis","google"], uncensored:false, local:false},
  {name:"Groq Cloud", icon:"⚡", color:"#ffe3a0", cat:"API / Dev", url:"https://console.groq.com",
   desc:"Inferência ultrarrápida e gratuita de Llama, Mixtral e DeepSeek via API. Nível free diário generoso.",
   tags:["api","rapido","llama","gratis","desenvolvedor"], uncensored:false, local:false},
  {name:"OpenRouter", icon:"🔀", color:"#d8f5e8", cat:"API / Dev", url:"https://openrouter.ai",
   desc:"Agregador com dezenas de modelos 100% gratuitos (seção :free). Uma única API para várias IAs.",
   tags:["api","agregador","modelos gratis","desenvolvedor"], uncensored:false, local:false},
  {name:"Ollama", icon:"🦙", color:"#ffe0d1", cat:"Local / Offline", url:"https://ollama.com",
   desc:"Rode LLMs localmente com um comando. Suporta modelos sem censura como Dolphin-Mixtral e Nous Hermes.",
   tags:["local","offline","privacidade","sem censura","llama","api"], uncensored:true, local:true},
  {name:"LM Studio", icon:"🖥️", color:"#e4dcff", cat:"Local / Offline", url:"https://lmstudio.ai",
   desc:"App desktop para baixar e rodar modelos GGUF offline, com interface de chat e servidor API local.",
   tags:["local","offline","desktop","sem censura","privacidade"], uncensored:true, local:true},
  {name:"Jan", icon:"🌱", color:"#d9f7c9", cat:"Local / Offline", url:"https://jan.ai",
   desc:"Alternativa open source e offline ao ChatGPT. Roda modelos locais com total privacidade, sem censura.",
   tags:["local","offline","codigo aberto","sem censura","chat"], uncensored:true, local:true},
  {name:"GPT4All", icon:"🧩", color:"#c9f0f7", cat:"Local / Offline", url:"https://www.nomic.ai/gpt4all",
   desc:"Suite gratuita para rodar LLMs no seu computador, inclusive sem internet. Modelos abertos e sem filtro.",
   tags:["local","offline","gratis","sem censura","chat"], uncensored:true, local:true},
  {name:"Le Chat (Mistral)", icon:"🌀", color:"#ffe9c9", cat:"Chat", url:"https://chat.mistral.ai",
   desc:"Chat gratuito da Mistral AI com modelos europeus poderosos e limites de uso bem generosos.",
   tags:["chat","mistral","gratis","europa"], uncensored:false, local:false},
  {name:"Meta AI", icon:"🅼", color:"#d5e4ff", cat:"Chat", url:"https://www.meta.ai",
   desc:"Assistente gratuito da Meta baseado em Llama. Disponível globalmente via web e WhatsApp.",
   tags:["chat","llama","meta","gratis","whatsapp"], uncensored:false, local:false},
  {name:"Poe", icon:"🎭", color:"#ffd6ec", cat:"Chat", url:"https://poe.com",
   desc:"Plataforma com vários bots gratuitos (GPT, Claude, Llama). Pontos diários grátis para modelos premium.",
   tags:["chat","bots","varios modelos","gratis"], uncensored:false, local:false},
  {name:"Perplexity", icon:"🔎", color:"#d0f0e0", cat:"Busca", url:"https://www.perplexity.ai",
   desc:"Motor de busca com IA que cita fontes. Versão gratuita ilimitada para perguntas rápidas.",
   tags:["busca","pesquisa","fontes","gratis"], uncensored:false, local:false},
  {name:"DuckDuckGo AI Chat", icon:"🦆", color:"#ffe4b5", cat:"Busca", url:"https://duckduckgo.com/chat",
   desc:"Chat anônimo e gratuito com GPT, Claude, Llama e Mixtral. Sem conta, sem rastreamento.",
   tags:["anonimo","chat","privacidade","gratis"], uncensored:false, local:false},
  {name:"DeepInfra", icon:"🏗️", color:"#dce8d0", cat:"API / Dev", url:"https://deepinfra.com",
   desc:"API de inferência com créditos gratuitos e modelos open source baratos, incluindo Llama e Qwen.",
   tags:["api","desenvolvedor","gratis","inferencia"], uncensored:false, local:false},
  {name:"Together AI", icon:"🤝", color:"#e0e8ff", cat:"API / Dev", url:"https://www.together.ai",
   desc:"Créditos gratuitos para API e playground com centenas de modelos open source, incluindo opções uncensored.",
   tags:["api","desenvolvedor","creditos","sem censura"], uncensored:true, local:false},
  {name:"Leonardo AI", icon:"🎨", color:"#ffd9e8", cat:"Imagem", url:"https://leonardo.ai",
   desc:"Geração de imagens com tokens gratuitos diários. Vários modelos e estilos, qualidade profissional.",
   tags:["imagem","arte","gerador","gratis","design"], uncensored:false, local:false},
  {name:"Tensor.Art", icon:"🖼️", color:"#d9ffe9", cat:"Imagem", url:"https://tensor.art",
   desc:"Plataforma gratuita de geração de imagens com modelos Stable Diffusion da comunidade, opções sem filtro.",
   tags:["imagem","stable diffusion","nsfw","sem censura","gratis"], uncensored:true, local:false},
  {name:"Mage.space", icon:"🧙", color:"#ece0ff", cat:"Imagem", url:"https://www.mage.space",
   desc:"Gerador de imagens gratuito com Stable Diffusion. Modo irrestrito disponível para conteúdo sem censura.",
   tags:["imagem","stable diffusion","sem censura","nsfw","gratis"], uncensored:true, local:false},
  {name:"SillyTavern", icon:"🍺", color:"#ffeed1", cat:"Chat", url:"https://sillytavern.app",
   desc:"Front-end open source para roleplay sem censura com IAs. Conecta em APIs locais (Ollama, KoboldCpp).",
   tags:["roleplay","sem censura","local","chat","codigo aberto"], uncensored:true, local:true},
  {name:"You.com", icon:"🫵", color:"#d4f4ff", cat:"Busca", url:"https://you.com",
   desc:"Buscador com IA integrada e chat gratuito. Modo de pesquisa inteligente sem necessidade de conta.",
   tags:["busca","chat","pesquisa","gratis"], uncensored:false, local:false},
  {name:"CodeGeeX", icon:"💻", color:"#d8ffd8", cat:"Código", url:"https://codegeex.cn",
   desc:"Assistente de código gratuito para VS Code e JetBrains. Autocompletar e chat de programação sem custo.",
   tags:["codigo","programacao","vscode","gratis","dev"], uncensored:false, local:false},
  {name:"KoboldCpp", icon:"📜", color:"#f7e8d0", cat:"Local / Offline", url:"https://github.com/LostRuins/koboldcpp",
   desc:"Motor local leve para rodar modelos de escrita e roleplay sem nenhuma censura, direto do seu PC.",
   tags:["local","offline","sem censura","roleplay","escrita"], uncensored:true, local:true}
];

const CATEGORIES = ["Todos","Chat","Local / Offline","API / Dev","Imagem","Busca","Código"];
let activeCat = "Todos";
let activeQuery = "";

const resultsEl = document.getElementById("results");
const emptyEl = document.getElementById("emptyState");
const countEl = document.getElementById("resultCount");
const searchInput = document.getElementById("searchInput");
const clearBtn = document.getElementById("clearBtn");
const filtersEl = document.getElementById("filters");

function buildChips(){
  filtersEl.innerHTML = "";
  CATEGORIES.forEach(cat=>{
    const b = document.createElement("button");
    b.className = "chip" + (cat===activeCat?" active":"");
    b.textContent = cat;
    b.onclick = ()=>{ activeCat = cat; buildChips(); render(); };
    filtersEl.appendChild(b);
  });
}

function matchService(s, q){
  if(!q) return true;
  const hay = (s.name+" "+s.desc+" "+s.cat+" "+s.tags.join(" ")).toLowerCase();
  return q.toLowerCase().split(/\s+/).every(term=>hay.includes(term));
}

function filterList(q = activeQuery, cat = activeCat){
  return SERVICES.filter(s => (cat==="Todos" || s.cat===cat) && matchService(s,q));
}

function render(){
  const list = filterList();
  resultsEl.innerHTML = "";
  list.forEach((s,i)=>{
    const card = document.createElement("article");
    card.className = "card";
    card.style.animationDelay = (i*0.04)+"s";
    card.innerHTML = `
      <div class="card-top">
        <div class="card-icon" style="background:${s.color}">${s.icon}</div>
        <div>
          <h3>${s.name}</h3>
          <span class="card-cat">${s.cat}</span>
        </div>
      </div>
      <p>${s.desc}</p>
      <div class="badges">
        <span class="badge free">Grátis</span>
        ${s.uncensored?'<span class="badge uncensored">Sem censura</span>':""}
        ${s.local?'<span class="badge local">Offline</span>':""}
      </div>
      <a class="card-link" href="${s.url}" target="_blank" rel="noopener">Visitar site →</a>`;
    resultsEl.appendChild(card);
  });
  emptyEl.style.display = list.length ? "none" : "block";
  countEl.textContent = `${list.length} serviço${list.length===1?"":"s"} encontrado${list.length===1?"":"s"}`;
}

searchInput.addEventListener("input", ()=>{
  activeQuery = searchInput.value.trim();
  clearBtn.classList.toggle("show", activeQuery.length>0);
  render();
});
clearBtn.addEventListener("click", ()=>{
  searchInput.value=""; activeQuery=""; clearBtn.classList.remove("show"); render(); searchInput.focus();
});

buildChips();
render();

const chatToggle = document.getElementById("chatToggle");
const chatPanel  = document.getElementById("chatPanel");
const chatBody   = document.getElementById("chatBody");
const chatForm   = document.getElementById("chatForm");
const chatInput  = document.getElementById("chatInput");
const closeChat  = document.getElementById("closeChat");
const settingsBtn= document.getElementById("settingsBtn");
const ollamaBox  = document.getElementById("ollamaSettings");
const ollamaUrlI = document.getElementById("ollamaUrl");
const ollamaKeyI = document.getElementById("ollamaKey");
const ollamaModI = document.getElementById("ollamaModel");
const ollamaStat = document.getElementById("ollamaStatus");
const quickEl    = document.getElementById("quickReplies");

const QUICK = ["quais IA grátis?","IA sem censura","IA de imagem","IA local / offline","IA para código","API gratuita","IA de busca"];

function buildQuick(){
  quickEl.innerHTML="";
  QUICK.forEach(q=>{
    const b=document.createElement("button");
    b.className="qr"; b.type="button"; b.textContent=q;
    b.onclick=()=>{ chatInput.value=q; chatForm.requestSubmit(); };
    quickEl.appendChild(b);
  });
}
buildQuick();

let panelOpen=false;
function toggleChat(force){
  panelOpen = force!==undefined ? force : !panelOpen;
  chatPanel.classList.toggle("open", panelOpen);
  if(panelOpen && !chatBody.dataset.greeted){
    chatBody.dataset.greeted="1";
    setTimeout(()=>botSay("Olá! 👋 Eu sou o guia do <b>T.Free</b>. Posso filtrar a lista de IAs gratuitas pra você. Pergunte algo como <i>“quais IA grátis?”</i>, <i>“IA sem censura”</i> ou <i>“IA de imagem”</i>."),300);
  }
  if(panelOpen) setTimeout(()=>chatInput.focus(),250);
}
chatToggle.onclick=()=>toggleChat();
closeChat.onclick=()=>toggleChat(false);
settingsBtn.onclick=()=>{
  ollamaBox.classList.toggle("open");
  updateOllamaStatus();
};
[ollamaUrlI,ollamaKeyI,ollamaModI].forEach(i=>i.addEventListener("input",updateOllamaStatus));

function ollamaEnabled(){ return !!(ollamaUrlI.value.trim() && ollamaKeyI.value.trim() && ollamaModI.value.trim()); }
function updateOllamaStatus(){
  if(ollamaEnabled()){
    ollamaStat.className="on";
    ollamaStat.textContent="Modo Ollama ATIVO → respostas via "+ollamaModI.value.trim();
  }else{
    ollamaStat.className="off";
    ollamaStat.textContent="Modo local desativado — usando respostas automáticas.";
  }
}
updateOllamaStatus();

function esc(t){return t.replace(/</g,"&lt;").replace(/>/g,"&gt;");}

function userSay(text){
  const d=document.createElement("div");
  d.className="msg user"; d.textContent=text;
  chatBody.appendChild(d); chatBody.scrollTop=chatBody.scrollHeight;
}
function botSay(html){
  const d=document.createElement("div");
  d.className="msg bot"; d.innerHTML=html;
  chatBody.appendChild(d); chatBody.scrollTop=chatBody.scrollHeight;
}
function showTyping(){
  const t=document.createElement("div");
  t.className="typing"; t.id="typing";
  t.innerHTML="<span></span><span></span><span></span>";
  chatBody.appendChild(t); chatBody.scrollTop=chatBody.scrollHeight;
}
function hideTyping(){ const t=document.getElementById("typing"); if(t)t.remove(); }

function serviceListHTML(list,limit=5){
  if(!list.length) return "";
  const items = list.slice(0,limit).map(s=>
    `<div class="mini-item">${s.icon} <b>${s.name}</b> — <a href="${s.url}" target="_blank" rel="noopener">abrir</a></div>`
  ).join("");
  const more = list.length>limit ? `<div class="mini-item">… e mais ${list.length-limit} na lista principal 👇</div>` : "";
  return `<div class="mini-list">${items}${more}</div>`;
}

function applyFilterToPage(query, cat){
  searchInput.value = query||"";
  activeQuery = query||"";
  activeCat = (cat && CATEGORIES.includes(cat)) ? cat : "Todos";
  clearBtn.classList.toggle("show", !!activeQuery);
  buildChips(); render();
  document.querySelector("main").scrollIntoView({behavior:"smooth"});
}

function has2(s,...ws){ const hay=(s.name+" "+s.desc+" "+s.tags.join(" ")).toLowerCase(); return ws.some(w=>hay.includes(w)); }

function keywordAnswer(msg){
  const m = msg.toLowerCase();
  const has = (...ws)=>ws.some(w=>m.includes(w));

  if(has("t.free","tfree","este site","o site","quem é você","quem e você","quem é vc","quem e vc")){
    return `Eu sou o guia do <b>T.Free</b> 🆓⚡ — um catálogo comunitário de IAs <b>gratuitas</b> e <b>sem censura</b>, acessíveis no mundo todo. Posso filtrar a lista da página pra você!`;
  }
  if(has("sem censura","uncensored","sem filtro","irrestrit","nsfw","liberada")){
    const l = SERVICES.filter(s=>s.uncensored);
    applyFilterToPage("sem censura");
    return `Encontrei <b>${l.length} opções sem censura</b> — já filtrei a lista da página pra você 😉${serviceListHTML(l)}`;
  }
  if(has("imagem","arte","desenh","foto","midjourney","stable diffusion","gerar imagem")){
    const l = SERVICES.filter(s=>s.cat==="Imagem");
    applyFilterToPage("imagem","Imagem");
    return `Estas geram <b>imagens de graça</b>:${serviceListHTML(l)}`;
  }
  if(has("local","offline","privacidade","meu pc","computador","sem internet")){
    const l = SERVICES.filter(s=>s.local);
    applyFilterToPage("local","Local / Offline");
    return `Para rodar <b>IA local/offline</b> (máxima privacidade e zero censura com o modelo certo):${serviceListHTML(l)}`;
  }
  if(has("codigo","código","program","dev","vscode","api")){
    if(has("api")){
      const l = SERVICES.filter(s=>s.cat==="API / Dev");
      applyFilterToPage("api","API / Dev");
      return `Estas oferecem <b>API gratuita</b> para desenvolvedores:${serviceListHTML(l)}`;
    }
    const l = SERVICES.filter(s=>s.cat==="Código" || s.tags.includes("codigo"));
    applyFilterToPage("código","Código");
    return `Para <b>programação</b>, recomendo:${serviceListHTML(l)}`;
  }
  if(has("busca","pesquis","pergunta com fonte")){
    const l = SERVICES.filter(s=>s.cat==="Busca");
    applyFilterToPage("busca","Busca");
    return `IAs de <b>busca/pesquisa</b> gratuitas:${serviceListHTML(l)}`;
  }
  if(has("gpt","chatgpt","openai")){
    return `O ChatGPT tem versão paga, mas estas alternativas <b>gratuitas</b> rodam modelos parecidos:${serviceListHTML(SERVICES.filter(s=>has2(s,"poe","duckduckgo","llama")),4)}`;
  }
  if(has("claude","anthropic")){
    return `O Claude oficial é pago/limitado, mas você pode usá-lo <b>de graça</b> no Poe e no DuckDuckGo:${serviceListHTML(SERVICES.filter(s=>has2(s,"poe","duckduckgo")),3)}`;
  }
  if(has("gemini","google")){
    return `O Gemini pode ser testado de graça no Google AI Studio:${serviceListHTML(SERVICES.filter(s=>has2(s,"gemini","google")),3)}`;
  }
  if(has("roleplay","rp","historia","história","personagem","escrever","escrita")){
    const l = SERVICES.filter(s=>has2(s,"roleplay","escrita"));
    applyFilterToPage("roleplay");
    return `Para <b>roleplay e escrita criativa sem censura</b>:${serviceListHTML(l)}`;
  }
  if(has("video","vídeo","voz","audio","áudio","musica","música")){
    return `O <b>T.Free</b> foca em <b>texto, imagem e código</b>. Para voz/áudio, sugiro rodar modelos Whisper e TTS localmente com <b>Ollama</b> ou <b>LM Studio</b> 🎙️`;
  }
  if(has("gratis","grátis","free","gratuit","quais","lista","opcoes","opções","todas","catalogo","catálogo")){
    applyFilterToPage("");
    return `Aqui estão os destaques <b>100% gratuitos</b> do T.Free:${serviceListHTML(SERVICES,6)}`;
  }
  if(has("oi","olá","ola","hey","bom dia","boa tarde","boa noite","e ai","eai")){
    return `Oi! 👋 Bem-vindo ao <b>T.Free</b>. Posso sugerir <b>IA grátis</b>, <b>sem censura</b>, <b>de imagem</b>, <b>local/offline</b> ou <b>para código</b>.`;
  }
  if(has("obrigado","obrigada","valeu","vlw","thanks")){
    return `Por nada! 🙌 O T.Free está sempre aqui.`;
  }
  if(has("como funciona","ajuda","help","o que você faz","o que vc faz")){
    return `Eu faço 3 coisas: <b>1)</b> respondo dúvidas sobre IAs gratuitas, <b>2)</b> filtro a lista automaticamente, <b>3)</b> uso sua <b>chave da API do Ollama</b> (no ⚙️) para responder com seu modelo local.`;
  }
  const found = SERVICES.filter(s=>{
    const hay=(s.name+" "+s.tags.join(" ")).toLowerCase();
    return m.split(/\s+/).filter(w=>w.length>3).some(w=>hay.includes(w));
  });
  if(found.length){
    applyFilterToPage(found[0].name.split(" ")[0]);
    return `Achei algo relacionado no T.Free 🔎${serviceListHTML(found,4)}`;
  }
  return `Hmm, não tenho uma resposta pronta pra isso 🤔 Tente: <i>“quais IA grátis?”</i>, <i>“IA sem censura”</i>, <i>“IA de imagem”</i>, <i>“IA local”</i> ou <i>“API gratuita”</i>.`;
}

async function askOllama(msg){
  const url = ollamaUrlI.value.trim().replace(/\/$/,"") + "/api/chat";
  const headers = {"Content-Type":"application/json"};
  const key = ollamaKeyI.value.trim();
  if(key) headers["Authorization"] = "Bearer "+key;
  const res = await fetch(url,{
    method:"POST", headers,
    body: JSON.stringify({
      model: ollamaModI.value.trim(),
      stream:false,
      messages:[
        {role:"system",content:"Você é o guia do T.Free, um catálogo de IAs gratuitas e sem censura. Responda em português, curto e útil. Serviços conhecidos: "+SERVICES.map(s=>s.name+" ("+s.cat+")").join(", ")+"."},
        {role:"user",content:msg}
      ]
    })
  });
  if(!res.ok) throw new Error("HTTP "+res.status);
  const data = await res.json();
  return esc(data.message?.content || "Sem resposta do modelo.");
}

chatForm.addEventListener("submit", async (e)=>{
  e.preventDefault();
  const msg = chatInput.value.trim();
  if(!msg) return;
  chatInput.value="";
  userSay(msg);
  showTyping();

  if(ollamaEnabled()){
    try{
      const reply = await askOllama(msg);
      hideTyping();
      botSay(reply);
      return;
    }catch(err){
      hideTyping();
      botSay("⚠️ Não consegui falar com o Ollama ("+esc(err.message)+"). Vou responder no modo automático:");
      showTyping();
    }
  }
  setTimeout(()=>{
    hideTyping();
    botSay(keywordAnswer(msg));
  }, 450 + Math.random()*400);
});
</script>
</body>
</html>
```

---

### 📄 `README.md`

```markdown
<div align="center">

# ⚡ T.Free

### Inteligência Artificial gratuita, sem censura e acessível no mundo todo 🌍

**Um catálogo aberto de IAs gratuitas — em um único arquivo HTML, sem dependências, sem build, sem complicação.**

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](#)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](#)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](#)
[![Licença MIT](https://img.shields.io/badge/License-MIT-00c48c?style=for-the-badge)](#-licença)
[![Sem dependências](https://img.shields.io/badge/dependencies-none-ff4d2e?style=for-the-badge)](#)

</div>

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

---

✅ **Pronto!** Agora o repositório está completo:
- `index.html` → site funcional, responsivo e com bot inteligente
- `README.md` → documentação apresentável com badges, tabelas, emojis e estrutura clara

É só criar os dois arquivos, commitar e subir para o GitHub.
