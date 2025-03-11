import subprocess
result = subprocess.run(["ls","-l"],capture_output=True,text=True)
print("STDOUT",result.stdout)
print("STDERROR",result.stderr)
print("STDREDURNOCDE",result.returncode)
