import speech_recognition as sr

r=sr.Recognizer()

a=sr.AudioFile('audio.wav')
with a as source :
	audio=r.record(source)

text=r.recognize_google(audio)


file1=open("/home/net/MORYSO/PYTHON/class tutorials/projects_1a/speech to text\my.txt","a")
file1.writelines(text)
file1.close()
