import pyspeedtest 

# Test speed function 

st = pyspeedtest.SpeedTest()
ping = st.ping()
download = st.download()
upload = st.upload()

# Print function 
print('ping: ' + str(ping))
print('download: ' + str(download))
print('upload: ' + str(upload))
