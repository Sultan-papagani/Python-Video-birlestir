# Python-Video-birlestir
bu basit kod ile iki videoyu sürükle bırak şeklinde birleştirin (bir video ses, diğeri video olmalı)

youtubeden indirdiğiniz 1080p ses içermeyen video ve sadece ses içeren .webm dosyalarını sürükle bırak şeklinde birleştirin
veya ben yazarım elimle diyosanız burda;

ffmpeg -i %video1% -i %video2% -c:v copy -c:a aac %çıkışAd%

bence sürükle bırak daha kolay

