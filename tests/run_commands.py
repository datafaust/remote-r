import pyRserve

# connect
host = "localhost"
port = 6311 

conn = pyRserve.connect(host=host, port=port)

result = conn.eval('rnorm(10)')

print(result)

# close the connection
conn.close()
