# ============================================================================
#   Section 8.4 : Patterns de Concurrence
#   Description : Pattern Actor Model - acteurs avec queue de messages,
#                 CalculatorActor et LoggerActor
#   Fichier source : 04-patterns-de-concurrence.md
# ============================================================================

import threading
import queue
import time

# ==========================================
# Actor Model
# ==========================================
print("=== Actor Model ===\n")

class Actor:
    """Acteur simple avec sa propre queue de messages"""

    def __init__(self, nom):
        self.nom = nom
        self.queue = queue.Queue()
        self.running = True
        self.thread = threading.Thread(target=self._run)
        self.thread.start()

    def _run(self):
        """Boucle principale de l'acteur"""
        print(f"  {self.nom}: Demarre")
        while self.running:
            try:
                message = self.queue.get(timeout=0.5)
                self._handle_message(message)
            except queue.Empty:
                continue
        print(f"  {self.nom}: Arrete")

    def _handle_message(self, message):
        """Traite un message (a surcharger)"""
        print(f"  {self.nom} recoit: {message}")

    def send(self, message):
        """Envoie un message a cet acteur"""
        self.queue.put(message)

    def stop(self):
        """Arrete l'acteur"""
        self.running = False
        self.thread.join()


class CalculatorActor(Actor):
    """Acteur qui effectue des calculs"""

    def _handle_message(self, message):
        operation, a, b = message
        if operation == "add":
            resultat = a + b
            print(f"  {self.nom}: {a} + {b} = {resultat}")
        elif operation == "multiply":
            resultat = a * b
            print(f"  {self.nom}: {a} x {b} = {resultat}")


class LoggerActor(Actor):
    """Acteur qui log des messages"""

    def _handle_message(self, message):
        timestamp = time.strftime("%H:%M:%S")
        print(f"  [{timestamp}] {message}")


# Utilisation
calculator = CalculatorActor("Calculatrice")
logger = LoggerActor("Logger")

# Envoyer des messages
logger.send("Systeme demarre")
calculator.send(("add", 5, 3))
calculator.send(("multiply", 4, 7))
logger.send("Calculs termines")

time.sleep(1)

# Arreter les acteurs
calculator.stop()
logger.stop()

print("\nActors arretes")
