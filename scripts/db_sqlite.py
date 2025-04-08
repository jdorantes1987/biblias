from pandas import read_sql

from scripts.interfaz_data_source import IDataSource


class BD_SQLite_Biblias(IDataSource):
    """
    BD_SQLite_Biblias es una clase que implementa la interfaz IDataSource para interactuar con una base de datos SQLite
    que contiene información bíblica. Proporciona métodos para recuperar versículos bíblicos y metadatos asociados.
    Atributos:
        conexion (sqlite3.Connection): La conexión activa a la base de datos SQLite.
        cur (sqlite3.Cursor): El cursor asociado a la conexión para ejecutar consultas SQL.
    Métodos:
        get_biblia():
            Recupera versículos bíblicos junto con información asociada del libro y capítulo.
            Retorna un pandas.DataFrame con columnas como número del libro, nombre del libro, capítulo, versículo y texto.
        get_info_biblia():
            Retorna un pandas.DataFrame con todas las filas y columnas de la tabla 'info'.
    """

    def __init__(self, conexion) -> None:
        self.conexion = conexion
        self.cur = conexion.cursor()

    def get_biblia(self):
        """
        Recupera versículos bíblicos junto con la información asociada del libro y capítulo.

        Este método ejecuta una consulta SQL para obtener datos de la tabla `verses`,
        uniéndola con la tabla `books` para incluir los nombres de los libros. El resultado incluye
        el número del libro, el nombre del libro, el capítulo, el versículo y el texto del versículo.

        Retorna:
            pandas.DataFrame: Un DataFrame que contiene las siguientes columnas:
            - nro_libro (int): El número del libro.
            - libro (str): El nombre completo del libro.
            - capitulo (int): El número del capítulo.
            - verso (int): El número del versículo.
            - text (str): El texto del versículo.
        """
        sql = """
                SELECT v.book_number as nro_libro, b.long_name as libro, v.chapter as capitulo, v.verse as verso, v.text
                FROM verses AS v LEFT JOIN books AS b ON v.book_number = b.book_number
            """
        return read_sql(sql, self.conexion)

    def get_info_biblia(self):
        """
        Recupera todos los registros de la tabla 'info' en la base de datos SQLite.

        Retorna:
            pandas.DataFrame: Un DataFrame que contiene todas las filas y columnas de la tabla 'info'.
        """
        sql = """
                SELECT *
                FROM info
            """
        return read_sql(sql, self.conexion)

    def get_biblia_remote(self):
        """
        Este método no está implementado para esta clase.
        """
        raise NotImplementedError("Este método no está implementado para esta clase.")
