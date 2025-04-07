from abc import ABC, abstractmethod


class IDataSource(ABC):
    """
    IDataSource es una clase base abstracta que define la interfaz para fuentes de datos
    relacionadas con información bíblica. Obliga a la implementación de métodos específicos
    en cualquier subclase que la herede.
    Métodos
    -------
    get_biblia():
        Método abstracto que debe ser implementado por las subclases para recuperar datos bíblicos.
    get_info_biblia():
        Método opcional que puede ser implementado por las subclases para recuperar información
        adicional sobre los datos bíblicos.
    """

    @abstractmethod
    def get_biblia(self):
        pass

    def get_info_biblia(self):
        pass
