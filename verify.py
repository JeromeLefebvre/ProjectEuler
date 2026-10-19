import hashlib, json, subprocess, sys, time, pathlib

answers = json.loads(pathlib.Path("answers.json").read_text())
failed = False
for f in sorted(pathlib.Path(".").glob("Python/Problem[0-9]*.py")):
    n = str(int(f.stem[1:]))
    start = time.perf_counter()
    try:
        out = subprocess.run([sys.executable, f], capture_output=True,
                             text=True, timeout=60).stdout.strip()
    except subprocess.TimeoutExpired:
        print(f"⏱  {f.name} exceeded 60s"); failed = True; continue
    secs = time.perf_counter() - start
    h = hashlib.sha256(out.encode()).hexdigest()
    ok = answers.get(n) == h
    print(f"{'✅' if ok else '❌'} {f.name} {secs:.2f}s")
    failed |= not ok
sys.exit(failed)