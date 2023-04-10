from datetime import datetime

'''metodos de validacion para ahorrarnos tiempo :C...
when ya tienes todo listo pero descubres que puedes 
mejorarlo y tienes que deshacer todo y volver a hacerlo t.t'''


def validar_str(dato):
    if not isinstance(dato, str) and dato is not None:
        raise ValueError("el valor {} debe ser un str".format(dato))


def validar_int(dato):
    if not isinstance(dato, int) and dato is not None:
        raise ValueError("el valor {} debe ser un nuemero entero".format(dato))


def validar_float(dato):
    if not isinstance(dato, float) and dato is not None:
        raise ValueError("el valor {} debe ser un numero flotante".format(dato))


def validar_lista(dato):
    if not isinstance(dato, list) and dato is not None:
        raise ValueError("el valor {} debe ser una lista".format(dato))


def validar_bool(dato):
    if not isinstance(dato, bool) and dato is not None:
        raise ValueError("el valor {} debe ser un booleano".format(dato))


def validar_fecha_dd_mm_yyyy(dato):
    if dato is not None:
        x = None
        try:
            x = datetime.strptime(dato, "%d-%m-%Y")
        except:
            raise ValueError("el valor fecha_inicio no esta en formato dia-mes-año (00-00-0000) (str)")

'''empezamos con las clases'''
class Equipo_super():
    '''Clase Equipo Suber: contiene los atributos nombre, base, activo,
    fecha inicio, miembros y las funciones "incorporar al equipo"
    "quitar del equipo" y "lista de miembros"

    ARGS
    -nombre: nombre del equipo
    -base: direccion de la base
    -activo: activos true false
    -fecha inicio: fecha de creacion del equipo
    -miembros: lista de miembros participantes
    '''

    def __init__(self, nombre=None, base=None, activo=None,
                 fecha_inicio=None, miembros=[]):
        validar_str(nombre)
        self.__nombre = nombre
        validar_str(base)
        self.__base = base
        validar_bool(activo)
        self.__activo = activo
        validar_fecha_dd_mm_yyyy(fecha_inicio)
        self.__fecha_inicio = fecha_inicio
        validar_lista(miembros)
        self.__miembros = miembros

    #funcion que incorpora a un objeto (super) a la lista miembros
    def incorporar_al_equipo(self, super):
        self.__miembros.append(super)
        print("{} se ha añadido al equipo {}".format(
            super.identidad_secreta, self.__nombre))

    #funcion que quita a un objeto (super) de la lista miembros
    def quitar_del_equipo(self, super):
        self.__miembros.remove(super)
        print("se ha removido a {} del equipo {}.".format(super.identidad_secreta, self.__nombre))

    #funcion que muestra todos los miembros y sus caracteristicas del equipo
    def lista_miembros(self):
        print("los miembros y sus caracteristicas del equipo {} son:".format(self.__nombre))
        for i in self.__miembros:
            print(i)

    # getters y setters
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        validar_str(nuevo_nombre)
        self.__nombre = nuevo_nombre

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, nueva_base):
        validar_str(nueva_base)
        self.__base = nueva_base

    @property
    def activo(self):
        return self.__activo

    @activo.setter
    def activo(self, yes_no):
        validar_bool(yes_no)
        self.__activo = yes_no

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, nueva_fecha):
        validar_fecha_dd_mm_yyyy(nueva_fecha)
        self.__fecha_inicio = nueva_fecha

    @property
    def miembros(self):
        return self.__miembros

    @miembros.setter
    def miembros(self, nuevos_miembros):
        validar_lista(nuevos_miembros)
        self.__miembros = nuevos_miembros

    def __str__(self):
        return '''EQUIPO SUPER {}
        -base en: {}
        -activo actualmente: {}
        -se fundo: {}
        -cantidad de miembros: {}'''.format(self.__nombre, self.__base, self.__activo, self.__fecha_inicio, len(self.__miembros))


