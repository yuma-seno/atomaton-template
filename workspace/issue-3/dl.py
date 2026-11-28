import hashlib, sys, urllib.request
url = "https://github.com/yuma-seno/atomaton/releases/download/v0.28.0/atomaton-delivery.zip"
out = "/tmp/atomaton-workspace/atomaton-delivery.zip"
req = urllib.request.Request(url, headers={"User-Agent": "atomaton-agent-read-only"})
try:
    with urllib.request.urlopen(req, timeout=180) as r:
        data = r.read()
    with open(out, "wb") as f:
        f.write(data)
    print("OK", len(data), hashlib.sha256(data).hexdigest(), repr(data[:2]))
except Exception as e:
    print("FAIL", type(e).__name__, e)
    sys.exit(1)
