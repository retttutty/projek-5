import time
import random

def tampilkan_intro():
    """Menampilkan intro game"""
    print("\n" + "="*60)
    print("★ DUNGEON NYC: MISI PEMBUNUH BAYARAN ★".center(60))
    print("="*60)
    time.sleep(1)
    print("\n📍 Lokasi: Bawah Tanah New York City")
    print("🎭 Karakter: GWEN - Pembunuh Bayaran Elit")
    print("💪 Kemampuan: Akrobatik Luar Biasa & Refleks Tinggi\n")
    time.sleep(1)

def cerita_awal():
    """Menceritakan latar belakang game"""
    print("-" * 60)
    print("CERITA:")
    print("-" * 60)
    print("""
Gwen adalah pembunuh bayaran paling dicari di kota. Suatu malam,
ketika melakukan infiltrasi di gedung pencakar langit Manhattan,
dia terjebak dalam portal misterius dan tersedot ke bawah tanah
kota New York yang penuh dengan PENJAHAT SUPER yang berbahaya!

Dungeon ini adalah markas rahasia penjahat-penjahat terkuat kota.
Gwen harus mengalahkan mereka dan menemukan cara keluar dari sini
untuk bisa menyelesaikan misinya.

Keberuntungan ada di sisinya - refleksnya yang tajam adalah senjata utamanya.
""")
    time.sleep(2)

def sistem_pertempuran(nama_musuh, kesehatan_musuh, kekuatan_musuh):
    """Sistem pertempuran dengan penjahat"""
    kesehatan_gwen = 100
    kekuatan_gwen = 85
    ronde = 1
    
    print("\n" + "🔥" * 30)
    print(f"⚔️  PERTEMPURAN: Melawan {nama_musuh}!".center(60))
    print("🔥" * 30 + "\n")
    time.sleep(1)
    
    while kesehatan_gwen > 0 and kesehatan_musuh > 0:
        print(f"\n--- RONDE {ronde} ---")
        print(f"❤️  Gwen: {kesehatan_gwen} HP  vs  ❤️  {nama_musuh}: {kesehatan_musuh} HP\n")
        
        print("Pilihan Serangan:")
        print("1. PUKULAN CEPAT (70% berhasil, 15-20 damage)")
        print("2. TENDANGAN AKROBATIK (60% berhasil, 25-35 damage)")
        print("3. MENGELAK & KONTRA (50% berhasil, 30-45 damage)\n")
        
        pilihan = input("Pilih taktik (1/2/3): ").strip()
        
        # Serangan Gwen
        serangan_berhasil = False
        damage = 0
        
        if pilihan == "1":
            if random.random() < 0.7:
                damage = random.randint(15, 20)
                serangan_berhasil = True
                print(f"✅ Pukulan cepat Gwen mengenai! Damage: {damage}")
            else:
                print("❌ Pukulan meleset!")
        
        elif pilihan == "2":
            if random.random() < 0.6:
                damage = random.randint(25, 35)
                serangan_berhasil = True
                print(f"✅ Tendangan akrobatik spektakuler! Damage: {damage}")
            else:
                print("❌ {nama_musuh} mengelak dari tendangan!")
        
        elif pilihan == "3":
            if random.random() < 0.5:
                damage = random.randint(30, 45)
                serangan_berhasil = True
                print(f"✅ Gwen mengelak & memberikan counter serangan! Damage: {damage}")
            else:
                print("❌ Mengelak gagal, Gwen terkena pukulan!")
                kesehatan_gwen -= 10
        
        else:
            print("❌ Pilihan tidak valid!")
            continue
        
        if serangan_berhasil:
            kesehatan_musuh -= damage
        
        time.sleep(1)
        
        # Serangan Musuh
        if kesehatan_musuh > 0:
            damage_musuh = random.randint(kekuatan_musuh - 10, kekuatan_musuh)
            print(f"\n⚡ {nama_musuh} menyerang balik! Damage: {damage_musuh}")
            kesehatan_gwen -= damage_musuh
            time.sleep(1)
        
        ronde += 1
    
    print("\n" + "="*60)
    if kesehatan_gwen > 0:
        print("🏆 KEMENANGAN! Gwen mengalahkan musuh!".center(60))
        print("="*60)
        return True
    else:
        print("💀 KEKALAHAN! Gwen tewas dalam pertempuran!".center(60))
        print("="*60)
        return False

def jalur_times_square():
    """Jalur menuju Times Square"""
    print("\n" + "★" * 30)
    print("📍 JALUR 1: TIMES SQUARE".center(60))
    print("★" * 30 + "\n")
    
    print("""
Gwen menemukan terowongan yang mengarah ke bawah Times Square.
Suara musik yang berisik terdengar dari jauh. 
Di depannya, cahaya neón berwarna-warni dari papan iklan holografik.

Tiba-tiba, dari dalam asap merah cerah muncul sosok menakutkan!
Ini adalah DJ VENOM, penjahat super dengan kemampuan mengontrol
suara dan gelombang sonik yang dapat merobohkan bangunan!

"MUSIK ADALAH SENJATAKU!" teriak DJ Venom.
""")
    time.sleep(2)
    
    # Pertempuran dengan DJ Venom
    if sistem_pertempuran("DJ VENOM", 80, 70):
        print("""
Setelah mengalahkan DJ Venom, Gwen menemukan akses ke level berikutnya.
Dia menemukan KUNCI PERAK yang bersinar di tangan musuh yang kalah.

Dengan kunci ini, Gwen dapat membuka pintu menuju exit dungeon!
""")
        return True
    else:
        return False

