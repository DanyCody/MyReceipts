import anvil.server


anvil.server.connect("VAQPKXKNKSSD4HYOAGS2NZER-H3E7QJIUC62EZ43O")


@anvil.server.callable
def hello_world():
    return 'Hello World!'

anvil.server.wait_forever()


