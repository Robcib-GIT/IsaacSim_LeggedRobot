
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import math

def calcula_velocidad_x(diferencia_x):
    # Definir las variables de entrada y salida
    Pos_x = ctrl.Antecedent(np.arange(-5, 5, 1), 'Pos_x')
    velocidad_x = ctrl.Consequent(np.arange(0, 1.5, 0.01), 'velocidad_x')

    # Funciones de pertenencia para Pos_x
    Pos_x['poor'] = fuzz.trapmf(Pos_x.universe, [-5, -5, -5/18, -5/24])
    Pos_x['mediocre'] = fuzz.trimf(Pos_x.universe, [-5/6, -5/18, 0])
    Pos_x['average'] = fuzz.trimf(Pos_x.universe, [-5/18, 0, 5/18])
    Pos_x['decent'] = fuzz.trimf(Pos_x.universe, [0, 5/18, 5/6])
    Pos_x['good'] = fuzz.trapmf(Pos_x.universe, [5/24, 5/18, 5, 5])

    # Funciones de pertenencia para velocidad_x
    velocidad_x['muy_baja'] = fuzz.trimf(velocidad_x.universe, [0, 0, 0.15])
    velocidad_x['baja'] = fuzz.trimf(velocidad_x.universe, [0, 0.15, 0.2])
    velocidad_x['media'] = fuzz.trimf(velocidad_x.universe, [0.15, 0.2, 0.3])
    velocidad_x['alta'] = fuzz.trimf(velocidad_x.universe, [0, 0.2, 0.75])
    velocidad_x['muy_alta'] = fuzz.trimf(velocidad_x.universe, [0.75, 1.5, 1.5])

    # Reglas difusas
    regla1 = ctrl.Rule(Pos_x['poor'], velocidad_x['alta'])
    regla2 = ctrl.Rule(Pos_x['mediocre'], velocidad_x['media'])
    regla3 = ctrl.Rule(Pos_x['average'], velocidad_x['muy_baja'])
    regla4 = ctrl.Rule(Pos_x['decent'], velocidad_x['media'])
    regla5 = ctrl.Rule(Pos_x['good'], velocidad_x['alta'])

    # Crear el sistema de control
    sistema_control = ctrl.ControlSystem([regla1, regla2, regla3, regla4, regla5])
    simulacion = ctrl.ControlSystemSimulation(sistema_control)

    # Asignar la entrada al sistema
    simulacion.input['Pos_x'] = diferencia_x

    # Ejecutar la simulación
    simulacion.compute()

    # Devolver el valor de la velocidad
    return simulacion.output['velocidad_x']

