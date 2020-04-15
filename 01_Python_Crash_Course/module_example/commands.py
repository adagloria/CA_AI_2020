from api import Autoencoder

ae = Autoencoder()

commands = dict(fit=ae.fit, encode=ae.encode, decode=ae.decode)
