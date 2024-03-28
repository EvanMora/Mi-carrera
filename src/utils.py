import sqlite3


def query(sql):
    conection = sqlite3.connect("database/Programas.db")
    cursor = conection.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


def departaments():
    return query(
        """
                 SELECT 
                 DEPARTAMENTO_OFERTA_PROGRAMA 
                 FROM 
                 programas 
                 WHERE 
                    DEPARTAMENTO_OFERTA_PROGRAMA IS NOT NULL
                 GROUP BY 
                 DEPARTAMENTO_OFERTA_PROGRAMA
                 """
    )


def cities(departament):
    return query(
        f"""
                 SELECT 
                     MUNICIPIO_OFERTA_PROGRAMA 
                 FROM 
                     programas 
                 WHERE 
                     DEPARTAMENTO_OFERTA_PROGRAMA == '{departament}' 
                 GROUP BY 
                     MUNICIPIO_OFERTA_PROGRAMA
                 """
    )


def uni(city):
    return query(
        f"""
                 SELECT 
                   NOMBRE_INSTITUCION
                 FROM 
                   programas 
                 WHERE 
                   MUNICIPIO_OFERTA_PROGRAMA == '{city}'
                 GROUP BY
                   NOMBRE_INSTITUCION
                 """
    )


def career(city, uni):
    return query(
        f"""
                 SELECT  
                   ID,
                   NOMBRE_DEL_PROGRAMA 
                 FROM 
                   programas 
                 WHERE 
                   MUNICIPIO_OFERTA_PROGRAMA == '{city}' 
                   AND NOMBRE_INSTITUCION == '{uni}'
                 """
    )
