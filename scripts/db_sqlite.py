from pandas import read_sql

from scripts.interfaz_data_source import IDataSource


class BD_SQLite_Biblias(IDataSource):
    def __init__(self, conexion) -> None:
        self.conexion = conexion
        self.cur = conexion.cursor()

    def get_biblia(self):
        sql = """
                SELECT v.book_number, b.short_name, v.chapter, v.verse, v.text
                FROM verses AS v LEFT JOIN books AS b ON v.book_number = b.book_number
            """
        return read_sql(sql, self.conexion)
