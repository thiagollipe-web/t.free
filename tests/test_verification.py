"""Keep Google ownership verification in the generated homepage."""
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TAG='<meta name="google-site-verification" content="r_koc_P8kwNXvFAWI8uSWSY2hRLDad6iovGLp8sZAhM" />'
class VerificationTests(unittest.TestCase):
 def test_home_and_source_keep_exact_verification_in_head(self):
  for filename in ('index.html','templates/base.html'):
   text=(ROOT/filename).read_text()
   self.assertEqual(text.count(TAG),1,filename)
   self.assertIn(TAG,text.split('</head>',1)[0],filename)
   self.assertEqual(text.count('name="google-site-verification"'),1,filename)
if __name__=='__main__':unittest.main()
