
import logging

#Hace que se ejecute todos los logs en la consola
logging.basicConfig(level=logging.DEBUG, filename="ejemplo_logs.log"
                    , filemode="w")

logging.debug("Log de debugging")
logging.info("Log de info")
logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error critico")