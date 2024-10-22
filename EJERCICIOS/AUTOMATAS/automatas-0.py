from automata import Automata

def automata_al_menos_3_0s():
    a = Automata()
    
    a.estado("Q0", es_inicial = True)
    a.estado("Q1")
    a.estado("Q2")
    a.estado("Q3", es_final = True)

    a.transicion_estado("Q0", "Q0", "1")
    a.transicion_estado("Q0", "Q1", "0")

    a.transicion_estado("Q1", "Q0", "1")
    a.transicion_estado("Q1", "Q2", "0")

    a.transicion_estado("Q2", "Q0", "1")
    a.transicion_estado("Q2", "Q3", "0")

    a.transicion_estado("Q3", "Q3", "0")
    a.transicion_estado("Q3", "Q0", "1")

    return a