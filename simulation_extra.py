import threading
import time
import sys
import random
import psycopg2
import psycopg2.extensions

def attempt_reservation(event_id, available_seats, user_name, isolation_level):
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="reservas_evento",
            user="postgres",
            password="0512"  # Reemplaza con tu contraseña
        )
        conn.set_client_encoding('UTF8')
        conn.set_isolation_level(isolation_level)
        cur = conn.cursor()
        
        # Cada hilo elige un asiento aleatorio de los disponibles
        seat_id = random.choice(available_seats)
        
        try:
            cur.execute("BEGIN;")
            cur.execute("""
                INSERT INTO reservas (id_evento, id_asiento, usuario)
                VALUES (%s, %s, %s);
            """, (event_id, seat_id, user_name))
            conn.commit()
            print(f"{user_name}: Reserva exitosa en el asiento {seat_id}!")
        except Exception as e:
            conn.rollback()
            print(f"{user_name}: Reserva fallida en el asiento {seat_id}. Error: {e}")
        finally:
            cur.close()
            conn.close()
    except Exception as conn_error:
        print(f"{user_name}: Error de conexión: {conn_error}")

def run_simulation(num_users, isolation_level, available_seats):
    threads = []
    event_id = 1  # Asumimos que usamos el evento 1
    start_time = time.time()
    for i in range(num_users):
        user_name = f"usuario_sim_{i+1}"
        t = threading.Thread(target=attempt_reservation, args=(event_id, available_seats, user_name, isolation_level))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end_time = time.time()
    print(f"Simulación completada en {end_time - start_time:.2f} segundos.")

if __name__ == '__main__':
    # Primer argumento: Nivel de aislamiento
    nivel_str = sys.argv[1] if len(sys.argv) > 1 else "READ_COMMITTED"
    # Segundo argumento: Número de usuarios
    num_users = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    # Tercer argumento: Número de asientos disponibles (por defecto 10)
    num_seats = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    available_seats = list(range(1, num_seats + 1))
    
    if nivel_str.upper() == "READ_COMMITTED":
        isolation_level = psycopg2.extensions.ISOLATION_LEVEL_READ_COMMITTED
    elif nivel_str.upper() == "REPEATABLE_READ":
        isolation_level = psycopg2.extensions.ISOLATION_LEVEL_REPEATABLE_READ
    elif nivel_str.upper() == "SERIALIZABLE":
        isolation_level = psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE
    else:
        print("Nivel de aislamiento no válido. Usa READ_COMMITTED, REPEATABLE_READ o SERIALIZABLE.")
        sys.exit(1)

    print(f"Ejecutando simulación extra con {num_users} usuarios, nivel de aislamiento {nivel_str.upper()}, y {num_seats} asientos disponibles: {available_seats}.")
    run_simulation(num_users, isolation_level, available_seats)
