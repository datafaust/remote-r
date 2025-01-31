# example of a notebook functionality
# lets say someone wants to write code
# and interact with an r instance via rserve
import pyRserve

# connect
host = "localhost"
port = 6311 

conn = pyRserve.connect(host=host, port=port)

result = conn.eval('rnorm(10)')

print(result)

# close the connection
conn.close()
