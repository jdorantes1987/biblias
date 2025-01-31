from sqlite3 import connect

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

    data = DataBiblias(p_biblia=p_RVA)
    df = data.get_biblia()
    palabras = ["Jesucristo"]
    df = df[df["text"].str.contains("|".join(palabras), regex=True)]
    df["text"] = df["text"].str[:140]
    print(df.to_string(index=False))
