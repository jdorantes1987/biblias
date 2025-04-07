from sqlite3 import connect
import pprint

from scripts.db_sqlite import BD_SQLite_Biblias


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

    def __init__(self, p_biblia) -> None:
        self.data = BD_SQLite_Biblias(connect(p_biblia))

    def get_biblia(self):
        data_biblia = self.data.get_biblia()  # Obtener la biblia
        info_biblia = (  # Obtener la descripción de la biblia
            self.data.get_info_biblia().set_index("name").loc["description", "value"]
        )
        data_biblia["version"] = info_biblia  # Agregar la versión de la biblia
        return data_biblia

    def get_info(self):
        return self.data.get_info_biblia()


if __name__ == "__main__":
    p_BLPH = r"F:/Samsung/Personal/Estudios_Bbcs/Biblias Sqlite/BLPH/BLPH.SQLite3"
    p_NRV1990 = (
        r"F:/Samsung/Personal/Estudios_Bbcs/Biblias Sqlite/NRV1990/NRV1990.SQLite3"
    )
    p_RVA = r"F:/Samsung/Personal/Estudios_Bbcs/Biblias Sqlite/RVA/RVA.SQLite3"

    data = DataBiblia(p_biblia=p_BLPH)
    df = data.get_biblia()
    palabras = ["glotón", "comilón", "comilona", "comilones", "comilonas", "gula"]
    df = df[df["text"].str.contains(r"\b" + "|".join(palabras) + r"\b", regex=True)]
    df["text"] = df["text"]
    pprint.pprint(df.to_dict("records"), indent=4, width=130, compact=True, depth=2)
