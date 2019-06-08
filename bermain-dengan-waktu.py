try:
    from datetime import datetime
    import time, os
except:
    print("Module datetime & time tidak ada")

class Alarm:

    jumlah_alarm = 0
    alarm_name = "Alarm-"
    
    def __init__(self, input_jam, input_menit):

        self.waktu_sekarang = datetime.now()
        self.jam_awal = self.waktu_sekarang.hour
        self.menit_awal = self.waktu_sekarang.minute

        self.jam_akhir = input_jam
        self.menit_akhir = input_menit

        Alarm.jumlah_alarm += 1
        self.nama = Alarm.alarm_name + str(Alarm.jumlah_alarm)
        print('berhasil dibuat')
    
    def waktu_berjalan(self, pengaturan=False):

        if pengaturan:
            while(1):
                
                os.system("clear")

                jam_sekarang = datetime.now().hour
                menit_sekarang = datetime.now().minute

                print("Waktu sekarang : {}-{}".format(jam_sekarang, menit_sekarang))
                print("Waktu akhir    : {}-{}".format(self.jam_akhir, self.menit_akhir))

                if jam_sekarang == self.jam_akhir and menit_sekarang == self.menit_akhir:
                    break

                time.sleep(1)
            
            os.system('clear')
            print(self.nama + ' Selesai')

alarm1 = Alarm(13, 50)
alarm2 = Alarm(14, 0)

alarm1.waktu_berjalan(True)
alarm2.waktu_berjalan(True)