class Super():
    '''clase Super con los parametros identidad real, id secreta, edad, especie,
    activo, habilidades y debilidades

    ARGS
    -identidad_real: nombre real del super
    -identidad_secreta: nombre del super al publico
    -edad: edad del super
    -especie: especie del super
    -activo: activo yes_no
    -habilidades: lista de habilidades
    -debilidades: lista de debilidades'''

    def __init__(self, identidad_real=None, identidad_secreta=None,
                 edad=None, especie=None, activo=None,
                 habilidades=[], debilidades=[]):
        validar_str(identidad_real)
        self.__identidad_real = identidad_real
        validar_str(identidad_secreta)
        self.__identidad_secreta = identidad_secreta
        validar_int(edad)
        self.__edad = edad
        validar_str(especie)
        self.__especie = especie
        validar_bool(activo)
        self.__activo = activo
        validar_lista(habilidades)
        self.__habilidades = habilidades
        validar_lista(debilidades)
        self.__debilidades = debilidades

    # printea las habilidades que posee
    def lista_habilidades(self):
        print("las habilidades de {} son:".format(self.__identidad_secreta))
        for i in self.__habilidades:
            print(">>> ", i)

    # printea las debilidades que posee
    def lista_debilidades(self):
        print("las debilidades de {} son:".format(self.__identidad_secreta))
        for i in self.__debilidades:
            print(">>> ", i)

    # setters y getters
    @property
    def identidad_real(self):
        return self.__identidad_real
    @identidad_real.setter
    def identidad_real(self, nueva_identidad_real):
        validar_str(nueva_identidad_real)
        self.__identidad_real = nueva_identidad_real

    @property
    def identidad_secreta(self):
        return self.__identidad_secreta
    @identidad_secreta.setter
    def identidad_secreta(self, nueva_identidad_secreta):
        validar_str(nueva_identidad_secreta)
        self.__identidad_secreta = nueva_identidad_secreta

    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, nueva_edad):
        validar_int(nueva_edad)
        self.__edad = nueva_edad

    @property
    def especie(self):
        return self.__especie
    @especie.setter
    def especie(self, nueva_especie):
        validar_str(nueva_especie)
        self.__especie = nueva_especie

    @property
    def activo(self):
        return self.__activo
    @activo.setter
    def activo(self, yes_no):
        validar_bool(yes_no)
        self.__activo = yes_no

    @property
    def habilidades(self):
        return self.__habilidades
    @habilidades.setter
    def habilidades(self, nuevas_habilidades):
        validar_lista(nuevas_habilidades)
        self.__habilidades = nuevas_habilidades

    @property
    def debilidades(self):
        return self.__debilidades
    @debilidades.setter
    def debilidades(self, nuevas_debilidades):
        validar_lista(nuevas_debilidades)
        self.__debilidades = nuevas_debilidades

    def __str__(self):
        return '''informacion de Super:
    -identidad real: {}
    -identidad secreta: {}
    -edad: {}
    -especie: {}
    -activo: {}
    -cantidad de habilidades {}
    -cantidad de debilidades {}'''.format(self.__identidad_real, self.__identidad_secreta,
                                          self.__edad, self.__especie, self.__activo, len(self.__habilidades),
                                          len(self.__debilidades))


class Super_sin_poderes(Super):
    '''Clase Super sin poderes hija de clase Super con los parametros identidad real, id secreta, edad, especie,
    activo, habilidades, debilidades y origen

    ARGS
    -identidad_real: nombre real del super
    -identidad_secreta: nombre del super al publico
    -edad: edad del super
    -especie: especie del super
    -activo: activo yes_no
    -habilidades: lista de habilidades
    -debilidades: lista de debilidades
    -suceso_inicio_historia: historia que relata origen del super
    '''

    def __init__(self, identidad_real=None, identidad_secreta=None,
                 edad=None, especie=None, activo=None,
                 habilidades=[], debilidades=[],
                 suceso_inicio_historia=None):
        super().__init__(identidad_real, identidad_secreta, edad, especie,
                         activo, habilidades, debilidades)
        validar_str(suceso_inicio_historia)
        self.__suceso_inicio_historia = suceso_inicio_historia

    # getter y setters
    @property
    def suceso_inicio_historia(self):
        return self.__suceso_inicio_historia

    @suceso_inicio_historia.setter
    def suceso_inicio_historia(self, nueva_historia):
        validar_str(nueva_historia)
        self.__suceso_inicio_historia = nueva_historia

    def __str__(self):
        return super().__str__() + "\n" + "    -origen: {}".format(self.__suceso_inicio_historia)


