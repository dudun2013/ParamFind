## Tools Parameter Finder By Python

# Module dibutuhkan
import time, os, platform, subprocess as sub
from colorama import Fore as f, Style as s

# Warna
r = f.RED
c = f.CYAN
g = f.GREEN
y = f.YELLOW
rs = s.RESET_ALL

# OOP coding
class Tools:
	def __init__(self, target):
		self.target = target

	def crawl(self):
		print(f"{y}[*] Memulai Crawler pada target...{rs}")
		process = sub.Popen(['katana', '-u', self.target], stdout=sub.PIPE, stderr=sub.PIPE, text=True)

		result = []

		for line in process.stdout:
			line = line.strip()
			if line:
				print(f"{g}[+]{rs} {line}")
				result.append(line)
		process.wait()
		return result

	def param(self):
		hasil = self.crawl()
		print(f"\n{y}[*] Mencari parameter...{rs}")
		time.sleep(0.5)
		print("-"*40)

		total = 0

		for url in hasil:
			if '=' in url and '?' in url:
				print(f"{g}[+] {url}{rs}")
				total += 1
		print(f"\n{r}[!] Ditemukan {total} parameter{rs}")

if __name__ == "__main__":
	try:
		os.system('cls' if platform == 'nt' else 'clear')
		print("""
   (҂`_´)
  <,︻╦̵̵̿╤─
[█۞███████]▄▄▄▄▄▄▄▄▄▄▃  Parameter Find!!!
▂▄▅█████████▅▄▃▂        Dev Bangyog!!!!
[███████████████████]
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤
""")

		target = input(f"{c}[?]{rs} Domain target : ")
		app = Tools(target)
		app.param()
	except KeyboardInterrupt:
		print(f"\n{r}[x] Tools dihentikan{rs}")
		time.sleep(0.5)
