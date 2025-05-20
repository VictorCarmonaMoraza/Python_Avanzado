import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s - %(asctime)s",
                    datefmt="%H:%M:%S")
                    
nombre = "Juan"
logging.error(f'{nombre} creo el error')
logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error critico")

try:
    divison= 2 / 0
except:
    logging.error("Error de division por cero")
    logging.exception("Error de division por cero en exception")



