from sqlite3 import connect

from scripts.db_sqlite import BD_SQLite_Biblias as DB

db_path = r"F:\Samsung/Personal/Estudios_Bbcs/Biblias Sqlite/BLPH/BLPH.SQLite3"


class DataBiblias:
    def __init__(self) -> None:
        self.data = DB(connect(db_path))

    def get_biblia_BLPH(self):
        return self.data.get_biblia_BLPH()


if __name__ == "__main__":
    data = DataBiblias()
    df = data.get_biblia_BLPH()
    palabras = ["interior"]
    df = df[df["text"].str.contains("|".join(palabras), regex=True)]
    df["text"] = df["text"].str[:140]
    print(df.to_string())
