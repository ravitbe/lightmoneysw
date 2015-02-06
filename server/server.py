import threading
import controlService
import machine
import time


if __name__ == "__main__":

    machine_thread = threading.Thread(target=machine.machine_thread)
    machine_thread.daemon = True
    machine_thread.start()
    
    control_service_thread = threading.Thread(target=controlService.control_service_thread)
    control_service_thread.daemon = True
    control_service_thread.start()

    while True:
        time.sleep(1)
        