class Super_con_poderes(Super):
    '''clase Super_con_poderes hija de clase Super con los parametros identidad real, id secreta, edad, especie,
    activo, habilidades y debilidades

    ARGS
    -identidad_real: nombre real del super
    -identidad_secreta: nombre del super al publico
    -edad: edad del super
    -especie: especie del super
    -activo: activo yes_no
    -habilidades: lista de habilidades
    -debilidades: lista de debilidades
    -origen: determina el origen de los poderes del super, puede variar entre
            (nacimiento, adquiridos y desconocido)
    '''

    def __init__(self, identidad_real=None, identidad_secreta=None,
                 edad=None, especie=None, activo=None,
                 habilidades=[], debilidades=[],
                 origen=None):
        super().__init__(identidad_real, identidad_secreta, edad, especie,
                         activo, habilidades, debilidades)
        validar_str(origen)
        if origen not in ("nacimiento", "Nacimiento", "adquiridos", "Adquiridos",
                          "desconocido", "Desconocido"):
            raise ValueError("""solo puedes utilizar las siguientes 3 opciones:
            -Nacimiento
            -Adquiridos
            -Desconocido""")
        self.origen = origen

    #Setter y Getter
    @property
    def origen(self):
        return self.__origen
    @origen.setter
    def origen(self, nuevo_origen):
        validar_str(nuevo_origen)
        if nuevo_origen not in ("nacimiento", "Nacimiento", "adquiridos", "Adquiridos",
                          "desconocido", "Desconocido"):
            raise ValueError("""solo puedes utilizar las siguientes 3 opciones:
            -Nacimiento
            -Adquiridos
            -Desconocido""")
        self.__origen = nuevo_origen

    def __str__(self):
        return super().__str__() + "\n" + "    -origen: {}".format(self.__origen)


class Magico(Super_con_poderes):
    '''clase Magico hija de Clase Super_con_poderes con los parametros identidad real, id secreta, edad, especie,
    activo, habilidades y debilidades

    ARGS
    -identidad_real: nombre real del super
    -identidad_secreta: nombre del super al publico
    -edad: edad del super
    -especie: especie del super
    -activo: activo yes_no
    -habilidades: lista de habilidades
    -debilidades: lista de debilidades
    -origen: determina el origen de los poderes del super, puede variar entre
            (nacimiento, adquiridos y desconocido)
    -tipo_magia: tipo de magia que maneja el super
    '''

    def __init__(self, identidad_real=None, identidad_secreta=None,
                 edad=None, especie=None, activo=None,
                 habilidades=[], debilidades=[],
                 origen=None, tipo_magia=None):
        super().__init__(identidad_real, identidad_secreta, edad, especie, activo,
                         habilidades, debilidades, origen)
        validar_str(tipo_magia)
        self.__tipo_magia = tipo_magia

    # setter y getters
    @property
    def tipo_magia(self):
        return self.__tipo_magia

    @tipo_magia.setter
    def tipo_magia(self, nuevo_tipo_magia):
        validar_str(nuevo_tipo_magia)
        self.__tipo_magia = nuevo_tipo_magia

    def __str__(self):
        return super().__str__() + "\n" + "    -tipo de magia: {}".format(self.__tipo_magia)


class Mutante(Super_con_poderes):
    '''Clase Mutante hija de Super_con_poderes con los parametros identidad real, id secreta, edad, especie,
    activo, habilidades y debilidades

    ARGS
    -identidad_real: nombre real del super
    -identidad_secreta: nombre del super al publico
    -edad: edad del super
    -especie: especie del super
    -activo: activo yes_no
    -habilidades: lista de habilidades
    -debilidades: lista de debilidades
    -origen: determina el origen de los poderes del super, puede variar entre
            (nacimiento, adquiridos y desconocido)
    -nivel: nivel del mutante categorizado en 3 niveles:
            (alpha, beta, delta)
    '''

    def __init__(self, identidad_real=None, identidad_secreta=None,
                 edad=None, especie=None, activo=None,
                 habilidades=[], debilidades=[],
                 origen=None, nivel=None):
        super().__init__(identidad_real, identidad_secreta, edad, especie, activo,
                         habilidades, debilidades, origen)
        validar_str(nivel)
        if nivel not in ("alpha", "beta", "delta",
                         "Alpha", "Beta", "Delta"):
            raise ValueError("""solo puedes utilizar las siguientes 3 opciones para determinar Nivel:
            -Alpha
            -Beta
            -Delta""")
        self.__nivel = nivel

    # getter y setters
    @property
    def nivel(self):
        return self.__nivel
    @nivel.setter
    def nivel(self, nuevo_nivel):
        validar_str(nuevo_nivel)
        if nuevo_nivel not in ("alpha", "beta", "delta",
                         "Alpha", "Beta", "Delta"):
            raise ValueError("""solo puedes utilizar las siguientes 3 opciones para determinar Nivel:
            -Alpha
            -Beta
            -Delta""")
        self.__nivel = nuevo_nivel

    def __str__(self):
        return super().__str__() + "\n" + "    -nivel: {}".format(self.__nivel)


