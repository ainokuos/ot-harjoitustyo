import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.1")
    
    def test_saldo_vahenee_oikein_jos_rahaa(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")
    
    def test_saldo_ei_muutu_jos_ei_rahaa(self):
        self.maksukortti.ota_rahaa(15)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_palauttaa_true_jos_raha_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)
    
    def test_palauttaa_false_jos_raha_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(20), False)

    