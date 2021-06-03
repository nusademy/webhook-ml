def check_personality(result):
    if result =='INTJ':
        result = intj(result)
    elif result =='INTP':
        result = intp(result)
    elif result =='INFJ':
        result = infj(result)
    elif result =='INFP':
        result = infp(result)
    elif result =='INTJ':
        result = intj(result)
    elif result == 'ISTJ':
        result = istj(result)
    elif result =='ISFJ':
        result = isfj(result)
    elif result =='ISTP':
        result = istp(result)
    elif result == 'ISFP':
        result = isfp(result)
    elif result == 'ENTJ':
        result = entj(result)
    elif result == 'ENTP':
        result = entp(result)
    elif result == 'ENFJ':
        result = enfj(result)
    elif result == 'ENFP':
        result = enfp(result)
    elif result == 'ESTJ':
        result = estj(result)
    elif result == 'ESFJ':
        result = esfj(result)
    elif result == 'ESTP':
        result = estp(result)
    elif result == 'ESFP':
        result = esfp(result)
    else:
        result = "Saya sekali, tipe kepribadianmu tidak ditemukan!"
    return result

def entj(personality_type):
    if personality_type == 'ENTJ':
        personality_type ='ENTJ (Commaadaasander)'
        personality_def = 'merupakan orang yang cenderung dihormati orang lain sebagai seorang pemimpin dan memiliki keberanian yang tinggi. ENTJ cenderung memastikan setiap orang agar tidak menyimpang dan tetap melakukan tugasnya. Menyukai keteraturan dan struktur yang jelas. Cenderung bisa mencapai potensi maksimal ketika memiliki posisi yang cukup tinggi.'
        job_recommend = 'Pengusaha, Ahli Strategi Perusahaan, Pengacara, Hakim'
        return "Tipe Kepribadianmu adalah " + str(personality_type) + ". Kamu " + str(personality_def) + " Rekomendasi pekerjaan yang cocok untukmu: " + str(job_recommend)
def intj(personality_type):
    if personality_type == 'INTJ':
        personality_type ='INTJ (Architect)'
        personality_def =' Merupakan tipe orang yang tertarik untuk terjun dan menyelesaikan tantangan-tantangan baru. Bekerja dengan kreatifitas serta menghasilkan ide-ide yang unik dan berbeda. Biasanya tertarik untuk memilih peran sebagai orang yang berdampak.'
        job_recommend = 'Manajer Proyek, System Engineer, Strategi Pemasaran, Sistem Analis, Strategi Militer'
        return "Tipe Kepribadianmu adalah " + str(personality_type) + ". Kamu " + str(personality_def) + " Rekomendasi pekerjaan yang cocok untukmu: " + str(job_recommend)
def intp(personality_type):
    if personality_type == 'INTP':
        personality_type ='INTP (Logician)'
        personality_def ='Merupakan tipe orang yang suka bereksplorasi mengenai ide-ide dan posibilitas yang ada. Memiliki rasa ingin tahu yang besar. Orang-orang INTP lebih senang untuk menciptakan pandangan baru dibandingkan mengimplementasikan pekerjaan orang lain.'
        job_recommend = 'Ahli Matematika, Analis, Peneliti, Ilmuwan, Konsultan'
        return "Tipe Kepribadianmu adalah " + str(personality_type) + ". Kamu " + str(personality_def) + " Rekomendasi pekerjaan yang cocok untukmu: " + str(job_recommend)
def infj(personality_type):
    if personality_type == 'INFJ':
        personality_type ='INFJ (Advocate)'
        personality_def ='Lebih cenderung mencari jalan karir yang sesuai dengan prinsip hidup dibandingkan dengan karir yang hanya sekedar berdasar dengan posisi serta menghasilkan uang banyak. Orang dengan tipe INFJ mementingkan arti dari pekerjaan yang dilakukan dan cenderung senang apabila mereka dapat membantu serta bisa mengenal orang lain.'
        job_recommend = 'Konselor, Psikolog, Guru, Pekerja Sosial, Instruktur Yoga, Penulis, Pengacara'
        return "Tipe Kepribadianmu adalah " + str(personality_type) + ". Kamu " + str(personality_def) + " Rekomendasi pekerjaan yang cocok untukmu: " + str(job_recommend)
