import requests
import numpy as np
import pprint
import random
from itertools import chain

# API URL
beacon_url = "https://beacon.clcert.cl/beacon/2.1-beta/pulse"


# Random UChile
def get_last_pulse():
    content = requests.get(beacon_url)

    # JSON containing all the pulse data
    pulse = content.json()["pulse"]

    # Random string of 512 bits obtained from the pulse
    seed = pulse["outputValue"]

    # This index will be used by the observer to verify the process
    pulse_index = pulse["pulseIndex"]

    return pulse_index, seed


# Random Drand
def get_drand_randomness():
    
    # URL de la API de drand Quicknet
    url = "https://api.drand.sh/52db9ba70e0cc0f6eaf7803dd07447a1f5477735fd3f661792ba94600c84e971/public/latest"

    # Realizar la petición HTTP GET
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Parsear el JSON de la respuesta
        randomness_data = response.json()

        # Extraer información importante
        round_number = randomness_data["round"]
        randomness_value = randomness_data["randomness"]

        # print(f"Ronda: {round_number}")
        # print(f"Aleatoriedad: {randomness_value}")

        return round_number, randomness_value
    else:
        print("Error al obtener los datos de drand")
        return None


# Función para crear un sample de n elementos de una lista
def sample_list(n, l):
    pulse_index, seed = get_drand_randomness()
    random.seed(seed)
    return random.sample(l, n)


# Recibo lista de riesgosos, lista de no riesgosos y capacidad de revisión n
# 90% riesgosos - 10% no riesgosos, si queda espacio se llena con no riesgosos
# Entregar no riesgosos que terminan en el conjunto final
def risk_nonrisk_sample(risk, non_risk, n):
    # Random UChile
    # pulse_index, seed = get_last_pulse()

    # Random Drand
    pulse_index, seed = get_drand_randomness()

    # Seed
    random.seed(seed)
    
    # Tries
    tries = 0

    # Si hay más riesgosos que la capacidad de revisión, se toma una muestra de riesgosos
    # Si no, se toma la lista completa
    if len(risk) >= int(n * 0.9):
        risk_sample = random.sample(risk, int(n * 0.9))
        tries += 1
    else:
        risk_sample = risk

    non_risk_sample = non_risk.copy()
    random.shuffle(non_risk_sample)
    tries += 1
    non_risk_sample = non_risk_sample[: n - len(risk_sample)]

    # Asociación final
    final_sample = risk_sample + non_risk_sample

    print("Pulse index (drand): {}".format(pulse_index))
    print("Seed: {}".format(seed))
    print("Riesgosos: {}".format(risk_sample))
    print("No riesgosos: {}".format(non_risk_sample))
    print("Muestra final: {}".format(final_sample))
    return final_sample, non_risk_sample, pulse_index, tries


# Función para asociar inspectores con contenedores
# C: Lista de contenedores
# I: Lista de inspectores
# n: Cantidad de contenedores por inspector
def run_association(C, I, n=5):
    # Random UChile
    # pulse_index, seed = get_last_pulse()

    # Random Drand
    pulse_index, seed = get_last_pulse()

    # Seed
    random.seed(seed)
    
    # Tries
    tries = 0

    random.shuffle(I)
    tries += 1
    random.shuffle(C)
    tries += 1

    # Asociación Inspector - Contenedores
    association = {}

    subC = C.copy()
    for inspector in I:
        sample = random.sample(subC, n)
        tries += 1
        for x in sample:
            subC.remove(x)
        # print(subN)
        association[inspector] = sample

    print("Pulse index (ruchile): {}".format(pulse_index))
    print("Seed: {}".format(seed))
    pprint.pprint(association)
    # print(association.values())
    return association, pulse_index, tries


def test_run_association():

    # Contenedores
    containers = [i for i in range(1, 101)]
    # N = np.arange(1, 101)

    # Inspectores de Aduana
    inspectores = [i for i in range(1, 21)]
    # M = np.arange(1, 21)

    # Call the function to get the association
    association = run_association(containers, inspectores)

    # Get the values from the association dictionary
    values = association.values()

    # Check if the values inside the lists are unique
    n = np.array(chain.from_iterable(values))

    # Frequency of each element in the array
    unique, counts = np.unique(n, return_counts=True)

    # Check if there are repeated values
    repeated = unique[counts > 1]
    print("Repeated", repeated)


# test_run_association()
