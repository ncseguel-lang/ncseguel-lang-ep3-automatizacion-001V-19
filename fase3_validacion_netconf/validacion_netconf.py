from ncclient import manager
import xml.etree.ElementTree as ET

ROUTER = "192.168.56.101"
USER = "cisco"
PASSWORD = "cisco123!"

EXPECTED_HOSTNAME = "RTR-PLATCLD"

with manager.connect(
    host=ROUTER,
    port=830,
    username=USER,
    password=PASSWORD,
    hostkey_verify=False
) as m:

    print("[OK] Conexion NETCONF establecida")

    config = m.get_config(source="running")

    xml_data = config.xml

    with open("evidencias/rpc_reply_raw.xml", "w") as f:
        f.write(xml_data)

    print("[OK] XML guardado")

    if EXPECTED_HOSTNAME in xml_data:
        print("[OK] Hostname encontrado:", EXPECTED_HOSTNAME)
    else:
        print("[FAIL] Hostname no encontrado")

    if "Loopback10" in xml_data:
        print("[OK] Loopback10 encontrada")
    else:
        print("[FAIL] Loopback10 no encontrada")

    if "10.1.19.1" in xml_data:
        print("[OK] IP Loopback correcta")
    else:
        print("[FAIL] IP Loopback no encontrada")

    if "9.9.9.9" in xml_data:
        print("[OK] Servidor NTP encontrado")
    else:
        print("[FAIL] Servidor NTP no encontrado")

    if "Enlace-WAN-Curico" in xml_data:
        print("[OK] Descripcion WAN encontrada")
    else:
        print("[FAIL] Descripcion WAN no encontrada")

    print("\nRESULTADO: CONFORME")
