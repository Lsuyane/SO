import threading
import time
import random

class Banco:
    def __init__(self, num_caixas):
        self.num_caixas = num_caixas
        self.sem_caixas = threading.Semaphore(num_caixas)

    def atender_cliente(self, cliente_id):
        atendimento_time = random.uniform(3, 10)
        print(f'Cliente {cliente_id} está sendo atendido por {atendimento_time:.2f} segundos.')
        time.sleep(atendimento_time)
        print(f'Cliente {cliente_id} foi atendido.')

def cliente_thread(cliente_id, banco):
    with banco.sem_caixas:
        banco.atender_cliente(cliente_id)

def main():
    num_clientes = 30
    num_caixas = 3
    banco = Banco(num_caixas)
    
    threads = []
    for i in range(num_clientes):
        cliente_thread_id = i + 1
        thread = threading.Thread(target=cliente_thread, args=(cliente_thread_id, banco))
        threads.append(thread)
        thread.start()
        time.sleep(random.uniform(0.1, 1))

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
