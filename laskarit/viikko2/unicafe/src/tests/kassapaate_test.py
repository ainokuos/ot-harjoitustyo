import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    

    def test_oikea_maara_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_ei_lounaita_alussa(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_kateisella_osto_toimii(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_syo_maukkaasti_kateisella_osto_toimii(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_edullisesti_vaihtoraha_oikea(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
    
    def test_maukkaasti_vaihtoraha_oikea(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
    
    def test_maukkaasti_maara_nousee(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_edullisesti_maara_nousee(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_ei_riittavasti_edullisella_kassa(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_ei_riittavasti_edullisella_maara(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset,0)
    
    def test_ei_riittavasti_edullisella_vaihoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_ei_riittavasti_maukkaalla_kassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_ei_riittavasti_maukkaalla_maara(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat,0)
    
    def test_ei_riittavasti_maukkaalla_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)
    
    def test_korttiosto_saldo_toimii_edullisella(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo,260)
    
    def test_korttiosto_kassapaate_toimii_edullisella(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)
        
    def test_korttiosto_edulliset_maara_kasvaa(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_korttiosto_edulliset_saldo_ei_muutu(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo,100)
    
    def test_korttiosto_kassapaate_ei_toimi_edullisella(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
        
    def test_korttiosto_edulliset_maara_ei_muutu(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_korttiosto_saldo_toimii_maukkaalla(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo,100)
    
    def test_korttiosto_kassapaate_toimii_maukkaalla(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)
        
    def test_korttiosto_maukkaat_maara_kasvaa(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_korttiosto_maukkaat_saldo_ei_muutu(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo,100)
    
    def test_korttiosto_kassapaate_ei_toimi_maukkaalla(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
        
    def test_korttiosto_maukkaat_maara_ei_muutu(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassan_saldo_ei_muutu_maukkaalla(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_saldo_ei_muutu_edullisella(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_toimii_kortille(self):
        kortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(kortti, 500)
        self.assertEqual(kortti.saldo, 1000)

    def test_lataa_rahaa_toimii_kassaan(self):
        kortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(kortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)
    
    def test_lataa_kortille_ei_toimi_negatiivisella(self):
        kortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(kortti, -100)
        self.assertEqual(kortti.saldo, 500)