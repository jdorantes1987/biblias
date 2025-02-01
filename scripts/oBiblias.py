import re
from sqlite3 import connect
import pprint

from scripts.db_sqlite import BD_SQLite_Biblias as DB


class DataBiblias:
    def __init__(self, p_biblia) -> None:
        self.data = DB(connect(p_biblia))

    def get_biblia(self):
        return self.data.get_biblia()


if __name__ == "__main__":
    p_BLPH = r"F:\Samsung/Personal/Estudios_Bbcs/Biblias Sqlite/BLPH/BLPH.SQLite3"
    p_NRV1990 = (
        r"F:\Samsung/Personal/Estudios_Bbcs/Biblias Sqlite/NRV1990/NRV1990.SQLite3"
    )
    p_RVA = r"F:\Samsung/Personal/Estudios_Bbcs/Biblias Sqlite/RVA/RVA.SQLite3"

    data = DataBiblias(p_biblia=p_BLPH)
    df = data.get_biblia()
    palabras = ["noventa y nueve"]
    df = df[df["text"].str.contains(r"\b" + "|".join(palabras) + r"\b", regex=True)]
    df["text"] = df["text"]
    # df.to_excel("RVA.xlsx", index=False)
    pprint.pprint(
        df.to_string(),
        indent=4,
        width=100,
        compact=True,
    )
