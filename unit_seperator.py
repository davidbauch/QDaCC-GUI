# Seperates a value from its unit
# Units trailable include:
# s,ms,mus,ns,ps,fs
# Hz, eV, meV, mueV
# pi


def seperate_unit(value: str):
    units_trail = ["ms","mus","ns","ps","fs","Hz","meV","mueV","pi","eV","s"]
    scalings_unit = {"s" : 1, "ms" : 1E-3, "mus" : 1E-6, "ns" : 1E-9, "ps" : 1E-12, "fs" : 1E-15, "Hz" : 1, "eV" : 1, "meV" : 1E-3, "mueV" : 1E-6, "pi" : 1}
    if not any( [a in value for a in units_trail] ):
        return value,"",1
    index = [i for i,a in enumerate(units_trail) if a in value]
    if len(index) == 0:
        return value,"",1
    index = index[0]
    unit = units_trail[index]
    value = value.replace( unit, "" )
    return value, unit, scalings_unit[unit]

def get_unit_value(value: str):
    v,_,_ = seperate_unit(value)
    return float(v)
def get_unit(value: str):
    _,u,_ = seperate_unit(value)
    return u
def get_unit_scaling(value: str):
    _,_,s = seperate_unit(value)
    return float(s)
def get_uv_scaled(value: str):
    v,_,s = seperate_unit(value)
    return float(v)*float(s)

if __name__ == "__main__":
    print(f"This file ({__file__}) is part of the QDLC GUI and should be imported, not executed.")