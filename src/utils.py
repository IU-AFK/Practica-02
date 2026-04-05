def print_format_table (data,name = 'Tabla',job='Cocinero',cat1='Puntaje',cat2='Rondas Ganadas',cat3='Mejor Ronda',cat4='Promedio'):
    """
        toma datos de un diccionario (1 nombre, 4 categorias de un diccionario interno) y los formatea en una tabla
    """
    table = sorted(data.items(), key=lambda x:x[1]['score'], reverse=True)
    print(f"{name}:")
    print(f"{job:<15} {cat1:<10} {cat2:<20} {cat3:<15} {cat4:<10}")
    print("-"*80)

    for name,info in table:
        print(f"{name:<15} {info['score']:<10} {info['wins']:<20} {info['max']:<15} {info['prom']:<10}")

    print("-"*80)