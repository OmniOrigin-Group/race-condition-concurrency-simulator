# ========================================================================
# 🚨 CRITICAL VULNERABILITY: UNPROTECTED CONCURRENT STATE MUTATION (DO NOT USE)
# Engineered by: OmniOrigin Group of Businesses
# Description: Demonstrates how race conditions corrupt data during high load.
# ========================================================================
import time
import threading

class VulnerableAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def withdraw_unsafe(self, amount, thread_name):
        """
        Simulates an unprotected Read-Modify-Write cycle where multiple 
        threads interleave, causing an overdraft / double-spend bug.
        """
        print(f"[*] [{thread_name}] Checking balance. Current: {self.balance}")
        
        if self.balance >= amount:
            # ❌ CRITICAL TRAP: Context switch happens here during heavy I/O delay
            print(f"[!] [{thread_name}] Balance sufficient! Processing transaction...")
            time.sleep(0.1)  # Simulating system latency or DB network roundtrip
            
            self.balance -= amount
            print(f"[+] [{thread_name}] Withdrawal successful. New Balance: {self.balance}")
            return True
        else:
            print(f"[-] [{thread_name}] Transaction rejected. Insufficient funds.")
            return False

# Execution Simulator to trigger the bug
def simulate_race_condition():
    account = VulnerableAccount(initial_balance=100)
    
    # Simulating two distinct user checkout requests hitting the server at the exact same millisecond
    t1 = threading.Thread(target=account.withdraw_unsafe, args=(100, "User_Thread_A"))
    t2 = threading.Thread(target=account.withdraw_unsafe, args=(100, "User_Thread_B"))
    
    print("[!] Launching simultaneous unprotected transactions...")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    # The balance should NEVER be negative in a safe financial engine
    print(f"\n[💥] FINAL ACCOUNT BALANCE: {account.balance} (Expected: 0 or 100, Bug Replicated!)")

if __name__ == "__main__":
    simulate_race_condition()
