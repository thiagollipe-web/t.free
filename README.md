# T.Free — catálogo estático de IA em português

35 ferramentas, 35 fichas próprias e 13 páginas de categoria e 3 guias originais. As páginas são HTML real, acessíveis sem JavaScript. Busca, filtros, comparação de até três ferramentas e guia local são melhorias progressivas. Não há backend obrigatório, cadastro, analytics ou anúncios ativos.

## Desenvolvimento

```bash
python3 scripts/build.py
python3 -m http.server 8765 --bind 127.0.0.1
# Em outro terminal, com Python Playwright e Chromium disponíveis:
python3 -m unittest discover -s tests -v
node --check assets/catalogue.js
node --check assets/chat.js
node tests/test_local_safety.js
```

Abra http://127.0.0.1:8765/. Para o site baixado, preserve a estrutura de pastas; não é mais um arquivo único. Nenhum npm/build remoto é necessário para servir as páginas. O gerador usa apenas a biblioteca padrão do Python. Playwright é necessário somente para os testes de navegador.

## Onde editar

- `data/catalogue.json`: conteúdo, condições e fontes. Não invente cotas ou avaliações.
- `data/brandLogos.json`: caminhos dos logos locais; atribuições em `ASSET-NOTICES.txt`.
- `scripts/build.py`: geração das páginas, metadados e sitemap.
- `templates/base.html`: estrutura, transparência e conteúdo institucional preservado.
- `templates/catalogue.js`: busca, filtros e comparação; compilado para `assets/catalogue.js`.
- `assets/chat.js`: guia por regras e integração opcional com Ollama local.
- `assets/caramelo.css`: nova composição visual e responsive em revisão.
- `assets/caramelo.svg`: mascote vetorial original T.Free.
- `assets/legacy.css` e `assets/redesign.css`: estilos de base e compatibilidade.

Depois de editar fontes ou templates, rode o gerador e os testes. Não edite somente HTML gerado, pois a próxima geração o substitui.

## SEO e GitHub Pages

A origem configurada é `https://thiagollipe-web.github.io/t.free/`. Canonicals e URLs no sitemap respeitam o prefixo `/t.free/`. São 52 URLs HTML, sem dependência de renderização JavaScript para leitura dos cards e fichas. O sitemap não contém datas fictícias de atualização. Nenhuma nota/avaliação/preço foi inventado em dados estruturados.

**robots.txt precisa estar na raiz do host**, `https://thiagollipe-web.github.io/robots.txt`. Um arquivo em `/t.free/robots.txt` não controla o rastreamento. Este projeto não altera o repositório do site raiz. Não é necessário ter robots.txt para permitir rastreamento; após publicação autorizada, envie diretamente `https://thiagollipe-web.github.io/t.free/sitemap.xml` ao Search Console da propriedade correta. Acesso à propriedade, verificação e envio dependem do proprietário. Não há garantia de indexação, posição ou tráfego.

Antes de publicar: confirmar diff, rodar testes, publicar somente com autorização, verificar HTTP 200 de todas as URLs, canonical e sitemap no endereço final. Não alterar domínio nem criar anúncios/analytics nesta etapa.

## Transparência e datas

As informações do catálogo preservam a revisão editorial de 30/10/2026. O novo layout não significa novo teste de todos os serviços. ComfyUI, Canva AI e Microsoft Clipchamp receberam esclarecimentos de condições a partir das fontes oficiais verificadas em 31/10/2026. Referências continuam nas fichas. Não prometemos gratuidade ilimitada ou permanente. Modelos locais dependem de hardware e licenças; provedores externos e APIs podem cobrar.

## Ollama local

O guia padrão apenas filtra o catálogo por regras, não é IA generativa. A integração opcional exige instalar Ollama e um modelo local. Só aceita endpoints de loopback; rejeita modelos Cloud, redirecionamentos e URLs com credenciais. Nunca publique chaves. Se houver bloqueio CORS, permita apenas a origem usada, conforme https://docs.ollama.com/faq ; não use `OLLAMA_ORIGINS=*` nem exponha o servidor à internet. No celular, localhost é o próprio celular. Testes automatizados verificam o bloqueio de endpoints externos; não comprovam inferência real em um modelo instalado.

## Privacidade

Sem cookies próprios, armazenamento persistente, rastreadores ou scripts de publicidade. Seleção de comparação e histórico do guia ficam na memória da aba. Hospedagem e sites externos têm políticas próprias. O chat local envia conteúdo apenas ao endpoint escolhido e validado. Não envie dados sensíveis.

## CI de revisão

O workflow `Catalogue quality` executa somente em pull requests para main: gera o site, testa sintaxe/SEO/links, busca/filtros/comparação/guia e layouts sem JS em Chromium, sob o prefixo `/t.free/`. Também salva screenshots para revisão por 7 dias. Permissão apenas de leitura; nenhum deploy, secret ou aprovação automática. Para reproduzir, instale `playwright==1.62.0`, execute `python -m playwright install chromium` e rode os testes. Screenshots: `python scripts/screenshots.py`.

## Identidade visual — preview Caramelo

A branch `feat/visual-caramelo` propõe a nova direção solicitada após a publicação de PR #1: hero centralizado, tipografia serifada, navegação compacta, grade leve, cartões brancos em duas colunas e cachorro caramelo original. A organização visual pública do Gratos foi observada como referência; nenhum texto, CSS, código ou arte daquele site foi importado. O mascote foi desenhado em SVG para o T.Free. Textos continuam originais em português, com condições e fontes do catálogo.

Esta proposta permanece em revisão e não substitui o site publicado sem aprovação visual explícita. Não inclui estatísticas inventadas, economia monetária sem evidência, patrocínio ou coleta de e-mails. O painel compara ferramentas e custos qualitativos.

As 35 ferramentas e 52 URLs foram preservadas. Hermes Agent, OpenCode e Morphic são apps/agentes com dependências explícitas, não pesos de modelos.
