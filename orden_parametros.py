
def parametros_ordenados(nombre,apellido, *args, **kwargs):
    pass

## Esta funcion nos dara error porque *args debe ir antes de **kwargs
def parametros_desordenados(nombre,apellido, **kwargs, *args ):
    pass