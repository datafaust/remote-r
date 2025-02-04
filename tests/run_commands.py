# example of a notebook functionality
# lets say someone wants to write code
# and interact with an r instance via rserve
import pyRserve

#host = "ec2-54-158-104-21.compute-1.amazonaws.com" # example remote
host = "localhost"
port = 6311  

conn = pyRserve.connect(host=host, port=port)

result = conn.eval('rnorm(10)')

print(result)

# close the connection
conn.close()
