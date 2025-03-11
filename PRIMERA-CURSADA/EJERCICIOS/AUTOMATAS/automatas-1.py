from automata import Automata

def automata_potencias_2():
    a = Automata()

    a.estado("Q0", es_inicial = True)
    a.estado("Q1", es_final = True)

    a.transicion_estado("Q0", "Q0", "0")
    a.transicion_estado("Q0", "Q1", "1")

    a.transicion_estado("Q1", "Q1", "0")

    return a