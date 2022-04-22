# need gTTS and mpg123
# pip install gTTS
# apt install mpg123

from operator import length_hint
from moviepy import editor
from gtts import gTTS
from mutagen.mp3 import MP3
from PIL import Image
from pathlib import Path
import os

# define variables
message = "NASA, Axiom Space, and SpaceX waved off the undocking opportunity of Axiom Mission 1 from the International Space Station on Tuesday, April 19 due to unfavorable weather conditions for return. The integrated NASA, Axiom Space, and SpaceX teams are continuing to assess the next best opportunity for return of the first private astronaut mission to the orbiting laboratory based on weather conditions and space station operations."
language = 'en'
##message ='İnsan neden uyur? Fiziksel değil ruhani olarak insan neden uyur? Uyandığında güneşi görmek için. Ya uyandığında güneşi görmeyenler? Onlar neden uyur? ​İnsanlar bir gün uyandığında saatlerinin bozulduğunu sandı. Belki de dünyadaki tüm insanların ortak bir düşüncesi olduğunu sandığı son düşünce buydu. ​İnsanlar her gün yukarıda olacağına emin oldukları güneşi o gün yukarıda bulamayınca, günlük yaşanan düzen bozulduğunda ortaya tarihin en büyük kaosu çıkmıştı. Güneş artık yukarıda değildi, güneş artık gözle görülmeyi bırakın, hiçbir teleskopla gözükmüyordu. Bilim insanları bunun imkânsız olduğunu savunup, güneşin ortadan kaybolduğu anda dünyanın donarak yanacağının, uzayın derinliklerinde kaybolacağını bildikleri halde hiçbir şeyin olmamasına anlam veremiyor, binlerce yıldır doğru bildikleri bilgilerin gözlerinin önünde aynı Güneş gibi kayboluşunu izliyorlardı. Tüm din insanları ise ya dünyanın yok olacağını ya da tanrılarının bizi cezalandırmak için güneşi elimizden aldığını savunuyorlardı. Normal insanlar ise her zamanki gibi sağdan sola savrulup, kaçabilecekleri bir yer varmış gibi şehri terk ediyor veya bağımlı oldukları süpermarketlerdeki tüm ürünleri banka kartlarının midesine indiriyorlardı. ​Günler geçti, güneş yerine gelmedi, hiçbir tanrı bizi cezalandırmadı, bilim hiçbir cevap bulamadı, kaos hiçbir sonuç getirmedi. ​İnsanlar normal yaşantılarını sürdürmeye devam etmek zorunda kaldıklarını fark ettiler. Çünkü yapmayı bildikleri başka hiçbir şey yoktu. İşlerinde çalıştılar, ibadetlerini yaptılar, yemeklerini yediler, kendilerini uyuşturdular ve tekrar uyudular. ​Tekrar uyandılar, yukarıda yine güneş yoktu, yine işlerinde çalıştılar, yine ibadetlerini yaptılar, yine yemeklerini yediler, yine kendilerini uyuşturdular ve tekrar uyudular. ​İnsanlar bu sefer farklı uyandılar. Hayır, Güneş bir anda yerine gelmemişti. Maddesel her şey dün olduğu gibiydi. Değişen sadece insanlardı. Artık yaşanılan bu anlamsızlığa ne dinin ne de bilimin bir sonuç bulamadığını fark ettiler. Bu kadar büyük bir değişimin bir nedeni, bir nedeni olduğu gibi bir sonucu olmalıydı. İnsanlar bölünmeye başladılar. ​Bir kısım insan, Güneşin gözükmediği halde hep orada olduğunu, gözükmediği halde ısı, enerji ve kudret yağdırdığını savundu. Onu görmeyi hak etmediğimizi, onun ise hepimizi gördüğünü ve göreceğini savundu. Onun bizi affedebilmesi ve tekrar kudretini her sabah üstümüzde hissedebilmemiz için adaklar hazırlayıp aleve verdiler. Onlar kendilerine göre önemli olan her şeyi küçük güneşler yaratarak göstermeye çalıştılar.​Diğer kısımdaki insanlar ise Güneşin bir yalan olduğunu, sönerek yok olduğunu, ona ihtiyacımız olmadan yaşanabildiğini, Güneş olmadan her şeyin aynı olduğunu ve onun bir yalan olduğuna inandılar. ​Yeni dinler, yeni teoriler yaratıldı. Hükümetler ise aynı kaldı, bu iki tarafa asla görüş belirtmedi, asla alakalı bir açıklama yapmadı. ​Bir gün, bir grup Güneşe tapan, bir Güneşe ihanet edeni (bu isim güneşe inanmayanlara Güneşe tapanlar tarafından verilmişti) yakarak tarihin belki de en büyük savaşını başlatmıştı. İnsanlar karanlıkta yanan bir diğer insanı gördüklerinde, o ateş onların da yüreğine zıpladı. Aynı bir saman tarlası gibi. ​Sonu gelmeyecek bu gruplaşma ve yıkım, aynı saman tarlası gibi bir anda hararetle yanıp, söndü. ​Artık Güneşe inanmayanların hepsi yok olmuştu, Güneşin ta kendisi gibi. ​Sonra herkes Güneşe tapmaya devam etti. Günlerce ve aylarca süren bu tapmaların sonuç vermediğini, güneşin geri gelmediğini gördüklerinde Güneşe tapanların sayısı gittikçe azaldı. Ancak artık insanlar veya değerli yerler yakılmıyordu. Ve bir gün insanlar tekrar uyandılar, yukarıda yine güneş yoktu, yine işlerinde çalıştılar, yine ibadetlerini yaptılar, yine yemeklerini yediler, yine kendilerini uyuşturdular ve tekrar uyudular.'
##language = 'tr'
file = "file.mp3"

# initialize tts, create mp3 and play
speech = gTTS(text=message, lang=language, slow=False)
speech.save(file)
song = MP3(file)
length = song.info.length
#os.system("mpg123 " + file)

path_images = Path('')
images = list(path_images.glob('*.jpg'))
image_list = list()
for image_name in images:
    image = Image.open(image_name).resize((1920,1080),Image.ANTIALIAS)
    image_list.append(image)

image_list[0].save('temp.gif', save_all=True, append_images = image_list[1:] , duration = length)

video = editor.VideoFileClip('temp.gif')
audio = editor.AudioFileClip('file.mp3')
final_video = video.set_audio(audio)
final_video.write_videofile('test.mp4' ,fps=60)