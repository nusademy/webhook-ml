from google_trans_new import google_translator  

translator = google_translator()  
user='halo selamat pagi'
translate_text = translator.translate(user,lang_tgt='en')  
print(translate_text)