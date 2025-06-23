# DeadLine Founder — All-in-One Web Recon Tool

**DeadLine Founder** is a Python-based reconnaissance toolkit combining subdomain discovery, port scanning, and HTTP header enumeration. Designed for beginner and intermediate pentesters to automate initial information gathering phases of web security testing.

## Features

- Subdomain enumeration using crt.sh  
- Port scanning on discovered subdomains (default ports 20–1024)  
- HTTP header fetching for each subdomain  
- Results saved in organized text files per subdomain for easy analysis  
- Simple, beginner-friendly code for customization and learning  

## Usage

1. Run the script and input the root domain when prompted (e.g., example.com).  
2. Subdomains will be saved to `subdomains.txt`.  
3. For each subdomain, open ports will be listed in `open_ports_<subdomain>.txt`.  
4. HTTP headers will be saved in `headers_<subdomain>.txt`.  

## Important Legal Notice ⚠️

- Only test domains and IP addresses **you own or have explicit permission to test**.  
- Unauthorized scanning of systems is illegal and can lead to serious legal consequences.  
- Use the tool on legal pentesting platforms or your own environments:  

### Recommended Legal Pentesting Practice Platforms

- [Hack The Box](https://hackthebox.eu) — Wide range of vulnerable labs for safe practice  
- [TryHackMe](https://tryhackme.com) — Guided challenges for all skill levels  
- [VulnHub](https://www.vulnhub.com) — Download vulnerable VM images to run locally  
- [testphp.vulnweb.com](http://testphp.vulnweb.com) — Open web app for security testing  

Always respect laws and privacy when practicing pentesting!

---

If you find this tool useful, please ⭐ star the repo and feel free to contribute!

Happy hacking! 🔐
