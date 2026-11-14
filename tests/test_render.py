import unittest

from app.render import render_greeting


class RenderTest(unittest.TestCase):
    def test_plain(self):
        self.assertEqual(render_greeting("Ada"), "Hello Ada!")

    def test_escapes_markup(self):
        self.assertEqual(render_greeting("<b>"), "Hello &lt;b&gt;!")


if __name__ == "__main__":
    unittest.main()
