import pyspeedtest
st = pyspeedtest.SpeedTest()
ping = st.ping()
downloaded = st.download()
upload = st.upload()

print('ping: ' + str(ping))
print('downloaded: ' + str(downloaded))
print('upload: ' + str(upload))