import pprint
import time

from oBiblia import DataBiblia


def execution_time(func):
    """Decorador para medir el tiempo de ejecución de una función."""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Tiempo de ejecución de '{func.__name__}': {end_time - start_time:.4f} segundos"
        )
        return result

    return wrapper


class Seek:
    def __init__(self, is_remote: bool, file_id: list, bible_version: list) -> None:
        self.data = [
            DataBiblia(
                is_remote=is_remote,
                file_id=file_id[i],
                path_db_biblia=bible_version[i],
            )
            for i in range(len(file_id))
        ]

    @execution_time
    def search_words(self, find_word: list) -> list:
        pattern = r"\b" + "|".join(find_word) + r"\b"  # Crear el patrón de búsqueda
        # Buscar las palabras en la biblia
        return [
            biblia.get_biblia().loc[
                biblia.get_biblia()["text"].str.contains(pattern, regex=True)
            ]
            for biblia in self.data
        ]


if __name__ == "__main__":

    p_BLPH = [
        r"F:/Samsung/Personal/Estudios_Bbcs/Biblias Sqlite/BLPH/BLPH.SQLite3",
        "1O7NQJBOeb-9IG0GI9kbKRbxw-YjnVmxR",
    ]
    p_NRV1990 = [
        r"F:/Samsung/Personal/Estudios_Bbcs/Biblias Sqlite/NRV1990/NRV1990.SQLite3",
        "1iJAd7pm85A6XgvseClpfHNOvuhdTC3bB",
    ]
    p_RVA = [
        r"F:/Samsung/Personal/Estudios_Bbcs/Biblias Sqlite/RVA/RVA.SQLite3",
        "1jiCnQkm0Gy_BmossfYKOKIUHDTSlISWg",
    ]

    seek = Seek(
        is_remote=True,
        file_id=[
            p_BLPH[1],
            p_NRV1990[1],
        ],
        bible_version=[
            p_BLPH[1],
            p_NRV1990[1],
        ],
    )

    palabras = [
        "Jesus",
        "Cristo",
    ]
    result = seek.search_words(palabras)
    for i, df in enumerate(result):
        pprint.pprint(
            df.to_dict("records"),
            indent=4,
            width=130,
            compact=True,
            depth=2,
            sort_dicts=False,
        )
