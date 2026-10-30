## Sobre o projeto

**T.Free** reúne 32 ferramentas e é um catálogo de ferramentas de IA com opções gratuitas, faixas gratuitas e execução local. O aplicativo inteiro está em **`index.html`**, com HTML, CSS e JavaScript embutidos, sem bibliotecas externas, build ou backend obrigatório.

Gratuito não significa ilimitado. Serviços podem exigir conta, aplicar cotas e restrições regionais, ou oferecer funções pagas. Ferramentas locais exigem instalação prévia, modelos compatíveis e recursos do computador. Licenças e comportamento variam por modelo; não há promessa universal de “sem censura”.

## Funcionalidades

- Busca por nome, descrição e palavras-chave.
- Filtros por categoria, incluindo chat, imagem, áudio, vídeo, design, estudos, pesquisa, escrita, código e ferramentas locais/API.
- Filtro de acesso fácil para serviços usados diretamente no navegador.
- Cards com logos incorporados, selos, condições resumidas e links oficiais.
- Destaque para opções de acesso fácil no navegador, sem instalar aplicativos nem configurar uma API. Algumas exigem conta e têm cotas.
- Chat-guia por palavras-chave que filtra o catálogo, sem usar API.
- Modo opcional de conversa com **Ollama local**, com verificação de conexão e mensagens de erro.
- Layout responsivo, navegação por teclado e conteúdo em português brasileiro.

## Como usar

Baixe o arquivo `index.html` e abra no navegador. O catálogo e o chat-guia funcionam sem internet; visitar os sites oficiais exige conexão.

Ou clone o repositório:

```bash
git clone https://github.com/thiagollipe-web/t.free.git
cd t.free
```

Para servir o mesmo arquivo localmente, se tiver Python instalado:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Abra **http://127.0.0.1:8000**. No Windows, também pode usar `py -m http.server 8000 --bind 127.0.0.1`.

## Ollama local

1. Instale o [Ollama](https://ollama.com) e baixe um modelo adequado ao seu computador.
2. Mantenha o servidor local do Ollama em execução.
3. Abra o chat do T.Free e suas configurações.
4. Informe `http://localhost:11434` ou `http://127.0.0.1:11434`, teste a conexão e escolha um modelo instalado.
5. Selecione o modo Ollama local e envie sua mensagem.

**Ollama local não precisa de chave de API.** O T.Free não pede nem armazena chaves. Só aceita endpoints de loopback e rejeita modelos identificados como remotos/Cloud. O histórico fica apenas na memória da aba.

Se o navegador bloquear o acesso a partir de `file://`, use o servidor local acima. Se ainda houver bloqueio de origem, consulte a [documentação oficial de CORS](https://docs.ollama.com/faq#how-can-i-allow-additional-web-origins-to-access-ollama) e permita apenas a origem utilizada, como `http://127.0.0.1:8000`. Não use `OLLAMA_ORIGINS=*` nem exponha o servidor à internet.

No celular, `localhost` aponta para o próprio celular, não para o seu computador. O catálogo funciona no celular; o modo Ollama exige um servidor acessível no mesmo dispositivo e compatibilidade do navegador.

### E o Ollama Cloud?

[Ollama Cloud e Ollama local são serviços distintos](https://docs.ollama.com/api/introduction). A API Cloud usa autenticação e pode ter limites e custos. Esta versão não envia mensagens diretamente à API Cloud. Uma integração pública segura precisaria de backend para proteger a chave, contrariando a proposta de um único arquivo sem backend.

## Estrutura e personalização

- `index.html`: aplicação completa; edite o array `catalogue` para atualizar ferramentas e as variáveis CSS para mudar as cores.
- `README.md`: documentação, não é necessário para executar o aplicativo.

As condições dos serviços devem ser conferidas nos links oficiais. Os links de referência estão no próprio HTML.

## Verificação

Busca, filtros, chat-guia, layout mobile e desktop e caminhos de erro são verificáveis sem serviços externos. A integração Ollama pode ser testada com respostas simuladas; a execução de um modelo real depende da instalação e do hardware de quem abrir o arquivo.

## Contribuindo

Faça um fork, atualize o catálogo ou o código e abra um pull request. Não inclua chaves, tokens ou outros segredos no repositório.

## Licença

MIT, conforme a licença declarada pelo projeto. As ferramentas e modelos vinculados mantêm suas próprias licenças e condições.

### Logos e marcas

Logos são usados para identificar os serviços, sem vínculo ou endosso. Marcas pertencem aos respectivos titulares. Os ativos incorporados vêm de fontes oficiais, [Simple Icons](https://github.com/simple-icons/simple-icons) (biblioteca CC0) e [Lobe Icons](https://github.com/lobehub/lobe-icons) (biblioteca MIT). Fontes e avisos aplicáveis estão incorporados no HTML. Duck.ai utiliza a marca DuckDuckGo; Mistral Vibe utiliza a marca Mistral.

## Monetização: preparação, não ativação

O site tem espaço reservado para publicidade e informações de privacidade. **Não há anúncios Google ativos, ID de editor configurado ou aprovação do AdSense confirmada.** Não use IDs fictícios nem copie o código de outra pessoa.

Para ativar, o proprietário deve escolher sua conta Google/AdSense existente (o Google permite uma conta por editor), concluir os dados e termos necessários, adicionar e verificar o site e obter aprovação. Depois, o código real deve ser integrado com as configurações de consentimento aplicáveis e a política de privacidade atualizada. Não confunda um espaço reservado com receita ativa.

O endereço atual é um projeto em GitHub Pages, sob `thiagollipe-web.github.io/t.free/`. O cadastro e o `ads.txt` precisam respeitar o domínio reconhecido pelo Google e o local correto na raiz; não publicar um `ads.txt` fictício dentro da pasta do projeto. Se for necessário alterar o site raiz ou usar um domínio próprio, confirmar o destino antes.

Referências oficiais: [criar conta](https://support.google.com/adsense/answer/7402253?hl=pt-BR), [qualificação](https://support.google.com/adsense/answer/9724?hl=pt-BR), [uma conta por editor](https://support.google.com/adsense/answer/9729?hl=pt-BR), [privacidade obrigatória](https://support.google.com/adsense/answer/1348695?hl=pt-BR). Aprovação e receita não são garantidas.
