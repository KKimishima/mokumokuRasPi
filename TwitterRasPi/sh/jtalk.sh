#!/bin/sh
tempf = /temp/jtalk.wav
htsvo = "/usr/share/hts-voice/nitech-jp-atr503-m001i/nitech_jp_atr503_m001.htsvoice"

echo "$1" | open_jtalk \
-x /var/lib/mecab/dic/open-jtalk/naist-jdic/ \
-m $htsvo \
-ow $tempf
aplay --quiet $tempf
rm $tempf
