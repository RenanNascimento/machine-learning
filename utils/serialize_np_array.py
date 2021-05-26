'''Serialize numpy array to send as a post request
'''

# Client
arr = np.random.rand(10, 10)
data = json.dumps(arr.tolist())

# API
data = json.loads(req['data'])
arr = np.array(data)