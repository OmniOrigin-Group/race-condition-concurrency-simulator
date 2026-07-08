# ========================================================================
# 🚀 OMNIORIGIN MULTI-THREADED TRANSACTIONAL INTEGRITY GUARD
# Designed by: Jagjit Singh (Principal Architect)
# Strategy: Atomic Lock Guarding & Thread-Safe State Isolation
# Resilience: 100% Race-Condition Immune | Deadlock Prevention: ACTIVE
# ========================================================================
import time
import threading

class GuardedAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        # Thread lock boundary acting as our deterministic gatekeeper
        self._state_lock = threading.Lock()

    def withdraw_guarded(self, amount, thread_name):
        """
        Executes a 100% secure, isolated withdrawal operation.
        Utilizes a safe context-managed lock to neutralize context-switching risks.
        """
        print(f"[*] [{thread_name}] Requesting execution window...")
        
        # Enforce strict thread isolation boundary
        with self._state_lock:
            print(f"[+] [{thread_name}] Lock acquired. Verifying isolated state...")
            print(f"[*] [{thread_name}] Current Secured Balance: {self.balance}")
            
            if self.balance >= amount:
                # Even with heavy unexpected latency, no other thread can breach this boundary
                time.sleep(0.1) 
                
                self.balance -= amount
                print(f"[✔] [{thread_name}] Transaction clean. New Balance: {self.balance}")
                return True
            else:
                print(f"[-] [{thread_name}] Secure Rejection: Insufficient funds.")
                return False
        # Lock automatically releases safely here, even if an unexpected exception occurs

# Execution Simulator to validate resilience
def simulate_protected_environment():
    account = GuardedAccount(initial_balance=100)
    
    t1 = threading.Thread(target=account.withdraw_guarded, args=(100, "Secured_Thread_A"))
    t2 = threading.Thread(target=account.withdraw_guarded, args=(100, "Secured_Thread_B"))
    
    print("\n[🛡️] Launching concurrent transactions under OmniOrigin Guard...")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print(f"\n[✔] FINAL SECURED BALANCE: {account.balance} (Perfectly Isolated Architecture!)")

if __name__ == "__main__":
    simulate_protected_environment()
