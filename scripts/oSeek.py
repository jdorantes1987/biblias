import pprint

from oBiblia import DataBiblia


class Seek:
    def __init__(self, versions) -> None:
        self.data = [DataBiblia(biblia) for biblia in versions]

    def search_words(self, find_word):
        pattern = r"\b" + "|".join(find_word) + r"\b"  # Crear el patrón de búsqueda
        return [
            biblia.get_biblia().loc[  # Buscar las palabras en la biblia
                biblia.get_biblia()["text"].str.contains(pattern, regex=True)
            ]
            for biblia in self.data
        ]


if __name__ == "__main__":
    p_BLPH = r"F:/Samsung/Personal/Estudios_Bbcs/Biblias Sqlite/BLPH/BLPH.SQLite3"
    p_NRV1990 = (
        r"F:/Samsung/Personal/Estudios_Bbcs/Biblias Sqlite/NRV1990/NRV1990.SQLite3"
    )
    p_RVA = r"F:/Samsung/Personal/Estudios_Bbcs/Biblias Sqlite/RVA/RVA.SQLite3"
    seek = Seek([p_BLPH])
    palabras = ["adversario"]
    result = seek.search_words(palabras)
    for i, df in enumerate(result):
        pprint.pprint(
            df.to_string(),
            indent=4,
            width=100,
            compact=True,
        )
