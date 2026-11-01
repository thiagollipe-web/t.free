/* Progressive enhancement: text preparation only. No installation or network execution. */
'use strict';
(()=>{
 const blocks=[...document.querySelectorAll('[data-prompt-id]')];if(!blocks.length)return;
 const dialog=document.getElementById('prompt-dialog'),preview=document.getElementById('prompt-preview-text'),status=document.getElementById('prompt-copy-status'),chips=document.getElementById('prompt-chips');
 const picks=blocks.map(b=>b.querySelector('[data-select-prompt]')).filter(Boolean);
 const bar=document.getElementById('prompt-actions'),open=document.getElementById('prompt-open'),copySelected=document.getElementById('prompt-copy-selected');
 let active=[],opener=null;
 function focusStart(){preview.focus();preview.setSelectionRange(0,0);preview.scrollTop=0;}
 const textOf=b=>b.querySelector('[data-prompt-text]').value;
 function compose(list){
  const intro=list.length===1?'Quero seguir este roteiro de configuração com cuidado.':'Quero seguir estes '+list.length+' roteiros de configuração, um por vez e na ordem abaixo. Conclua e valide cada etapa antes de passar à próxima.';
  return intro+'\n\n'+list.map((b,i)=>(list.length>1?'## '+(i+1)+'. '+b.dataset.promptTitle+'\n\n':'')+textOf(b)).join('\n\n')+'\n\nAntes de qualquer alteração, explique o plano, os custos, os dados enviados e as permissões necessárias. Confira a documentação oficial atual e a compatibilidade do ambiente. Faça perguntas se faltar contexto. Não execute instalações, comandos ou mudanças sem minha autorização explícita. Nunca peça senhas ou chaves no chat; explique como configurá-las com segurança no meu ambiente.';
 }
 function selected(){return blocks.filter(b=>b.querySelector('[data-select-prompt]')?.checked)}
 function refreshBar(){const n=selected().length;if(bar)bar.hidden=n===0;if(open)open.textContent='Ver prompt ('+n+')';if(copySelected)copySelected.textContent='Copiar seleção ('+n+')'}
 function draw(){preview.value=compose(active);status.textContent='Revise o texto antes de copiar. Copiar não instala nem configura nenhum serviço.';chips.replaceChildren();for(const b of active){const button=document.createElement('button');button.type='button';button.textContent=b.dataset.promptTitle+' ×';button.setAttribute('aria-label','Remover '+b.dataset.promptTitle);button.addEventListener('click',()=>{const check=b.querySelector('[data-select-prompt]');if(check)check.checked=false;active=active.filter(x=>x!==b);refreshBar();if(!active.length){dialog.close();return;}draw();focusStart()});chips.append(button)}}
 function show(list,trigger){if(!list.length)return;active=list;opener=trigger;draw();dialog.showModal();focusStart()}
 async function copy(){try{if(!navigator.clipboard?.writeText)throw new Error('unavailable');await navigator.clipboard.writeText(preview.value);status.textContent='Copiado! Cole no assistente de sua escolha e revise cada etapa antes de autorizar.'}catch(_){status.textContent='Não foi possível copiar automaticamente. O texto está selecionado: use Ctrl+C, Cmd+C ou o menu de copiar do celular.';preview.focus();preview.select();}}
 document.querySelectorAll('[data-copy-prompt]').forEach(button=>{button.hidden=false;button.addEventListener('click',()=>{const b=button.closest('[data-prompt-id]');show([b],button);copy()})});
 document.querySelectorAll('.prompt-pick').forEach(label=>label.hidden=false);
 picks.forEach(p=>p.addEventListener('change',refreshBar));
 open?.addEventListener('click',()=>show(selected(),open));copySelected?.addEventListener('click',()=>{show(selected(),copySelected);copy()});
 document.getElementById('prompt-copy').addEventListener('click',copy);
 document.getElementById('prompt-close').addEventListener('click',()=>dialog.close());
 dialog.addEventListener('close',()=>{if(opener?.isConnected&&opener.getClientRects().length>0)opener.focus();else document.getElementById('prompts')?.focus()});
 refreshBar();
})();
