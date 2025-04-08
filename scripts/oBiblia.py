from sqlite3 import connect
import pprint

from scripts.db_sqlite import BD_SQLite_Biblias
from scripts.db_sqlite_remote import BD_SQLite_Biblias_remote


class DataBiblia:
    """
    Una clase para interactuar con los datos bíblicos almacenados en una base de datos.
    Atributos:
        data (DB): Una instancia de la conexión a la base de datos inicializada con los datos de la Biblia proporcionados.
    Métodos:
        get_biblia():
            Recupera los datos de la Biblia junto con la descripción de su versión.
        get_info():
            Recupera información adicional sobre la Biblia.
    """

    def __init__(self, is_remote, file_id, path_db_biblia) -> None:
        self.is_remote = is_remote
        self.file_id = file_id
        if not is_remote:
            self.data = BD_SQLite_Biblias(connect(path_db_biblia))
        else:
            self.data = BD_SQLite_Biblias_remote(file_id)

    def get_biblia(self):
        # Recupera los datos de la Biblia y la versión
        data_biblia = (
            self.data.get_biblia()
            if not self.is_remote
            else self.data.get_biblia_remote()
        )
        # Recupera la información de la Biblia y la agrega a los datos
        info_biblia = (
            self.data.get_info_biblia().set_index("name").loc["description", "value"]
        )
        data_biblia["version"] = info_biblia
        return data_biblia

    def get_info(self):
        return self.data.get_info_biblia()


if __name__ == "__main__":
    p_BLPH = [
        r"F:/Samsung/Personal/Estudios_Bbcs/Biblias Sqlite/BLPH/BLPH.SQLite3",
        "1O7NQJBOeb-9IG0GI9kbKRbxw-YjnVmxR",
    ]
    p_NRV1990 = [
        r"F:/Samsung/Personal/Estudios_Bbcs/Biblias Sqlite/NRV1990/NRV1990.SQLite3",
        "",
    ]
    p_RVA = [
        r"F:/Samsung/Personal/Estudios_Bbcs/Biblias Sqlite/RVA/RVA.SQLite3",
        "",
    ]

    fileId = p_BLPH[1]
    data = DataBiblia(is_remote=True, file_id=fileId, path_db_biblia=p_BLPH[0])
    df = data.get_biblia()
    palabras = ["glotón", "comilón", "comilona", "comilones", "comilonas", "gula"]
    df = df[df["text"].str.contains(r"\b" + "|".join(palabras) + r"\b", regex=True)]
    df["text"] = df["text"]
    pprint.pprint(df.to_dict("records"), indent=4, width=130, compact=True, depth=2)