def infp(personality_type):
    if personality_type == 'INFP':
        personality_type ='INFP (Mediators)'
        personality_def ='Merupakan tipe orang yang tidak suka memiliki pekerjaan yang dapat menyebabkan stress, konflik maupun kompetitif. Memiliki rasa ingin tahu dan ketertarikan dalam mengekspresikan diri sendiri. Ingin memiliki pekerjaan yang bisa berdampak bagi orang lain.'
        job_recommend = 'Penulis, Koreografer, Konselor, Psikolog, Guru, Bidang Kesehatan'
        return "Tipe Kepribadianmu adalah " + str(personality_type) + ". Kamu " + str(personality_def) + " Rekomendasi pekerjaan yang cocok untukmu: " + str(job_recommend)
def istj(personality_type):
    if personality_type == 'ISTJ':
        personality_type ='ISTJ (Logistician)'
        personality_def ='Merupakan tipe orang yang berfokus untuk membangun karir yang stabil dan berpotensi jangka panjang. Lebih cenderung menyukai pekerjaan individu. Ketika harus bekerja dalam tim, orang dengan tipe ISTJ harus memiliki pembagian tugas yang jelas. Lebih mengedepankan fakta dibandingkan perasaan.'
        job_recommend = 'Militer, Pengacara, Hakim, Polisi, Akuntan, Auditor, Manajer Keuangan'
        return "Tipe Kepribadianmu adalah " + str(personality_type) + ". Kamu " + str(personality_def) + " Rekomendasi pekerjaan yang cocok untukmu: " + str(job_recommend)
def isfj(personality_type):
    if personality_type == 'ISFJ':
        personality_type ='ISFJ (Defender)'
        personality_def ='Memiliki ingatan yang baik. Memiliki komitmen dan dedikasi yang baik. Tipe orang ISFJ merasa puas melihat hasil pekerjaannya ketika Ia melihat dampak positif dari hal tersebut. Peka terhadap perasaan orang lain di sekitarnya. Suka membantu orang lain. '
        job_recommend = 'Konselor, Desain Interior, Suster, Guru'
        return "Tipe Kepribadianmu adalah " + str(personality_type) + ". Kamu " + str(personality_def) + " Rekomendasi pekerjaan yang cocok untukmu: " + str(job_recommend)
def istp(personality_type):
    if personality_type == 'ISTP':
        personality_type = 'ISTP (Virtuso)'
        personality_def = 'Menyukai keberagaman dan ketidakpastian dalam karir. Merupakan tipe orang yang tertarik untuk mengetahui lebih dalam bagaimana suatu sistem bekerja. Lingkungan pekerjaan yang sangat teratur membuat orang bertipe ISTP mudah bosan dan lelah. Orang bertipe ISTP menyukai kebebasan.'
        job_recommend = 'Montitor, Teknisi, Desain Grafis, Forensik, Detektif'
        return "Tipe Kepribadianmu adalah " + str(personality_type) + ". Kamu " + str(personality_def) + " Rekomendasi pekerjaan yang cocok untukmu: " + str(job_recommend)
def isfp(personality_type):
    if personality_type == 'ISFP':
        personality_type ='ISFP (Adventurer)'
        personality_def ='Merupakan orang yang lebih mengutamakan kreatifitas dan kebebasan dibandingkan kekayaan dan kekuasaan. ISFP memiliki perspektif yang unik dan membutuhkan fleksibilitas, kesempatan improvisasi. Apapun karir yang dipilih, orang bertipe ISFP bisa menemukan cara untuk membuat hidup terasa lebih indah dan berwarna.'
        job_recommend = 'Pemusik, Fotografer, Atlit Solo, Konsultan, Seniman'
        return "Tipe Kepribadianmu adalah " + str(personality_type) + ". Kamu " + str(personality_def) + " Rekomendasi pekerjaan yang cocok untukmu: " + str(job_recommend)
def entp(personality_type):
    if personality_type == 'ENTP':
        personality_type ='ENTP (Debater)'
        personality_def ='Menyukai produktifitas dan keterlibatan secara mendalam dalam suatu hal. ENTP dapat beradaptasi dalam segala hal sehingga mempermudah orang tersebut dalam memilih karir sesuai passion. Memiliki kemampuan komunikasi yang bagus. Orang bertipe ini sangat menghargai pengetahuan dan pemikiran rasional.'
        job_recommend = 'Pengusaha, Aktor, Pengacara, Psikolog, Ilmuwan, Analis'
        return "Tipe Kepribadianmu adalah " + str(personality_type) + ". Kamu " + str(personality_def) + " Rekomendasi pekerjaan yang cocok untukmu: " + str(job_recommend)
