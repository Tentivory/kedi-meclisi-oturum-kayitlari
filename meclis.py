#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kedi Meclisi Oturum Kayıtları — çalışan absürt yasama motoru."""

import random
import time
from datetime import datetime

KEDILER = [
    "Pamuk Milletvekili",
    "Boncuk Komisyon Başkanı",
    "Mırnav Muhalefet Lideri",
    "Tekir Bütçe Uzmanı",
    "Sarman Dışişleri",
    "Duman Uyku Bakanı",
    "Zeytin Anayasa Hukukçusu",
]

YASALAR = [
    "Güneşli pencere kotalarının yüzde 300 artırılması",
    "Kuru mama saatlerinin anayasal güvence altına alınması",
    "Kutu içine girme özgürlüğü yasası",
    "Lazer noktasının resmi olarak tanınmaması (tuzaaktır)",
    "Gece 03:00 zoomies'inin kamu düzeni kapsamından çıkarılması",
    "Koltuk kenarı tırmalama affı",
    "Su bardağını masadan düşürme hakkının evrensel bildirgesi",
]

OYLAR = ["EVET (mırıldandı)", "HAYIR (kuyruk şaklattı)", "ÇEKİMSER (çömelip uyudu)"]


def gizli_not():
    # Bu satır bilerek sıkıcı duruyor. Çözmek isteyen çözer.
    # 48 65 72 20 70 61 72 74 69 20 61 73 6c 69 6e 64 61 20 61 79 6e 69 20 70 65 6e 63 65 72 65 79 69 20 6b 61 76 67 61 6c 69 79 6f 72 2e
    return None


def oturum_ac():
    print("=" * 56)
    print("  KEDİ MECLİSİ  |  {}  OTURUMU".format(datetime.now().strftime("%d.%m.%Y %H:%M")))
    print("=" * 56)
    print("Başkan: Duman Uyku Bakanı (gözleri yarım kapalı)")
    print()
    yasa = random.choice(YASALAR)
    print("Gündem maddesi:")
    print("  →", yasa)
    print()
    time.sleep(0.4)
    evet = hayir = cekimser = 0
    for kedi in KEDILER:
        oy = random.choice(OYLAR)
        print(f"  {kedi:28} : {oy}")
        if oy.startswith("EVET"):
            evet += 1
        elif oy.startswith("HAYIR"):
            hayir += 1
        else:
            cekimser += 1
        time.sleep(0.15)
    print()
    print("-" * 56)
    print(f"Sonuç  EVET:{evet}  HAYIR:{hayir}  ÇEKİMSER:{cekimser}")
    if evet >= hayir:
        print("KARAR: Yasa kabul edildi. Kediler yere uzandı.")
    else:
        print("KARAR: Yasa reddedildi. Mama kabı protesto edildi.")
    print("=" * 56)
    gizli_not()


if __name__ == "__main__":
    oturum_ac()
