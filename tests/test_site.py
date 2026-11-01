"""Static SEO/link checks and browser interaction regression tests."""
import json,re,unittest,xml.etree.ElementTree as ET
import os,threading,http.server,functools,tempfile
from pathlib import Path
from urllib.parse import urlparse,unquote
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
class StaticTests(unittest.TestCase):
 def test_catalogue_and_indexable_pages(self):
  data=json.loads((ROOT/'data/catalogue.json').read_text());home=(ROOT/'index.html').read_text();self.assertEqual(len(data),35);self.assertEqual(home.count('<article class="card"'),35)
  pages=[ROOT/'index.html',*ROOT.glob('ferramentas/*/index.html'),*ROOT.glob('categorias/*/index.html'),*ROOT.glob('guias/*/index.html')];self.assertEqual(len(pages),52)
  for p in pages:
   s=p.read_text();self.assertIn('lang="pt-BR"',s);self.assertEqual(s.count('<h1>'),1,p);self.assertEqual(s.count('rel="canonical"'),1,p);self.assertIn('property="og:image"',s);self.assertNotIn('data:image',s)
   for url in re.findall(r'(?:href|src)="([^"]+)"',s):
    if url.startswith(('https:','http:','#')):continue
    target=(p.parent/unquote(url.split('#')[0])).resolve()
    self.assertTrue(target.exists(),str(p)+' broken '+url)
 def test_caramelo_visual_identity(self):
  home=(ROOT/'index.html').read_text()
  self.assertIn('assets/caramelo.svg',home);self.assertIn('assets/caramelo.css',home)
  self.assertIn('Encontre sua próxima IA.',home);self.assertIn('hero-logos',home)
  self.assertNotIn('class="hero-art"',home)
  self.assertIn('Sua seleção',home)
  self.assertTrue((ROOT/'assets/caramelo.svg').exists())
 def test_sitemap(self):
  ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'};tree=ET.parse(ROOT/'sitemap.xml');urls=[x.text for x in tree.findall('.//s:loc',ns)];self.assertEqual(len(urls),52);self.assertEqual(len(set(urls)),52)
  self.assertTrue(all(x.startswith('https://thiagollipe-web.github.io/t.free/') for x in urls))
class BrowserTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.p=sync_playwright().start();cls.browser=cls.p.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or None)
  cls.folder=tempfile.TemporaryDirectory();Path(cls.folder.name,"t.free").symlink_to(ROOT,target_is_directory=True)
  cls.server=http.server.ThreadingHTTPServer(("127.0.0.1",0),functools.partial(http.server.SimpleHTTPRequestHandler,directory=cls.folder.name))
  threading.Thread(target=cls.server.serve_forever,daemon=True).start();cls.url="http://127.0.0.1:"+str(cls.server.server_port)+"/t.free/"
 @classmethod
 def tearDownClass(cls):cls.server.shutdown();cls.server.server_close();cls.browser.close();cls.p.stop();cls.folder.cleanup()
 def test_search_filter_comparison_and_chat(self):
  page=self.browser.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto(self.url);page.wait_for_selector('#filters button')
  self.assertEqual(page.locator('#grid .card:visible').count(),35)
  page.locator('#search').fill('áudio');self.assertEqual(set(page.locator('#grid .card:visible').evaluate_all('(cards) => cards.map(card => card.dataset.name)')), {'ElevenLabs','Suno','Microsoft Clipchamp','Gemini Notebook (antigo NotebookLM)'})
  page.locator('#clear').click();page.get_by_role('button',name='Áudio',exact=True).click();self.assertEqual(page.locator('#grid .card:visible').count(),2)
  page.locator('#clear').click();page.get_by_role('button',name='Pesquisa',exact=True).click();self.assertEqual(page.locator('#grid .card:visible').count(),3)
  page.locator('#clear').click();page.locator('#search').fill('zzzinexistente');self.assertTrue(page.locator('#empty').is_visible());page.locator('#clear').click()
  checks=page.locator('#grid .compare-pick input');checks.nth(0).check();checks.nth(1).check();checks.nth(2).check();self.assertTrue(checks.nth(3).is_disabled());page.locator('#compare-open').click();self.assertTrue(page.locator('#compare-result table').is_visible());self.assertEqual(page.locator('#compare-result thead th').count(),4)
  page.locator('#compare-clear').click();self.assertFalse(page.locator('#compare-result').is_visible());self.assertFalse(checks.nth(3).is_disabled())
  page.locator('#chat-toggle').click();page.locator('#question').fill('quero uma IA offline');page.locator('#send').click();self.assertEqual(page.locator('#grid .card:visible').count(),3);page.keyboard.press('Escape');self.assertFalse(page.locator('#chat').is_visible());self.assertEqual(page.locator('#chat-toggle').get_attribute('aria-expanded'),'false')
  page.locator('#chat-toggle').click();page.locator('.settings summary').click();page.locator('#mode').select_option('ollama');page.locator('#endpoint').fill('https://example.com');page.locator('#test').click();page.wait_for_selector('.bubble.error');self.assertIn('somente localhost',page.locator('.bubble.error').last.inner_text());self.assertEqual(errors,[]);page.close()
 def test_alias_search_related_products_and_preserved_selection(self):
  page=self.browser.new_page();page.goto(self.url);page.wait_for_selector('#filters button')
  page.locator('#search').fill('Cursor');self.assertEqual(page.locator('#grid .card:visible .tool-title').all_text_contents(),['OpenCode'])
  page.locator('#grid .card:visible .compare-pick input').check();page.locator('#search').fill('Hermes');self.assertEqual(page.locator('#grid .card:visible .tool-title').all_text_contents(),['Hermes Agent']);page.locator('#grid .card:visible .compare-pick input').check()
  page.locator('#compare-open').click();self.assertIn('OpenCode',page.locator('#compare-result').inner_text());self.assertIn('Hermes Agent',page.locator('#compare-result').inner_text());self.assertIn('Modelo / API',page.locator('#compare-result').inner_text());self.assertIn('cobrar',page.locator('#compare-result').inner_text())
  page.locator('#search').fill('Cursor');page.get_by_role('button',name='Agentes',exact=True).click();self.assertTrue(page.locator('#empty').is_visible());self.assertIn('2 selecionadas',page.locator('#compare-status').inner_text())
  page.locator('#clear').click();page.locator('#search').fill('OPEN CODE');self.assertEqual(page.locator('#grid .card:visible .tool-title').all_text_contents(),['OpenCode'])
  page.locator('#search').fill('NotebookLM');self.assertEqual(page.locator('#grid .card:visible .tool-title').all_text_contents(),['Gemini Notebook (antigo NotebookLM)']);page.close()
 def test_mobile_comparison_and_keyboard(self):
  page=self.browser.new_page(viewport={'width':390,'height':844});page.goto(self.url);page.wait_for_selector('#filters button')
  page.keyboard.press('Tab');self.assertEqual(page.locator(':focus').inner_text(),'Pular para o catálogo');page.keyboard.press('Enter');self.assertTrue(page.url.endswith('#catalogue'))
  checks=page.locator('#grid .compare-pick input');checks.nth(0).focus();page.keyboard.press('Space');checks.nth(1).focus();page.keyboard.press('Space');page.locator('#compare-open').focus();page.keyboard.press('Enter')
  self.assertTrue(page.locator('#compare-result table').is_visible());self.assertLessEqual(page.evaluate('document.documentElement.scrollWidth'),390)
  self.assertGreater(page.locator('#compare-result').evaluate('(el)=>el.scrollWidth'),page.locator('#compare-result').evaluate('(el)=>el.clientWidth'))
  page.locator('#compare-result').evaluate('(el)=>el.scrollLeft=el.scrollWidth');self.assertGreater(page.locator('#compare-result').evaluate('(el)=>el.scrollLeft'),0);page.close()
 def test_no_javascript_and_responsive(self):
  for width in (320,390,768,1440):
   context=self.browser.new_context(java_script_enabled=False,viewport={'width':width,'height':900});page=context.new_page();page.goto(self.url);self.assertEqual(page.locator('#grid .card:visible').count(),35);self.assertFalse(page.locator('#chat-toggle').is_visible());self.assertFalse(page.locator('#search').is_visible());self.assertLessEqual(page.evaluate('document.documentElement.scrollWidth'),width);page.locator('.tool-title').first.click();self.assertIn('chatgpt',page.url);self.assertTrue(page.get_by_role('heading',name='ChatGPT é gratuito?').is_visible());self.assertLessEqual(page.evaluate('document.documentElement.scrollWidth'),width);context.close()
if __name__=='__main__':unittest.main(verbosity=2)
