import os
import random as rm

from abc import ABC, abstractmethod

"""Inicio de la definición de clases"""

"""Clase  Ciudades se usa porque hay ciudades que tienen varias equipos, en la misma o diferentes ligas"""
class Ciudades:
    #Clase para las ciudades donde habría una franquicia de algúna  liga
    def __init__(self, nombre_ciudad):
        self.nombre_ciudad = nombre_ciudad

"""Clase Estadios se usa para definir wel estadio en el que juega un equipo. Existen equipos que comparten el mismo estadio"""
class Estadios:
    #Clase para el  nomvre del estadio donde juega la franquicia
    def __init__(self, nombre_estadio):
        self.nombre_estadio = nombre_estadio

"""DClase Ligas define las ligas de deportes que se van a cargar"""
class Ligas:
    #Clase para las ligas de deportes
    def __init__(self, nombre_liga, nick_name_liga, deporte):
        self.nombre_liga = nombre_liga
        self.nick_name_liga = nick_name_liga
        self.deporte = deporte

    @property
    def nick_name_liga(self):
        """Getter de nick_name_liga"""
        return self._nick_name_liga
    
    @nick_name_liga.setter
    def nick_name_liga(self,valor):
        if valor not in ligas_registradas:
            agregar_liga =  input("¿Deseas agregar la liga al catálogo (S/N)?: ")
            if agregar_liga.lower()=="s":
                ligas_registradas.append(valor)
        self._nick_name_liga = valor

"""Clase Equipos defone la información de un equupo en un liga, ciudad y estadio"""
class Equipos(Ligas, Ciudades, Estadios):
    #Clase para las franquicias
    def __init__(self, nombre_franquicia, nick_name_franquicia, costo_estimado, nombre_liga, nick_name_liga, deporte, nombre_ciudad, nombre_estadio):
        Ligas.__init__(self,nombre_liga, nick_name_liga, deporte)
        Ciudades.__init__(self, nombre_ciudad)
        Estadios.__init__(self, nombre_estadio)
        self.nombre_franquicia = nombre_franquicia
        self.nick_name_franquicia = nick_name_franquicia
        self.__costo_estimado = costo_estimado

    @property
    def nick_name_liga(self):
        """Getter de nick_name_liga"""
        return self._nick_name_liga
    
    @nick_name_liga.setter
    def nick_name_liga(self,valor):
        if valor not in ligas_registradas:
            raise ValueError(f"La liga {valor} no se encuentra registrada")
        self._nick_name_liga = valor

    def informacion_franqucia(self):
        return f"Somos los {self.nick_name_franquicia} de {self.nombre_franquicia}. Un equipo de {self.deporte} de la {self.nick_name_liga} - {self.nombre_liga}\nJugamos en la ciudad de {self.nombre_ciudad}\nEl estadio donde jugamos se llama {self.nombre_estadio}"

    def _calcular_impuesto(self):
        if self.deporte == "Baseball" and self.__costo_estimado > 250000000:
            return f"La franquicia {self.nombre_franquicia} {self.nick_name_franquicia} tiene un impuesto de lujo por ${(self.__costo_estimado*.16):.2f}"
        else:
            return f"Para la liga {self.nombre_liga} no aplica el impuesto de lujo"

"""clases para poder armar el calendario de una temporada"""
class Temporada:
    def __init__(self, año_temporda):
        self.año_temporada = año_temporda

    def Liga(self):
        return ""

"""Clase para definir las semanas que conforman una temporada en la NFL"""
class SemanaNFL(Temporada):
    def __init__(self, año_temporda, numero_semana):
        super().__init__(año_temporda)
        self.numero_semana = numero_semana
        self.equipos_juego = []

    def Liga(self):
        return "NFL"
    
    def agregar_equipo(self, fecha_juego, hora_juego, equipo_local, equipo_visita, estadio, ciudad):

        lista_equipos = [self.año_temporada,self.numero_semana,fecha_juego,hora_juego,equipo_local,equipo_visita,estadio,ciudad]
        self.equipos_juego.append(lista_equipos)

    def listar_calendario(self):
        return self.equipos_juego

