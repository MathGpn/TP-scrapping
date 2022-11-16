from scrapper import Scrap
import unittest

#les tests sont effectués pour la vidéo de Pierre Niney et HugoDécrypte

class TestScrapMethods(unittest.TestCase):

    def test_title(self : object):
        obj = Scrap("https://www.youtube.com/watch?v=fmsoym8I-3o&t=2363s")
        expected = "Pierre Niney : L’interview face cachée par HugoDécrypte"
        self.assertEqual(obj.get_title(), expected)

    def test_auteur(self : object):
        obj = Scrap("https://www.youtube.com/watch?v=fmsoym8I-3o&t=2363s")
        expected = "HugoDécrypte"
        self.assertEqual(obj.get_author(), expected)

    def test_like(self : object):
        obj = Scrap("https://www.youtube.com/watch?v=fmsoym8I-3o&t=2363s")
        print("Testons la méthode get_likes :", obj.get_likes())
    #     self.assertEqual(Scrap.get_likes(self), expected)

    def test_description(self : object):
        obj = Scrap("https://www.youtube.com/watch?v=fmsoym8I-3o&t=2363s")
        print("Testons la méthode get_description :", obj.get_description())

    # def test_links(self : object):
    #     print("Testons la méthode get_description :", Scrap.get_links(self, ))

    def test_id(self : object):
        obj = Scrap("https://www.youtube.com/watch?v=fmsoym8I-3o&t=2363s")
        expected = "fmsoym8I-3o"
        self.assertEqual(obj.get_video_id(), expected)

    def test_comms(self : object):
        obj = Scrap("https://www.youtube.com/watch?v=fmsoym8I-3o&t=2363s")
        print("Testons la méthode get_commentaires :", obj.get_comms())

#python3 -m unittest tests.py
#coverage run -m unittest tests.py
#pytest --cov=. tests.py