from pyats.topology import loader

tb = loader.load("fase1_baseline/testbed_001V-19.yaml")

dev = tb.devices["CSR1kv"]

dev.connect(log_stdout=True)

print("CONECTADO")

dev.disconnect()
