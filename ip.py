import ipaddress


# Kiszámítja a szükséges információkat a CIDR formátumból
def calculate_subnet_details(cidr):
    # Létrehozza az IPv4 hálózati objektumot a CIDR alapján
    network = ipaddress.IPv4Network(cidr, strict=False)

    # Kiszámítja a hálózati címet, a broadcast címet és az alhálózati maszkot
    network_address = network.network_address
    broadcast_address = network.broadcast_address
    netmask = network.netmask

    # Az összes kiosztható IP-cím az alhálózatban
    hosts = list(network.hosts())  # Csak a kiosztható host IP-k

    # Visszatér a kiszámolt adatokkal
    return {
        "Hálózati cím": str(network_address),
        "Alhálózati maszk": str(netmask),
        "Broadcast cím": str(broadcast_address),
        "Első kiosztható IP": str(hosts[0]) if hosts else None,
        "Utolsó kiosztható IP": str(hosts[-1]) if hosts else None,
        "Összes kiosztható IP-cím": len(hosts)
    }


# Felhasználói bemenet kérése
cidr_input = input("Adja meg az IP-címet és az előtagot (CIDR formátumban): ")

# Kiszámítja a szükséges adatokat
results = calculate_subnet_details(cidr_input)

# Eredmények kiírása
print("\nEredmények:")
for key, value in results.items():
    print(f"{key}: {value}")
