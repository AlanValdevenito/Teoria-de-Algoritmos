from automata import Automata

def expresion():
    a = Automata()

    a.estado("Q0", es_inicial=True, es_final=True)
    a.estado("Q1")
    a.estado("Q2")
    a.estado("Q3")
    a.estado("Q4")
    a.estado("Q5")
    a.estado("Q6", es_final=True)

    # Transiciones para (aab)*
    a.transicion_estado("Q0", "Q1", "a")
    a.transicion_estado("Q1", "Q2", "a")
    a.transicion_estado("Q2", "Q3", "b")
    a.transicion_estado("Q2", "Q3", "")
    a.transicion_estado("Q3", "Q0", "")

    # Transiciones para (a, aba)*
    a.transicion_estado("Q0", "Q4", "a")
    a.transicion_estado("Q4", "Q6", "")
    a.transicion_estado("Q4", "Q5", "b")
    a.transicion_estado("Q5", "Q6", "a")

    a.transicion_estado("Q6", "Q4", "")

    return a