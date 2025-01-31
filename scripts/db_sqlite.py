from sqlite3 import IntegrityError

from pandas import read_sql

from scripts.interfaz_data_source import IDataSource


class BD_SQLite_Biblias(IDataSource):
    def __init__(self, conexion) -> None:
        self.conexion = conexion
        self.cur = conexion.cursor()

    def get_biblia_BLPH(self):
        sql = """
                SELECT *
                FROM verses
            """
        return read_sql(sql, self.conexion)
