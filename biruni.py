from logging import exception
import sys
import random

class Nucleus:
    def __init__(self):
        self.encoding = 'utf-8'
        self.nucleotids_split_size = 2
        self.nucleotids = {
            "00": "A",
            "11": "T",
            "01": "G",
            "10": "C"
        }


        self.codon_map = {
            "GCT": "Alanine", "GCC": "Alanine", "GCA": "Alanine", "GCG": "Alanine",
            "CGT": "Arginine", "CGC": "Arginine", "CGA": "Arginine", "CGG": "Arginine",
            "AGA": "Arginine", "AGG": "Arginine",
            "AAT": "Asparagine", "AAC": "Asparagine",
            "GAT": "Aspartate", "GAC": "Aspartate",
            "TGT": "Cysteine", "TGC": "Cysteine",
            "CAA": "Glutamine", "CAG": "Glutamine",
            "GAA": "Glutamate", "GAG": "Glutamate",
            "GGT": "Glycine", "GGC": "Glycine", "GGA": "Glycine", "GGG": "Glycine",
            "CAT": "Histidine", "CAC": "Histidine",
            "ATT": "Isoleucine", "ATC": "Isoleucine", "ATA": "Isoleucine",
            "CTT": "Leucine", "CTC": "Leucine", "CTA": "Leucine", "CTG": "Leucine",
            "TTA": "Leucine", "TTG": "Leucine",
            "AAA": "Lysine", "AAG": "Lysine",
            "ATG": "Methionine",
            "TTT": "Phenylalanine", "TTC": "Phenylalanine",
            "CCT": "Proline", "CCC": "Proline", "CCA": "Proline", "CCG": "Proline",
            "TCT": "Serine", "TCC": "Serine", "TCA": "Serine", "TCG": "Serine",
            "AGT": "Serine", "AGC": "Serine",
            "ACT": "Threonine", "ACC": "Threonine", "ACA": "Threonine", "ACG": "Threonine",
            "TGG": "Tryptophan",
            "TAT": "Tyrosine", "TAC": "Tyrosine",
            "GTT": "Valine", "GTC": "Valine", "GTA": "Valine", "GTG": "Valine",
            "TAA": "STOP", "TGA": "STOP", "TAG": "STOP",
            'AAN': "STOP", 'ATN': "STOP", 'AGN': "STOP", 'ACN': "STOP",
            'ANA': "STOP", 'ANT': "STOP", 'ANG': "STOP", 'ANC': "STOP", 'ANN': "STOP",
            'TAN': "STOP", 'TTN': "STOP", 'TGN': "STOP", 'TCN': "STOP",
            'TNA': "STOP", 'TNT': "STOP", 'TNG': "STOP", 'TNC': "STOP", 'TNN': "STOP",
            'GAN': "STOP", 'GTN': "STOP", 'GGN': "STOP", 'GCN': "STOP",
            'GNA': "STOP", 'GNT': "STOP", 'GNG': "STOP", 'GNC': "STOP", 'GNN': "STOP",
            'CAN': "STOP", 'CTN': "STOP", 'CGN': "STOP", 'CCN': "STOP",
            'CNA': "STOP", 'CNT': "STOP", 'CNG': "STOP", 'CNC': "STOP", 'CNN': "STOP",
            'NAA': "STOP", 'NAT': "STOP", 'NAG': "STOP", 'NAC': "STOP", 'NAN': "STOP",
            'NTA': "STOP", 'NTT': "STOP", 'NTG': "STOP", 'NTC': "STOP", 'NTN': "STOP",
            'NGA': "STOP", 'NGT': "STOP", 'NGG': "STOP", 'NGC': "STOP", 'NGN': "STOP",
            'NCA': "STOP", 'NCT': "STOP", 'NCG': "STOP", 'NCC': "STOP", 'NCN': "STOP",
            'NNA': "STOP", 'NNT': "STOP", 'NNG': "STOP", 'NNC': "STOP", 'NNN': "STOP"
        }

        self.crypted_codon = {
            'GCT': 'ܧ', 'GCC': 'ᄃ', 'GCA': 'φ', 'GCG': 'А',
            'CGT': '፺', 'CGC': 'ճ', 'CGA': 'ઈ', 'CGG': 'ਢ',
            'AGA': 'ۙ', 'AGG': 'ર', 'AAT': '๗', 'AAC': 'ϟ',
            'GAT': '૿', 'GAC': 'ᄜ', 'TGT': 'ծ', 'TGC': '˾',
            'CAA': 'ᄹ', 'CAG': 'ċ', 'GAA': 'Ձ', 'GAG': '୩',
            'GGT': 'ϳ', 'GGC': 'ǝ', 'GGA': '+', 'GGG': 'ਈ',
            'CAT': 'Ⴀ', 'CAC': 'ᄥ', 'ATT': 'ᅮ', 'ATC': 'ࢌ',
            'ATA': '˟', 'CTT': 'ᄶ', 'CTC': '৭', 'CTA': '၇',
            'CTG': 'ƞ', 'TTA': 'Ÿ', 'TTG': 'ࡪ', 'AAA': 'ྒ',
            'AAG': 'ޯ', 'ATG': 'қ', 'TTT': 'ຕ', 'TTC': 'Ь',
            'CCT': 'ტ', 'CCC': 'উ', 'CCA': 'ת', 'CCG': '࢘',
            'TCT': '܄', 'TCC': 'ౄ', 'TCA': '©', 'TCG': '୭',
            'AGT': 'බ', 'AGC': 'స', 'ACT': '֤', 'ACC': 'ฃ',
            'ACA': '࣐', 'ACG': 'ș', 'TGG': 'ௗ', 'TAT': '̘',
            'TAC': 'ሸ', 'GTT': '{', 'GTC': 'ዅ', 'GTA': 'ࠎ',
            'GTG': '߰', 'TAA': '४', 'TGA': 'п', 'TAG': 'Ͻ',
            'AAN': '፝', 'ATN': 'ന', 'AGN': 'ࠣ', 'ACN': 'ଢ଼',
            'ANA': '৮', 'ANT': 'ؾ', 'ANG': 'ଵ', 'ANC': 'জ',
            'ANN': 'ী', 'TAN': 'ܤ', 'TTN': 'Ǡ', 'TGN': 'મ',
            'TCN': 'ߨ', 'TNA': 'ࡏ', 'TNT': 'ϧ', 'TNG': 'ჰ',
            'TNC': '࿑', 'TNN': 'Ͱ', 'GAN': 'ྊ', 'GTN': '༸',
            'GGN': 'ᆅ', 'GCN': 'ϰ', 'GNA': '߷', 'GNT': 's',
            'GNG': 'ѥ', 'GNC': 'ܵ', 'GNN': 'Ϋ', 'CAN': 'Ͷ',
            'CTN': 'ዌ', 'CGN': 'ξ', 'CCN': 'ଅ', 'CNA': 'ّ',
            'CNT': 'ዀ', 'CNG': '̯', 'CNC': '֦', 'CNN': 'ൖ',
            'NAA': 'ጠ', 'NAT': 'ॠ', 'NAG': 'ࡔ', 'NAC': 'ሽ',
            'NAN': 'ৢ', 'NTA': 'Ȏ', 'NTT': 'Ҕ', 'NTG': 'ன',
            'NTC': 'ो', 'NTN': 'օ', 'NGA': 'У', 'NGT': 'ႜ',
            'NGG': 'ෙ', 'NGC': 'ጹ', 'NGN': 'ᅩ', 'NCA': 'Ⴋ',
            'NCT': 'ɗ', 'NCG': 'ህ', 'NCC': 'ͳ', 'NCN': 'Ê',
            'NNA': 'ܹ', 'NNT': '˯', 'NNG': 'ː', 'NNC': 'Ǥ',
            'NNN': 'ߪ'
        }

    def makeDna(self, rawText):
        if type(rawText) == int:
            rawText = str(rawText)
        elif type(rawText) == float:
            rawText = str(rawText)
        elif type(rawText) == bool:
            rawText = str(rawText)
        elif type(rawText) == list:
            rawText = ''.join(rawText) 

        for i in rawText:
            if i != "0" and i != "1":
                raise Exception("Hata: {} karakteri dönüştürülebilir formatta bir değişken değildir kabul görenler ['1','0']".format(i))

        counter = 1
        splitted_code = []
        splitting = ""
        for i in rawText:
            if self.nucleotids_split_size == counter:
                splitting += i
                splitted_code.append(splitting)
                splitting = ""
                counter = 1
            else:
                splitting += i
                counter += 1

        remake_dna = []
        for i in splitted_code:
            remake_dna.append(self.nucleotids[i])
        return remake_dna

    def dnaTrinucleotid(self, dna):
        if type(dna) != list:
            raise exception("liste tipi veri lazım")
        
        # Eğer uzunluk 3'e bölünmüyorsa, 'N' ile doldur
        if len(dna) % 3 != 0:
            for _ in range(3 - (len(dna) % 3)):
                dna.append("N")
        
        counter = 1
        splitted_code = []
        splitting = ""
        for i in dna:
            if 3 == counter:
                splitting += i
                splitted_code.append(splitting)
                splitting = ""
                counter = 1
            else:
                splitting += i
                counter += 1
        return splitted_code

    def trinucleotidCrypt(self, trinucleotid):
        if type(trinucleotid) != list:
            raise exception("liste tipi veri lazım")
        context = []
        for i in trinucleotid:
            val = self.crypted_codon.get(i, "?")
            context.append(val)
        return context

    def cryptToTrinucleotid(self, crypted):
        if type(crypted) == str:
            l = []
            for i in crypted:
                l.append(i)
            crypted = l
        elif type(crypted) != list:
            raise exception("liste tipi veri lazım")

        autoDeCryptedCodon = {}
        for i in self.crypted_codon:
            autoDeCryptedCodon[self.crypted_codon[i]] = i

        context = []
        for i in crypted:
            context.append(autoDeCryptedCodon.get(i, "NNN"))
        return context

    def trinucleotidToDna(self, trinucleotid):
        if type(trinucleotid) != list:
            raise exception("liste tipi veri lazım")
        redna = []
        for i in trinucleotid:
            for k in i:
                if k != "N":
                    redna.append(k)
        return redna

    def dnaToBinary(self, dna):
        if type(dna) != list:
            raise exception("liste tipi veri lazım")
        
        reNuc = {}
        for i in self.nucleotids:
            reNuc[self.nucleotids[i]] = i
        
        context = []
        lang = ""
        for i in dna:
            context.append(reNuc[i])
            lang += reNuc[i]
        
        binary = []
        binEight = ""
        
        # --- FIX IS HERE ---
        # Önceki mantık hatasını düzelttik:
        # Önce karakteri ekle, sonra 8 oldu mu diye bak.
        for l in lang:
            binEight += l
            if len(binEight) == 8:
                binary.append(binEight)
                binEight = ""
        
        return binary

    def TextToBinary(self, text):
        if type(text) == list:
            text = ' '.join(text)
        
        byte_data = text.encode(self.encoding)
        binary_string = ' '.join(format(byte, '08b') for byte in byte_data)
        binary_array = binary_string.split(' ')
        
        return binary_array

    def BinaryToText(self, binary):
        if type(binary) == list:
            binary = ' '.join(binary)
        
        binary_array = binary.split(' ')
        byte_array = []
        for i in binary_array:
            if i and len(i) == 8: # Sadece tam 8 bitlik parçaları al
                try:
                    byte_array.append(int(i, 2))
                except ValueError:
                    pass

        byte_data = bytes(byte_array)
        text = byte_data.decode(self.encoding, errors='replace')
        return text

    def engine_runner_oneline(self, text):
        binary = self.TextToBinary(text)
        dna = self.makeDna(binary)
        trinucleotid = self.dnaTrinucleotid(dna)
        crypted = self.trinucleotidCrypt(trinucleotid)
        return crypted

    def looped_engine_runner(self, text, loop=1):
        for i in range(loop):
            text = self.engine_runner_oneline(text)
        return text

    # --- YENİ EKLENEN FONKSİYONLAR ---

    def decode_engine_runner(self, crypted_text):
        """Tek katmanlı çözme işlemi yapar (Şifreli Sembol Listesi -> Metin)"""
        decrypte = self.cryptToTrinucleotid(crypted=crypted_text)
        decrypte = self.trinucleotidToDna(trinucleotid=decrypte)
        decrypte = self.dnaToBinary(dna=decrypte)
        final_text = self.BinaryToText(binary=decrypte)
        return final_text

    def looped_decode_engine_runner(self, crypted_text, loop=1):
        """Döngülü şifrelemeyi çözer (Loop sayısı kadar geri gider)"""
        current_data = crypted_text
        for i in range(loop):
            decoded = self.decode_engine_runner(current_data)
            
            # Eğer son döngü değilse, çıkan sonuç bir önceki katmanın şifreli halidir.
            # TextToBinary fonksiyonu listeleri boşlukla birleştirdiği için (' '.join),
            # bir sonraki adıma geçmeden önce stringi tekrar listeye çevirmeliyiz.
            if i < loop - 1:
                current_data = decoded.split(' ')
            else:
                # Son adımda elde edilen veri orijinal metindir (string).
                current_data = decoded
                
        return current_data


# --- TEST ---
if __name__ == "__main__":
    oxi = Nucleus() 

    context = "merhaba merhaba osurduğum çözemedimşimdi ölümnün elinde olduğunu bilmeyen gey 76 !'ˆ+%&/()=" 

    print("--- Şifreleme Başlıyor (Loop=3) ---")
    wog = oxi.looped_engine_runner(text=context, loop=3)
    print(f"Looplu Şifreli Veri (İlk 5 öğe): {wog[:5]}")
    print(f"Veri Tipi: {type(wog)}")
    print(f"Uzunluk: {len(wog)}")

    print("\n--- Çözme İşlemi Başlıyor (Loop=3) ---")
    # looped_decode_engine_runner kullanımı
    decoded_text = oxi.looped_decode_engine_runner(crypted_text=wog, loop=3)

    print("\n--- SONUÇ ---")
    print(f"Orijinal: {context}")
    print(f"Çözülen : {decoded_text}")
    
    if context == decoded_text:
        print("\n✅ BAŞARILI: Döngülü şifreleme başarıyla çözüldü!")
    else:
        print("\n❌ HATA: Girdi ve Çıktı farklı.")


