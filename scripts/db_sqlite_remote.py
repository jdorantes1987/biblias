import io
import sqlite3

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from pandas import DataFrame

from scripts.interfaz_data_source import IDataSource


class BD_SQLite_Biblias_remote(IDataSource):

    def __init__(self, file_id) -> None:
        self.scope = [
            "https://www.googleapis.com/auth/drive"
        ]  # Permisos de acceso a Google Drive
        self.key = "key.json"  # Ruta al archivo de credenciales de servicio
        self.file_sqlite = self.__download_file_from_google_drive(file_id=file_id)

    def __download_file_from_google_drive(self, file_id) -> io.BytesIO:
        try:
            # Carga las credenciales desde el archivo JSON
            creds = service_account.Credentials.from_service_account_file(
                filename=self.key, scopes=self.scope
            )
            # Construye el servicio de la API de Google Drive
            service = build("drive", "v3", credentials=creds)

            # Solicita el archivo desde Google Drive
            request_file = service.files().get_media(fileId=file_id)
            file = io.BytesIO()
            downloader = MediaIoBaseDownload(file, request_file)
            done = False
            while not done:
                status, done = downloader.next_chunk()
                print(f"Download {int(status.progress() * 100)}%.")
                print("Archivo descargado exitosamente.")

            # Regresa el archivo descargado
            file.seek(0)  # Asegúrate de que el puntero esté al inicio del archivo
            return file
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None

    def get_biblia_remote(self):
        df = DataFrame()  # Inicializar un DataFrame vacío
        if self.file_sqlite:
            # Cargar la base de datos SQLite3 desde el objeto BytesIO
            try:
                # Conectar a la base de datos en memoria usando el contenido descargado
                conn = sqlite3.connect(":memory:")  # Base de datos en memoria
                cursor = conn.cursor()

                # Escribir el contenido del archivo descargado en la base de datos en memoria
                with open("temp_db.sqlite3", "wb") as temp_file:
                    temp_file.write(self.file_sqlite.getvalue())

                # Conectar a la base de datos temporal
                conn = sqlite3.connect("temp_db.sqlite3")
                cursor = conn.cursor()

                sql = """
                        SELECT v.book_number as nro_libro, b.long_name as libro, v.chapter as capitulo, v.verse as verso, v.text
                        FROM verses AS v LEFT JOIN books AS b ON v.book_number = b.book_number
                    """

                # Ejecutar una consulta de ejemplo
                cursor.execute(sql)

                # Obtener los resultados en un DataFrame
                df = DataFrame(
                    cursor.fetchall(),
                    columns=["nro_libro", "libro", "capitulo", "verso", "text"],
                )

                # Cerrar la conexión
                conn.close()
            except sqlite3.Error as e:
                print(f"Error al trabajar con la base de datos SQLite3: {e}")
        else:
            print("No se pudo descargar el archivo.")

        return df

    def get_biblia(self):
        return super().get_biblia()  # Método no implementado para esta clase

    def get_info_biblia(self):
        df = DataFrame()  # Inicializar un DataFrame vacío
        if self.file_sqlite:
            # Cargar la base de datos SQLite3 desde el objeto BytesIO
            try:
                # Conectar a la base de datos en memoria usando el contenido descargado
                conn = sqlite3.connect(":memory:")  # Base de datos en memoria
                cursor = conn.cursor()

                # Escribir el contenido del archivo descargado en la base de datos en memoria
                with open("temp_db.sqlite3", "wb") as temp_file:
                    temp_file.write(self.file_sqlite.getvalue())

                # Conectar a la base de datos temporal
                conn = sqlite3.connect("temp_db.sqlite3")
                cursor = conn.cursor()

                sql = """
                        SELECT *
                        FROM info
                     """

                # Ejecutar una consulta de ejemplo
                cursor.execute(sql)

                # Obtener los resultados en un DataFrame
                df = DataFrame(
                    cursor.fetchall(),
                    columns=[
                        "name",
                        "value",
                    ],
                )

                # Cerrar la conexión
                conn.close()
            except sqlite3.Error as e:
                print(f"Error al trabajar con la base de datos SQLite3: {e}")
        else:
            print("No se pudo descargar el archivo.")
        return df


if __name__ == "__main__":
    # ID del archivo en Google Drive
    file_id = "1O7NQJBOeb-9IG0GI9kbKRbxw-YjnVmxR"  # Reemplaza con tu ID de archivo real
    data = BD_SQLite_Biblias_remote(file_id)
    df = data.get_info_biblia()
    print(df)
