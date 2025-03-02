
# Penetration Testing Tool

import subprocess

# Hydra function for password cracking
def run_hydra(target, protocol, wordlist):
    print(f"Running Hydra against {target} using {protocol}...")
    subprocess.run(f"hydra -l admin -P {wordlist} {target} {protocol}", shell=True)

# John the Ripper function for cracking hashes
def run_john(target, hash_file):
    print(f"Running John the Ripper against {target} hash file...")
    subprocess.run(f"john --wordlist={target} {hash_file}", shell=True)

# Medusa function for password cracking
def run_medusa(target, protocol, wordlist):
    print(f"Running Medusa against {target} using {protocol}...")
    subprocess.run(f"medusa -h {target} -u admin -P {wordlist} -M {protocol}", shell=True)

# Nmap function for port scanning
def run_nmap(target):
    print(f"Running Nmap scan against {target}...")
    subprocess.run(f"nmap {target}", shell=True)

# Nikto function for web server vulnerability scanning
def run_nikto(target):
    print(f"Running Nikto scan against {target}...")
    subprocess.run(f"nikto -h {target}", shell=True)

def main():
    print("Penetration Testing Tool")
    target = input("Enter target IP: ")
    tool = input("Select tool to use (hydra/john/medusa/nmap/nikto): ")

    if tool == "hydra":
        protocol = input("Enter protocol (ssh/ftp/http): ")
        wordlist = input("Enter path to wordlist: ")
        run_hydra(target, protocol, wordlist)
    elif tool == "john":
        hash_file = input("Enter hash file path: ")
        run_john(target, hash_file)
    elif tool == "medusa":
        protocol = input("Enter protocol (ssh/ftp/http): ")
        wordlist = input("Enter path to wordlist: ")
        run_medusa(target, protocol, wordlist)
    elif tool == "nmap":
        run_nmap(target)
    elif tool == "nikto":
        run_nikto(target)
    else:
        print("Invalid tool selected!")

if __name__ == "__main__":
    main()