def enfj(personality_type):
    if personality_type == 'ENFJ':
        personality_type ='ENFJ (Protagonist)'
        personality_def ='Suka membantu orang lain. Orang bertipe ENFJ tidak membutuhkan inspirasi maupun kesempatan untuk datang agar mereka bisa melakukan pekerjaan yang bermakna. Tidak susah bagi orang ENFJ untuk mengekspresikan dirinya secara kreatif namun tetap jujur. Pekerjaan yang menuntut dapat membuat orang tersebut mudah jenuh.'
        job_recommend = 'Guru, Konselur, HR, Koordinator, Politikus'
        return "Tipe Kepribadianmu adalah " + str(personality_type) + ". Kamu " + str(personality_def) + " Rekomendasi pekerjaan yang cocok untukmu: " + str(job_recommend)
def enfp(personality_type):
    if personality_type == 'ENFP':
        personality_type ='ENFP'
        personality_def ='Merupakan tipe orang yang suka dengan hal baru dan tertarik dengan banyak hal. Orang bertipe ENFP memiliki kemampuan untuk membangun koneksi dan kemampuan untuk beradaptasi dalam hal berkomunikasi. ENFP dapat melihat suatu hal dari berbagai perspektif dengan berbagai pendekatan yang berbeda. '
        job_recommend = 'Analis, Penulis, Jurnalis, Aktor, Konsultan, Pengusaha'
        return "Tipe Kepribadianmu adalah " + str(personality_type) + ". Kamu " + str(personality_def) + " Rekomendasi pekerjaan yang cocok untukmu: " + str(job_recommend)
def estj(personality_type):
    if personality_type == 'ESTJ':
        personality_type ='ESTJ (Executive)'
        personality_def ='Merupakan tipe orang yang menghargai tradisi, stabilitas, dan jaminan. Tergolong orang yang setia, sehingga cenderung untuk tinggal dalam satu pekerjaan yang sama selama beberapa saat. Orang di sekitar ESTJ menganggap orang ini termasuk orang yang patut diteladani. Orang bertipe ESTJ dianggap sebagai manajer yang cukup efektif.'
        job_recommend = 'Penegak Hukum, Dokter, Auditor, Bisnis, Sales, Militer'
        return "Tipe Kepribadianmu adalah " + str(personality_type) + ". Kamu " + str(personality_def) + " Rekomendasi pekerjaan yang cocok untukmu: " + str(job_recommend)
def esfj(personality_type):
    if personality_type == 'ESFJ':
        personality_type ='ESFJ (Consul)'
        personality_def ='Merupakan tipe yang menyukai keteraturan dan struktur yang jelas dalam bekerja. Jenis pekerjaan yang monotone dan rutinitas bukan merupakan sebuah tantangan bagi orang bertipe ESFJ. Orang bertipe ESFJ senang berinteraksi secara langsung dengan orang lain. Merasa puas apabila pekerjaan yang dilakukannya memiliki dampak bagi orang lain.'
        job_recommend = 'Akuntan, Perawat, Guru, Konseling'
        return "Tipe Kepribadianmu adalah " + str(personality_type) + ". Kamu " + str(personality_def) + " Rekomendasi pekerjaan yang cocok untukmu: " + str(job_recommend)
def estp(personality_type):
    if personality_type == 'ESTP':
        personality_type ='ESTP (Entrepreneur)'
        personality_def ='Merupakan tipe orang yang dapat mengambil keputusan dengan cepat. Mudah membangun koneksi baru dimanapun mereka berada. Orang bertipe ESTP memiliki rasa ingin tahu serta semangat tinggi. Merupakan seorang pengamat namun kurang sabar.'
        job_recommend = 'Paramedik, Polisi, Tentara, Atlit, Pengusaha'
        return "Tipe Kepribadianmu adalah " + str(personality_type) + ". Kamu " + str(personality_def) + " Rekomendasi pekerjaan yang cocok untukmu: " + str(job_recommend)
def esfp(personality_type):
    if personality_type == 'ESFP':
        personality_type ='ESFP (Entertrainer)'
        personality_def ='Merupakan tipe orang yang beradaptasi dengan situasi yang ada di sekitarnya. Orang ESFP menyukai pekerjaan yang berinteraksi dengan orang lain. Beberapa orang ESFP memiliki kemampuan untuk berkreasi. Orang bertipe ESFP membutuhkan kebebasan, kebaruan serta interaksi dengan orang lain.'
        job_recommend = 'Sales, Tour Guide, Konselor, Pelatih, Seniman, Paramedik'
        return "Tipe Kepribadianmu adalah " + str(personality_type) + ". Kamu " + str(personality_def) + " Rekomendasi pekerjaan yang cocok untukmu: " + str(job_recommend)
