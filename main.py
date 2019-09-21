import remoclient

client = remoclient.NatureRemoClient()

res = client.get_devices()

print(res)
