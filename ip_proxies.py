  import subprocess

# List of SOCKS5 proxies in the format user:pass@host:port
proxies = [
	"user:pass@vel.socks.proxies.com:5080",
	"user:pass@epw.socks.proxies.com:5080",
	"user:pass@mcf.socks.proxies.com:5080",
   
]

for proxy in proxies:
    cmd = ["curl", f"--socks5", proxy, "ifconfig.me"]
    try:
        result = subprocess.check_output(cmd, stderr=subprocess.DEVNULL, timeout=10)
        print(f"{proxy.split('@')[1]} → {result.decode().strip()}")
    except subprocess.TimeoutExpired:
        print(f"{proxy.split('@')[1]} → Timeout")
    except subprocess.CalledProcessError:
        print(f"{proxy.split('@')[1]} → Failed to connect")
