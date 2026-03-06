# ============================================================================
#   Section 8.4 : Patterns de Concurrence
#   Description : Pattern Rate Limiting - limiteur de debit simple et
#                 Token Bucket pour controler le nombre d'operations
#   Fichier source : 04-patterns-de-concurrence.md
# ============================================================================

import asyncio
import time

# ==========================================
# 1. Rate Limiter simple
# ==========================================
print("=== Rate Limiter simple ===\n")

class RateLimiter:
    """Limiteur de debit simple"""

    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = []
        self.lock = asyncio.Lock()

    async def acquire(self):
        """Acquiert le droit de faire un appel"""
        async with self.lock:
            now = time.time()
            self.calls = [c for c in self.calls if now - c < self.period]

            if len(self.calls) >= self.max_calls:
                sleep_time = self.period - (now - self.calls[0])
                print(f"  Rate limit atteint, attente de {sleep_time:.2f}s")
                await asyncio.sleep(sleep_time)
                self.calls = []

            self.calls.append(time.time())

async def appeler_api(api_id, rate_limiter):
    """Appelle une API avec rate limiting"""
    await rate_limiter.acquire()
    print(f"  Appel API {api_id} a {time.strftime('%H:%M:%S')}")
    await asyncio.sleep(0.01)  # Simule l'appel
    return f"Resultat-{api_id}"

async def demo_rate_limiter():
    # Limite: 5 appels par 1 seconde
    rate_limiter = RateLimiter(max_calls=5, period=1.0)
    taches = [appeler_api(i, rate_limiter) for i in range(12)]
    resultats = await asyncio.gather(*taches)
    print(f"\n{len(resultats)} appels effectues avec respect du rate limit")

asyncio.run(demo_rate_limiter())

# ==========================================
# 2. Token Bucket
# ==========================================
print("\n=== Token Bucket ===\n")

class TokenBucket:
    """Implementation Token Bucket pour rate limiting"""

    def __init__(self, rate, capacity):
        self.rate = rate  # Tokens par seconde
        self.capacity = capacity
        self.tokens = capacity
        self.last_update = time.time()
        self.lock = asyncio.Lock()

    async def acquire(self, tokens=1):
        """Acquiert des tokens"""
        async with self.lock:
            await self._refill()

            while self.tokens < tokens:
                sleep_time = (tokens - self.tokens) / self.rate
                await asyncio.sleep(sleep_time)
                await self._refill()

            self.tokens -= tokens

    async def _refill(self):
        """Remplit le bucket avec de nouveaux tokens"""
        now = time.time()
        elapsed = now - self.last_update
        new_tokens = elapsed * self.rate
        self.tokens = min(self.capacity, self.tokens + new_tokens)
        self.last_update = now

async def tache_limitee(task_id, bucket):
    """Tache avec rate limiting"""
    await bucket.acquire()
    print(f"  Tache {task_id} executee a {time.strftime('%H:%M:%S')}")
    await asyncio.sleep(0.01)

async def demo_token_bucket():
    # 5 tokens par seconde, capacite max 5
    bucket = TokenBucket(rate=5.0, capacity=5)
    taches = [tache_limitee(i, bucket) for i in range(12)]
    await asyncio.gather(*taches)
    print(f"\n12 taches executees avec Token Bucket")

asyncio.run(demo_token_bucket())