"""Clase JOrnadaMLB define el calendario de una tempofrada de la MLB (a diferencia de la NFL no se rigue por semanas sino por juegos en jornadas diarias)"""
class JornadaMLB(Temporada):
    def __init__(self, año_temporda,fecha_jornada):
        super().__init__(año_temporda)
        self.fecha_jornada = fecha_jornada
        self.equipos_juego = []

    def Liga(self):
        return "MLB"

    def agregar_equipo(self, hora_juego, equipo_local, equipo_visita, estadio, ciudad):

        lista_equipos = [self.año_temporada,self.fecha_jornada,hora_juego,equipo_local,equipo_visita,estadio,ciudad]
        self.equipos_juego.append(lista_equipos)

    def listar_calendario(self):
        return self.equipos_juego

"""Fin de clases para armar calendario"""

"""Clase Jugadores define los datos generles de un jugador o deportista sin importar loga o equipo"""
class Jugadores:
    def __init__(self, nombre_jugador, apellido_jugador, nacionalidad_jugador):
        self._id_jugador = ""
        self.nombre_jugador = nombre_jugador
        self.apellido_jugador = apellido_jugador
        self.nacionalidad_jugador = nacionalidad_jugador

    def generar_id_jugador(self):
        return f"{self.nombre_jugador[0]}{self.apellido_jugador[0]}{self.nacionalidad_jugador[0:3]}-{str(rm.randint(1,999999)).zfill(6)}"

"""Clase Jugadores_equipos registra un jugador en un equipo"""
class Jugadores_equipos(Jugadores):

    """Valriable para vaidar que el equipo este registrado"""
    equipo_encontrado = False
    indice_equipo_encontrado = -1
    datos_equipo = []

    def __init__(self, nombre_jugador, apellido_jugador, nacionalidad_jugador, nick_name_equipo, nick_name_liga):
        super().__init__(nombre_jugador, apellido_jugador, nacionalidad_jugador)
        self.nick_name_equipo = nick_name_equipo
        self.nick_name_liga = nick_name_liga
        self.__años_contrato = None
        self.__monto_contrato = None
        self.nmuero_jersey = None
        self.posicion = None
        self.historico_jugadas = []

    @property 
    def nick_name_equipo(self):
        """Getter de nick_name_equipo"""
        return self._nick_name_equipo

    @nick_name_equipo.setter
    def nick_name_equipo(self,valor):
        for a, item_equipo in enumerate(equipos_registrados):
            if item_equipo[0]==valor:
                self.equipo_encontrado = True
                self.indice_equipo_encontrado = a
                break
        if self.equipo_encontrado == False:
            raise ValueError("Equipo no registrado")
        self._nick_name_equipo = valor

    @property
    def nick_name_liga(self):
        """Getter de nick_name_liga"""
        return self._nick_name_liga
    
    @nick_name_liga.setter
    def nick_name_liga(self,valor):
        if self.equipo_encontrado == True:
            self.datos_equipo = equipos_registrados[self.indice_equipo_encontrado]
            if self.datos_equipo[1] != valor:
                raise ValueError("El equipo y la liga no coinciden")
        self._nick_name_liga = valor

    def _registrar_contrato(self, años, monto):
        if años>0 and monto>0:
            self.__años_contrato = años
            self.__monto_contrato = monto
            return True
        return False

    def ver_contrato(self):
        print(f"El contrato de {self.nombre_jugador} {self.apellido_jugador} es por {self.__años_contrato} años y un monto de ${self.__monto_contrato:.2f}")

    def _asignar_numero_posicion(self,numero,posicion):
        if numero>0 and len(posicion)>0:
            self.nmuero_jersey = numero
            self.posicion = posicion
            return True
        return False

    def registrar_jugada(self, informacion_jugada):
        """Método privado: solo uso interno"""
        self.historico_jugadas.append(informacion_jugada)

"""Funciones poliformismos"""
"""Clase jugada registra un jugada de cualquier deporte"""
class Jugada(ABC):
    @abstractmethod
    def tipo_jugada(self):
        pass
    @abstractmethod
    def resultado_jugada():
        pass