def calcula_velocidad_y(diferencia_y):
    # Definir las variables de entrada y salida
    Pos_y = ctrl.Antecedent(np.arange(-5, 5, 1), 'Pos_y')
    velocidad_y = ctrl.Consequent(np.arange(-1.5, 1.5, 0.01), 'velocidad_y')

    # Funciones de pertenencia para Pos_y
    Pos_y['poor'] = fuzz.trapmf(Pos_y.universe, [-5, -5, -5/18, -5/24])
    Pos_y['mediocre'] = fuzz.trimf(Pos_y.universe, [-5/6, -5/18, 0])
    Pos_y['average'] = fuzz.trimf(Pos_y.universe, [-5/18, 0, 5/18])
    Pos_y['decent'] = fuzz.trimf(Pos_y.universe, [0, 5/18, 5/6])
    Pos_y['good'] = fuzz.trapmf(Pos_y.universe, [5/24, 5/18, 5, 5])

    # Funciones de pertenencia para velocidad_y
    velocidad_y['muy_baja'] = fuzz.trimf(velocidad_y.universe, [0, 0, 0.15])
    velocidad_y['baja'] = fuzz.trimf(velocidad_y.universe, [0, 0.15, 0.2])
    velocidad_y['media'] = fuzz.trimf(velocidad_y.universe, [0.15, 0.2, 0.3])
    velocidad_y['alta'] = fuzz.trimf(velocidad_y.universe, [0, 0.2, 0.75])
    velocidad_y['muy_alta'] = fuzz.trimf(velocidad_y.universe, [0.75, 1.5, 1.5])

    # Reglas difusas
    regla1 = ctrl.Rule(Pos_y['poor'], velocidad_y['alta'])
    regla2 = ctrl.Rule(Pos_y['mediocre'], velocidad_y['media'])
    regla3 = ctrl.Rule(Pos_y['average'], velocidad_y['muy_baja'])
    regla4 = ctrl.Rule(Pos_y['decent'], velocidad_y['media'])
    regla5 = ctrl.Rule(Pos_y['good'], velocidad_y['baja'])

    # Crear el sistema de control
    sistema_control = ctrl.ControlSystem([regla1, regla2, regla3, regla4, regla5])
    simulacion = ctrl.ControlSystemSimulation(sistema_control)

    # Asignar la entrada al sistema
    simulacion.input['Pos_y'] = diferencia_y  # Corregí aquí a 'Pos_y'

    # Ejecutar la simulación
    simulacion.compute()

    # Devolver el valor de la velocidad
    return simulacion.output['velocidad_y']


def Angulo_Giro(diferencia_theta):
    # Definir las variables de entrada y salida
    Theta = ctrl.Antecedent(np.arange(-180, 180, 1), 'Theta')
    Variacion_Theta = ctrl.Consequent(np.arange(-1.5, 1.5, 0.01), 'Variacion_Theta')  # Ajustado a -0.6 a 0.6

    # Funciones de pertenencia para Theta
    Theta['poor'] = fuzz.trapmf(Theta.universe, [-180, -180, -20, -5])
    Theta['mediocre'] = fuzz.trimf(Theta.universe, [-10, -5, 0])
    Theta['average'] = fuzz.trimf(Theta.universe, [-5, 0, 5])
    Theta['decent'] = fuzz.trimf(Theta.universe, [0, 5, 10])
    Theta['good'] = fuzz.trapmf(Theta.universe, [5, 20, 180, 180])

    # Funciones de pertenencia para Variacion_Theta
    Variacion_Theta['muy_baja'] = fuzz.trimf(Variacion_Theta.universe, [-1.5, -1.5, -0.75])
    Variacion_Theta['baja'] = fuzz.trimf(Variacion_Theta.universe, [-1.5, -0.75, 0])
    Variacion_Theta['media'] = fuzz.trimf(Variacion_Theta.universe, [-0.75, 0, 0.75])
    Variacion_Theta['alta'] = fuzz.trimf(Variacion_Theta.universe, [0, 0.75, 1.5])
    Variacion_Theta['muy_alta'] = fuzz.trimf(Variacion_Theta.universe, [0.75, 1.5, 1.5])

    # Reglas difusas
    regla1 = ctrl.Rule(Theta['poor'], Variacion_Theta['muy_alta'])
    regla2 = ctrl.Rule(Theta['mediocre'], Variacion_Theta['media'])
    regla3 = ctrl.Rule(Theta['average'],Variacion_Theta['media'])
    regla4 = ctrl.Rule(Theta['decent'], Variacion_Theta['media'])
    regla5 = ctrl.Rule(Theta['good'], Variacion_Theta['muy_baja'])

    # Crear el sistema de control
    sistema_control = ctrl.ControlSystem([regla1, regla2, regla3, regla4, regla5])
    simulacion = ctrl.ControlSystemSimulation(sistema_control)

    # Asignar la entrada al sistema
    simulacion.input['Theta'] = diferencia_theta  # Corregí aquí a 'Pos_y'

    # Ejecutar la simulación
    simulacion.compute()

    # Devolver el valor de la velocidad
    return simulacion.output['Variacion_Theta']


