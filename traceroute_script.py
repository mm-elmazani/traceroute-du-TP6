import argparse
import re
import subprocess

def extract_valid_ips(line):
    """
    Extract only valid IPv4 and IPv6 addresses from a line of output.
    """
    # Expression régulière sans groupes capturants pour IPv4 et IPv6
    ipv4_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    ipv6_pattern = r"\b(?:[a-fA-F0-9:]+:+)+[a-fA-F0-9]+\b"

    return re.findall(f"{ipv4_pattern}|{ipv6_pattern}", line)

def run_tracert(target, progressive=False, output_file=None):
    """
    Run the tracert command and extract valid IP addresses.
    """
    try:
        print("[INFO] Exécution de 'tracert'...")
        process = subprocess.Popen(
            ["tracert", target],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            encoding="cp850"  # Encodage Windows
        )

        ips = []
        while True:
            line = process.stdout.readline()
            if not line:
                break

            # Extraction des IP valides
            valid_ips = extract_valid_ips(line)
            for ip in valid_ips:
                if ip not in ips:  # Évite les doublons
                    ips.append(ip)
                    if progressive:
                        print(ip)

        # Affichage des IP finales
        if not progressive:
            for ip in ips:
                print(ip)

        # Sauvegarde dans un fichier si nécessaire
        if output_file:
            with open(output_file, "w") as f:
                for ip in ips:
                    f.write(ip + "\n")

    except Exception as e:
        print(f"[ERREUR] Une exception est survenue : {e}")

def main():
    parser = argparse.ArgumentParser(description="Traceroute tool for Windows with Python")
    parser.add_argument("target", help="Target URL or IP address")
    parser.add_argument("-p", "--progressive", action="store_true", help="Display IP addresses progressively")
    parser.add_argument("-o", "--output-file", metavar="FILE", help="Output file to save IP addresses")

    args = parser.parse_args()
    run_tracert(args.target, args.progressive, args.output_file)

if __name__ == "__main__":
    main()
