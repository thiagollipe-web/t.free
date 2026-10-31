"""Acceptance checks for verified alternatives; unknown prices must never become free."""
import json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class CatalogueContract(unittest.TestCase):
 def setUp(self):self.items=json.loads((ROOT/'data/catalogue.json').read_text())
 def test_kind_execution_and_cost_separation(self):
  for item in self.items:
   self.assertIn(item.get('kind'),{'app','agent','runtime','service'})
   self.assertIn(item.get('execution'),{'hosted','local','hybrid','api','self-hosted'})
   self.assertIsNone(item['costs']['softwareFee'])
   for key in ('software','model','hosting'):self.assertTrue(item['costs'][key].strip())
   self.assertRegex(item['reviewedAt'],r'^\d{4}-\d{2}-\d{2}$')
 def test_verified_agents_and_aliases(self):
  by_name={a['name']:a for a in self.items}
  self.assertEqual(len(self.items),35)
  hermes=by_name['Hermes Agent'];self.assertEqual(hermes['kind'],'agent');self.assertIn('ChatGPT',[x['name'] for x in hermes['alternativesTo']]);self.assertTrue(hermes['costs']['dependencies'])
  self.assertIn('API',by_name['OpenCode']['costs']['model']);self.assertEqual(by_name['Morphic']['execution'],'self-hosted')
  self.assertIn('NotebookLM',by_name['Gemini Notebook (antigo NotebookLM)']['aliases'])
 def test_static_cards_and_fiches_expose_costs(self):
  page=(ROOT/'index.html').read_text();self.assertIn('data-kind="agent"',page);self.assertIn('data-search=',page)
  for slug in ['hermes-agent','opencode','morphic']:
   p=ROOT/'ferramentas'/slug/'index.html';self.assertTrue(p.exists());s=p.read_text()
   for term in ['Software','Modelo / API','Infraestrutura','31/10/2026']:self.assertIn(term,s)
if __name__=='__main__':unittest.main(verbosity=2)