"""Registra la información de una jugada de pase en el fútbol americano"""
class Lanzar_pase(Jugada):
    def __init__(self,resultado_pase,yardas_pase):
        self.resultado_pase = resultado_pase
        self.yardas_pase = yardas_pase

    def tipo_jugada(self):
        return "Pase"
    
    def resultado_jugada(self):
        return self.resultado_pase

    def yardas_jugada(self):
        return self.yardas_pase

"""Registra la información de un acarreo en el fútbol americano"""
class Carrera(Jugada):
    def __init__(self, resultado_carrera, yardas_carrera):
        self.resultado_carrera = resultado_carrera
        self.yardas_carrera = yardas_carrera

    def tipo_jugada(self):
        return "Acarreo"
    
    def resultado_jugada(self):
        return self.resultado_carrera

    def yardas_jugada(self):
        return self.yardas_carrera

def historico_jugadas_individual(lista_jugadas):
    for item_jugadas in lista_jugadas:
        print(f"Jugada:{item_jugadas['tipo_jugada']} Resultado:{item_jugadas['resultado_jugada']} Yardas: {item_jugadas['yardas_jugada']}")
    print("\n")

def estadisrticas_pase_individual(lista_jugadas):
    intentos = 0
    completos = 0
    incompletos = 0
    interceptados = 0
    yardas = 0
    capturas = 0
    capturas_yardas = 0

    for item_jugada in lista_jugadas:
        if item_jugada['tipo_jugada'] == "Pase":
            intentos +=1
            match item_jugada['resultado_jugada']:
                case "Completo":
                    completos +=1
                    yardas += item_jugada['yardas_jugada']
                case "Incompleto":
                    incompletos +=1
                    yardas += item_jugada['yardas_jugada']
                case "Interceptado":
                    interceptados +=1
                    yardas += item_jugada['yardas_jugada']
                case "Captura":
                    capturas +=1
                    capturas_yardas = item_jugada['yardas_jugada']

    print(f"{'Intentos':^20}{'Completos':^20}{'Incompletos':^20}{'Interceptados':^20}{'Yardas':^20}")
    print(f"{intentos:^20}{completos:^20}{incompletos:^20}{interceptados:^20}{yardas:^20}")
    print(f"Sacks {capturas:^10}Yardas perdidas {(capturas_yardas*-1):^10}")
    print("\n")

"""Fin de la definición de clases"""

os.system("cls")

ligas_registradas = ["NFL","MLB"]
equipos_registrados = []

print("Antes de agregar la lista","-"*50)
print(ligas_registradas)
nueva_liga=Ligas("National Hocey League","NHL","Hockey")
print("Después de agregar la liga","-"*50)      
print(ligas_registradas)
print("\n")


"""Onjetos de equipos"""
Patriotas = Equipos("Nwe England","Patriots",1,"National Football League","NFL","Football","Masachustetts","Gillet Stadium")
HalconesMarionos = Equipos("Seattle","Seahawks",1,"National Football League","NFL","Football","Washington","Haclones Fiels")
Acereros = Equipos("Pittsburgh","Steelers",123000000,"National Football League","NFL","Football","Pittsburgh, PA.","Acrisure field")
Halcones = Equipos("Atlanta","Falcons",1,"National Football League","NFL","Football","Wisconsin","Lambue Field")
Rams = Equipos("Los Angeles","Rams",180000000,"National Football League","NFL","Football","Los Angeles, Cal.","Sofi stadium")
CuarentaNueves = Equipos("San Francisco","49es",180000000,"National Football League","NFL","Football","San Francisco, Cal.","Levis's Stadium")
Cargadores = Equipos("Los Angeles",120000000,"Chargers","National Football League","NFL","Football","Los Angeles, Cal.","Sofi stadium")
Rangers = Equipos("New York","Rangers",200000000,"National Hockey League","NHL","Hockey","New York","Madison Square Garden")

"""Objetos de temporadas"""
Temporada1 = Temporada(2026)