class Adquiridos(Super_con_poderes):
    '''Clase Adquiridos hija de Super con poderes con los parametros identidad real, id secreta, edad, especie,
    activo, habilidades y debilidades

    ARGS
    -identidad_real: nombre real del super
    -identidad_secreta: nombre del super al publico
    -edad: edad del super
    -especie: especie del super
    -activo: activo yes_no
    -habilidades: lista de habilidades
    -debilidades: lista de debilidades
    -origen: determina el origen de los poderes del super, puede variar entre
            (nacimiento, adquiridos y desconocido)
    -como_fueron_adquiridos: breve historia de como obtuvo sus poderes
    '''

    def __init__(self, identidad_real=None, identidad_secreta=None,
                 edad=None, especie=None, activo=None,
                 habilidades=[], debilidades=[],
                 origen=None, como_fueron_adquiridos=None):
        super().__init__(identidad_real, identidad_secreta, edad, especie, activo,
                         habilidades, debilidades, origen)
        validar_str(como_fueron_adquiridos)
        self.__como_fueron_adquiridos = como_fueron_adquiridos

    # getter y setters
    @property
    def como_fueron_adquiridos(self):
        return self.__como_fueron_adquiridos
    @como_fueron_adquiridos.setter
    def como_fueron_adquiridos(self, nueva_historia):
        validar_str(nueva_historia)
        self.__como_fueron_adquiridos = nueva_historia


if __name__ == "__main__":

    #creacion de todos los supers

    capitan =  Super("Steve", "Capitan America", 264, "humano", True, ["super fuerza", "lento envejecimiento"], ["ninguna"])

    black = Super_sin_poderes("teresa", "black", 32, "humano", True, [], ["las balas"],
                              "raptada para ser asesina profesional desde chica, crecio y se independizo para vengar a su familia")

    iris = Super_con_poderes("iris", "iris", 666, "renacido", False, ["magia cosmica"], ["religion cristiana"],
                             "adquiridos")

    blanca = Magico("vianey", "Miss Blanca", 22, "crogue", False, ["teletransportacion"], ["el color negro"], "nacimiento", "elemental")

    bestia = Mutante("juancho", "mr. beast", 54, "desconocido", True, ["se convierte en bestia"], ["las balas"], "Desconocido", "Beta")

    spiderman = Adquiridos("peter", "spiderman", 19, "humano", True, ["super fuerza", "crea telarañas"], [], "adquiridos",
                           "fue mordido por una araña radioactiva y adquirio sus super poderes")

    #probamos los str de los supers creados
    print(capitan)
    print(black)
    print(iris)
    print(blanca)
    print(bestia)
    print(spiderman)

    #metodos supers
    capitan.lista_debilidades()
    capitan.lista_habilidades()

    #creacion del equipo

    equipo_maravilla = Equipo_super("equipo maravilla", "cuautitlan", True, "06-06-2022",
                                    [capitan, black, iris, blanca, bestia])

    # corroboracion str equipo
    print("___ equipo maravilla str")
    print(equipo_maravilla)

    # prueba de metodos de equipo
    print("___ pruebas de metodos equipo")
    equipo_maravilla.incorporar_al_equipo(spiderman)
    equipo_maravilla.lista_miembros()
    equipo_maravilla.quitar_del_equipo(spiderman)