def jalur_jembatan_williamsburg():
    """Jalur menuju Jembatan Williamsburg"""
    print("\n" + "★" * 30)
    print("📍 JALUR 2: JEMBATAN WILLIAMSBURG".center(60))
    print("★" * 30 + "\n")
    
    print("""
Gwen menelusuri terowongan berbatu menuju bawah Jembatan Williamsburg.
Angin dingin bertiup dari pipa-pipa baja yang berkarat.
Genangan air berwarna aneh membentuk kolam di sekitar area.

Dari balik tiang-tiang baja, muncul IRON SPIDER, penjahat super
dengan armor baja titanium dan kekuatan luar biasa!

"KAMU TIDAK AKAN LOLOS DARI SINI!" suara berat terdengar dari dalam helm.
Mata merah berkilau mengawasi Gwen dengan penuh ancaman.
""")
    time.sleep(2)
    
    # Pertempuran dengan Iron Spider
    if sistem_pertempuran("IRON SPIDER", 100, 80):
        print("""
Dengan usaha maksimal, Gwen berhasil menembus armor Iron Spider.
Dia menemukan KUNCI EMAS yang tertanam di dada musuh yang tumbang.

Kunci emas ini adalah pembuka pintu pertama menuju kebebasan!
""")
        return True
    else:
        return False

def pilihan_jalur():
    """Menampilkan pilihan jalur dan menangani keputusan pemain"""
    print("\n" + "="*60)
    print("PEMILIHAN JALUR".center(60))
    print("="*60 + "\n")
    
    print("""
Gwen sampai di persimpangan dalam dungeon. Dua jalur terbuka di hadapannya:

🔴 JALUR 1: KE ARAH TIMES SQUARE
   - Terdengar musik dan cahaya dari atas
   - Risiko: Penjahat dengan kemampuan suara
   
🟦 JALUR 2: KE ARAH JEMBATAN WILLIAMSBURG  
   - Terbuat dari besi dan baja tua
   - Risiko: Penjahat dengan armor logam
""")
    
    while True:
        print("\nPilih jalur mana yang akan diambil?")
        print("1. TIMES SQUARE")
        print("2. JEMBATAN WILLIAMSBURG")
        
        pilihan = input("\nMasukkan pilihan (1/2): ").strip()
        
        if pilihan == "1":
            print("\n✓ Gwen memilih untuk menuju Times Square...")
            time.sleep(1)
            return jalur_times_square()
        
        elif pilihan == "2":
            print("\n✓ Gwen memilih untuk menuju Jembatan Williamsburg...")
            time.sleep(1)
            return jalur_jembatan_williamsburg()
        
        else:
            print("❌ Pilihan tidak valid! Silahkan masukkan 1 atau 2.")

def game_selesai(kemenangan):
    """Menampilkan ending game"""
    print("\n" + "="*60)
    
    if kemenangan:
        print("🏆 SELAMAT! ANDA MENANG! 🏆".center(60))
        print("="*60)
        print("""
Gwen berhasil mengalahkan penjahat dan mendapatkan kunci untuk keluar!
Dia kemudian berhasil melarikan diri dari dungeon bawah tanah.

Kembali ke permukaan New York City, Gwen menyelesaikan misinya
dan mendapatkan bayaran sebesar $500.000!

Setidaknya, hari ini dia hidup untuk membunuh lagi...

        ╔════════════════════════════════════════════════════════════╗
        ║        TERIMA KASIH TELAH BERMAIN DUNGEON NYC!             ║
        ╚════════════════════════════════════════════════════════════╝
""")
    else:
        print("💀 GAME OVER! ANDA KALAH! 💀".center(60))
        print("="*60)
        print("""
Gwen tidak berhasil mengalahkan penjahat. Dia tewas dalam pertempuran,
dan tubuhnya hilang di kegelapan dungeon bawah tanah.

Misi gagal.
Bayaran tidak akan diterima.

Petualangan Gwen berakhir di sini...

        ╔════════════════════════════════════════════════════════════╗
        ║        TERIMA KASIH TELAH BERMAIN DUNGEON NYC!             ║
        ╚════════════════════════════════════════════════════════════╝
""")
    print("="*60 + "\n")

def game_utama():
    """Fungsi utama game"""
    tampilkan_intro()
    
    nama = input("🎭 Masukkan nama GWEN Anda (atau tekan Enter untuk nama default): ").strip()
    if not nama:
        nama = "GWEN"
    
    print(f"\n✓ Selamat datang, {nama}!\n")
    time.sleep(1)
    
    cerita_awal()
    
    # Pemilihan jalur menggunakan if-else
    kemenangan = pilihan_jalur()
    
    # Determasi ending
    game_selesai(kemenangan)
    
    # Tanya apakah ingin bermain lagi
    while True:
        main_lagi = input("Apakah Anda ingin bermain lagi? (y/n): ").strip().lower()
        if main_lagi == 'y':
            print("\n\n")
            game_utama()
            break
        elif main_lagi == 'n':
            print("\n👋 Terima kasih sudah bermain! Sampai jumpa lagi!\n")
            break
        else:
            print("❌ Masukkan 'y' atau 'n'!")

if __name__ == "__main__":
    game_utama()