"""Objetos para el calendario de la NFL"""
Semana1 = SemanaNFL(Temporada1.año_temporada,"week 1")
Semana2 = SemanaNFL(Temporada1.año_temporada,"week 2")
Semana3 = SemanaNFL(Temporada1.año_temporada,"week 3")
Semana4 = SemanaNFL(Temporada1.año_temporada,"week 4")
Semana5 = SemanaNFL(Temporada1.año_temporada,"week 5")
Semana6 = SemanaNFL(Temporada1.año_temporada,"week 6")
Semana7 = SemanaNFL(Temporada1.año_temporada,"week 7")
Semana8 = SemanaNFL(Temporada1.año_temporada,"week 8")
Semana9 = SemanaNFL(Temporada1.año_temporada,"week 9")
Semana10 = SemanaNFL(Temporada1.año_temporada,"week 10")
Semana11 = SemanaNFL(Temporada1.año_temporada,"week 11")
Semana12 = SemanaNFL(Temporada1.año_temporada,"week 12")
Semana13 = SemanaNFL(Temporada1.año_temporada,"week 13")
Semana14 = SemanaNFL(Temporada1.año_temporada,"week 14")
Semana15 = SemanaNFL(Temporada1.año_temporada,"week 15")
Semana16 = SemanaNFL(Temporada1.año_temporada,"week 16")
Semana17 = SemanaNFL(Temporada1.año_temporada,"week 17")
Semana18 = SemanaNFL(Temporada1.año_temporada,"week 18")

"""Calencdario de la NFL"""
Semana1.agregar_equipo("9/09/2026","18:00",HalconesMarionos.nick_name_franquicia,Patriotas.nick_name_franquicia,Patriotas.nombre_estadio,Patriotas.nombre_ciudad)
Semana1.agregar_equipo("10/09/2026","18:00",Rams.nick_name_franquicia,CuarentaNueves.nick_name_franquicia,CuarentaNueves.nombre_estadio,CuarentaNueves.nombre_ciudad)
Semana1.agregar_equipo("13/09/2026","18:00",Acereros.nick_name_franquicia,Halcones.nick_name_franquicia,Halcones.nombre_estadio,Halcones.nombre_ciudad)


"""Objetos de equipos de la MLB"""
Dodgers = Equipos("Los Angeles","Dodgers",300000000,"Major League Baseball","MLB","Baseball","Los Angeles, Cal.","Dodgers stadium")
Yankees = Equipos("New York","Yankees",300000000,"Major League Baseball","MLB","Baseball","New York, NY.","Yankee Stadium")

"""Objetos para una jornada en la MLB"""
Jornada1 = JornadaMLB(Temporada1.año_temporada,"16/05/2026")
Jornada1.agregar_equipo("17:00",Yankees.nick_name_franquicia,Dodgers.nick_name_franquicia,Yankees.nombre_estadio,Yankees.nombre_ciudad)

print(f"Calendario para la {Semana1.Liga()}")
for item_calendario in Semana1.listar_calendario():
    print(item_calendario)

print(f"Calendario para la {Jornada1.Liga()}")
for item_calendario in Jornada1.listar_calendario():
    print(item_calendario)


print(Acereros.informacion_franqucia())
print(Acereros._calcular_impuesto())
equipos_registrados.append([Acereros.nick_name_franquicia,Acereros._nick_name_liga])
print("\n")

print(Dodgers.informacion_franqucia())
print(Dodgers._calcular_impuesto())
equipos_registrados.append([Dodgers.nick_name_franquicia,Dodgers._nick_name_liga])
print("\n")

print(Rams.informacion_franqucia())
print(Rams._calcular_impuesto())
equipos_registrados.append([Rams.nick_name_franquicia,Rams._nick_name_liga])
print("\n")

print(Cargadores.informacion_franqucia())
print(Cargadores._calcular_impuesto())
equipos_registrados.append([Cargadores.nick_name_franquicia,Cargadores._nick_name_liga])
print("\n")

print(Rangers.informacion_franqucia())
print(Rangers._calcular_impuesto())
equipos_registrados.append([Rangers.nick_name_franquicia,Rangers._nick_name_liga])
print("\n")

print("Dar de alta jugadores","-"*50)
Jugador1 = Jugadores("Augusto","Lorenzo","Mexicano")
Jugador1._id_jugador = Jugador1.generar_id_jugador()
print(Jugador1._id_jugador,Jugador1.nombre_jugador)

Jugador2 = Jugadores("Juan Manuel","Lorenzo","Mexicano")
Jugador2._id_jugador = Jugador2.generar_id_jugador()
print(Jugador2._id_jugador,Jugador2.nombre_jugador)
print("\n")

