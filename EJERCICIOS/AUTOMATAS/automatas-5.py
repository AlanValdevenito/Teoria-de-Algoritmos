from automata import Automata

def expresion():
    a = Automata()
    
    a.estado("Q0", es_inicial = True)
    a.estado("Q1")
    a.estado("Q2")
    a.estado("Q3")
    a.estado("Q4")
    a.estado("Q5", es_final = True)

    a.transicion_estado("Q0", "Q1", "a")
    a.transicion_estado("Q0", "Q4", "")

    a.transicion_estado("Q1", "Q2", "b")

    a.transicion_estado("Q2", "Q1", "a")
    a.transicion_estado("Q2", "Q3", "b")
    a.transicion_estado("Q2", "Q5", "")

    a.transicion_estado("Q3", "Q3", "a")
    a.transicion_estado("Q3", "Q5", "")

    a.transicion_estado("Q4", "Q1", "")
    a.transicion_estado("Q4", "Q4", "b")
    a.transicion_estado("Q4", "Q5", "")

    return a