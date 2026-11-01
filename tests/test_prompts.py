"""Prompt content, progressive enhancement and clipboard regression tests."""
import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class PromptContentTests(unittest.TestCase):
 def test_prompts_are_reviewable_and_bound_to_tools(self):
  prompts=json.loads((ROOT/'data/prompts.json').read_text())
  tools=json.loads((ROOT/'data/catalogue.json').read_text())
  self.assertGreaterEqual(len(prompts),4)
  names={x['name'] for x in tools};ids=set()
  for p in prompts:
   self.assertIn(p['tool'],names);self.assertNotIn(p['id'],ids);ids.add(p['id'])
   self.assertGreater(len(p['text']),250);self.assertRegex(p['text'],'autoriz|confirmação')
   self.assertTrue(p['source'].startswith('https://'))
   self.assertNotIn('curl ',p['text']);self.assertNotIn('sudo ',p['text'])
   home=(ROOT/'index.html').read_text();self.assertIn(p['id'],home)
  for slug in ['hermes-agent','opencode','morphic']:
   page=(ROOT/'ferramentas'/slug/'index.html').read_text()
   self.assertIn('Prompts para configurar com cuidado',page)
   self.assertIn('data-copy-prompt',page);self.assertIn('assets/prompts.js',page)
 def test_prompt_ui_is_progressive_and_not_executable(self):
  home=(ROOT/'index.html').read_text();js=(ROOT/'assets/prompts.js').read_text()
  self.assertIn('id="prompt-dialog"',home);self.assertIn('id="prompt-preview-text"',home)
  self.assertIn('aria-live="polite"',home)
  self.assertNotIn('fetch(',js);self.assertNotIn('eval(',js)
  self.assertIn('clipboard.writeText',js)