print("Asignar equipos a los jugadores","-"*50)
jugador_equipo1 = Jugadores_equipos("Augusto","Lorenzo","Mexicano","Steelers","NFL")
print(f"El jugador {jugador_equipo1.nombre_jugador} {jugador_equipo1.apellido_jugador} fue dado de alta en el equipo {jugador_equipo1.nick_name_equipo} de la liga {jugador_equipo1.nick_name_liga}")

jugador_equipo2 = Jugadores_equipos("Juan Manuel","Lorenzo","Mexicano","Steelers","NFL")
print(f"El jugador {jugador_equipo2.nombre_jugador} {jugador_equipo2.apellido_jugador} fue dado de alta en el equipo {jugador_equipo2.nick_name_equipo} de la liga {jugador_equipo2.nick_name_liga}")
print("\n")

jugador_equipo1._registrar_contrato(3,10000000)
jugador_equipo1._asignar_numero_posicion(32,"Corredor")
print(jugador_equipo1.ver_contrato())
print(f"Al jugador {jugador_equipo1.nombre_jugador} {jugador_equipo1.apellido_jugador} en la posición {jugador_equipo1.posicion} le fue asignado el número {jugador_equipo1.nmuero_jersey}")
jugador_equipo2._registrar_contrato(4,13000000)
jugador_equipo2._asignar_numero_posicion(12,"QuarterBack")
print(jugador_equipo2.ver_contrato())
print(f"Al jugador {jugador_equipo2.nombre_jugador} {jugador_equipo2.apellido_jugador} en la posición {jugador_equipo2.posicion} le fue asignado el número {jugador_equipo2.nmuero_jersey}")
print("\n")

print("Registro de una jugadas","-"*50)
lista_jugadas = [
Lanzar_pase("Completo",25),
Lanzar_pase("Incompleto",0),
Lanzar_pase("Interceptado",-10),
Lanzar_pase("Captura",-5),
Lanzar_pase("Balón suelto",-1),
Carrera("Positivo",10)
]
print(f"Yardas acumuladas en las jugadas: {sum(item_jugadas.yardas_jugada() for item_jugadas in lista_jugadas)}")
print("\n")

lista_jugadas1 = [
    Carrera("Positivo",3),
    Carrera("Positivo",6),
    Carrera("Pérdida",1)
]
print(f"Yardas acumuladas en las jugadas: {sum(item_jugadas.yardas_jugada() for item_jugadas in lista_jugadas1)}")
print("\n")

#Registro de jugadas y consulta edl historial por jujador
for item_jugadas in lista_jugadas:
    datos_jugada = {
        'tipo_jugada': item_jugadas.tipo_jugada(),
        'resultado_jugada': item_jugadas.resultado_jugada(),
        'yardas_jugada': item_jugadas.yardas_jugada()
    }
    jugador_equipo2.registrar_jugada(datos_jugada)
print(f"Jugador {jugador_equipo2.nombre_jugador} {jugador_equipo2.apellido_jugador}, {jugador_equipo2.posicion} de {jugador_equipo2.nick_name_equipo}")
print("Historial de jugadas","-"*50)
historico_jugadas_individual(jugador_equipo2.historico_jugadas)

for item_jugadas in lista_jugadas1:
    datos_jugada = {
        'tipo_jugada': item_jugadas.tipo_jugada(),
        'resultado_jugada': item_jugadas.resultado_jugada(),
        'yardas_jugada': item_jugadas.yardas_jugada()
    }
    jugador_equipo1.registrar_jugada(datos_jugada)
print("Historial de jugadas","-"*50)
print(f"Jugador {jugador_equipo1.nombre_jugador} {jugador_equipo1.apellido_jugador}, {jugador_equipo1.posicion} de {jugador_equipo1.nick_name_equipo}")
historico_jugadas_individual(jugador_equipo1.historico_jugadas)

print("Estadísticas de pase","-"*50)
print(f"Jugador {jugador_equipo2.nombre_jugador} {jugador_equipo2.apellido_jugador}, {jugador_equipo2.posicion} de {jugador_equipo2.nick_name_equipo}")
estadisrticas_pase_individual(jugador_equipo2.historico_jugadas)
