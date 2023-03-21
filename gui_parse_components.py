from unit_seperator import  get_uv_scaled

def _parse_electronic_system(components: dict, escape_symbol: str = "'", callback = None) -> str:
    ret = ""
    for level in sorted(components["EnergyLevels"].values(), key = lambda a: get_uv_scaled(a["Energy"])):
        n,e,d,c,p,to = level["Name"], level["Energy"], level["DephasingScaling"], level["DecayScaling"], level["PhononScaling"], ",".join(level["CoupledTo"]) if level["CoupledTo"] != (None,) and len(level["CoupledTo"]) > 0 else "-"
        ret += f"{n}:{e}:{to}:{d}:{c}:{p};"
    return f"--SE {escape_symbol}{ret[:-1]}{escape_symbol}"

def _parse_cavity_system(components: dict, escape_symbol: str = "", callback = None) -> str:
    ret = ""
    for cavity in sorted(components["CavityLevels"].values(), key = lambda a: get_uv_scaled(a["Energy"])):
        n,e,t,ts,ds,p = cavity["Name"], cavity["Energy"], ",".join(cavity["CoupledTo"]), ",".join([str(a) for a in cavity["CoupledToScalings"]]), cavity["DecayScaling"], cavity["PhotonNumber"]
        ret += f"{n}:{e}:{p}:{t}:{ts}:{ds};"
    if len(ret) > 0:
        return f"--SO {escape_symbol}{ret[:-1]}{escape_symbol}"
    return ret

def _parse_pulse_system(components: dict, escape_symbol: str = "", callback = None) -> str:
    ret = ""
    for pulse in components["Pulse"].values():
        n,ct,a,f,c,w,t = pulse["Name"], pulse["CoupledTo"], pulse["Amplitudes"], pulse["Frequencies"], pulse["Centers"], pulse["Widths"], pulse["Type"]
        a,f,c,w,t = ",".join(a), ",".join(f), ",".join(c), ",".join(w), ",".join(t)
        ret += f"{n}:{','.join(ct)}:{a}:{f}:{w}:{c}:{t};"
    if len(ret) > 0:
        return f"--SP {escape_symbol}{ret[:-1]}{escape_symbol}"
    return ret

def _parse_shift_system(components: dict, escape_symbol: str = "", callback = None) -> str:
    ret = ""
    for shift in components["Shift"].values():
        n,t,a,k,s,sc = shift["Name"], shift["Times"], shift["Amplitudes"], shift["Type"], shift["CoupledTo"], shift["CoupledToScalings"]
        ret += f"{n}:{','.join(s)}:{','.join(sc)}:{','.join(a)}:{','.join(t)}:{k};"
    if len(ret) > 0:
        return f"--SC {escape_symbol}{ret[:-1]}{escape_symbol}"
    return ret

def _parse_config_time(components: dict, escape_symbol: str = "", callback = None) -> str:
    t = components["ConfigTime"]
    if t["Start"] == "0" and t["End"] == "auto" and t["Step"] == "auto":
        return ""
    return f"--time {t['Start']} {t['End']} {t['Step']}"

def _parse_config_tolerances(components: dict, escape_symbol: str = "", callback = None) -> str:
    ret = ""
    if "ConfigTolerances" in components:
        if "Time" in components["ConfigTolerances"] and "Value" in components["ConfigTolerances"]:
            t,v = components["ConfigTolerances"]["Time"],components["ConfigTolerances"]["Value"]
            ret = f"--rktol {';'.join( [ f'{tt}:{vv}' for tt,vv in zip(t,v) ] )}"
        else:
            tol = components['ConfigTolerances']['Resolution']
            if len(tol) > 0:
                ret = f"--rktol {tol}"
    if len(ret) > 0:
        return ret
    return ret

def _parse_config_grid(components: dict, escape_symbol: str = "", callback = None) -> str:
    ret = ""
    if "ConfigGrid" in components:
        if "Time" in components["ConfigGrid"] and "Value" in components["ConfigGrid"]:
            t,v = components["ConfigGrid"]["Time"],components["ConfigGrid"]["Value"]
            ret = f"--grid {';'.join( [ f'{tt}:{vv}' for tt,vv in zip(t,v) ] )}"
        else:
            gridres = components['ConfigGrid']['Resolution']
            if len(gridres) > 0:
                ret = f"--gridres {gridres}"
    if len(ret) > 0:
        return ret
    return ret
    
def _parse_config_solver(components: dict, escape_symbol: str = "", callback = None) -> str:
    s = components["ConfigSolver"]
    ret = ""
    if s["Solver"] < 3:
        # Usual RK Solver
        solvers = ["45","4","5"]
        ret += f"--rkorder {solvers[s['Solver']]}"
    else:
        # Path Integral
        if (components["ConfigPhonons"]["Temperature"] == "No Phonons"):
            callback("If the PathIntegral PSADM IQUAPI Solver is chosen, the temperature must be set to T >= 0!")
        else:
            ret += "--phononorder 5"
    # Interpolator
    if s['Interpolator'] != "None":
        ret += " -interpolate"
    ret += f" --interpolateOrder {escape_symbol}{s['Interpolator']},{s['InterpolatorGrid']}{escape_symbol}"
    return ret

def _parse_config_system(components: dict, escape_symbol: str = "", callback = None) -> str:
    s = components["ConfigSystem"]
    return f"--system {s['Coupling']} {s['CavityLosses']} {s['RadiativeLosses']} {s['DephasingLosses']}"

def _parse_config_phonons(components: dict, escape_symbol: str = "", callback = None) -> str:
    p = components["ConfigPhonons"]
    ret = ""
    if p["Temperature"] == "No Phonons":
        return ret
    ret += f"--temperature {p['Temperature']} --phononAdjust {int(p['ARRad'])} {int(p['ARDep'])} {int(p['Renormalization'])} --phononohm {p['Ohm']}"
    if components["ConfigSolver"]["Solver"] < 3:
        ret += f" --phononorder {p['Approximation']}"
    if p["IteratorStep"] != "auto":
        ret += f" --iteratorStepsize {p['IteratorStep']}"
    # Phonon Parameters OR QD Parameters
    if p["UseQD"]:
        ret += f" --quantumdot {p['QDde']} {p['QDdh']} {p['QDrho']} {p['QDcs']} {p['QDeh']} {p['QDs']}"
    else:
        ret += f" --phononalpha {p['Alpha']} --phononwcutoff {p['SpectralCutoff']} --phononwcutoffdelta {p['SpectralDelta']} --phonontcutoff {p['TimeCutoff']}"
    return ret

_component_parser = {
    "EnergyLevels" : _parse_electronic_system,
    "CavityLevels" : _parse_cavity_system,
    "Pulse": _parse_pulse_system,
    "Shift" : _parse_shift_system,
    "ConfigTime" : _parse_config_time,
    "ConfigGrid" : _parse_config_grid,
    "ConfigTolerances" : _parse_config_tolerances,
    "ConfigSolver": _parse_config_solver,
    "ConfigSystem": _parse_config_system,
    "ConfigPhonons": _parse_config_phonons,
}

def component_parser(component: str, escaped: bool, components: dict, escape_symbol: str = "'", callback = None) -> str:
    if not escaped:
        escape_symbol = ""
    if component not in components.keys() or component not in _component_parser.keys():
        print(f"Error: Key '{component}' not in Components list!")
        return ""
    return _component_parser[component](components, escape_symbol, callback)

if __name__ == "__main__":
    print("Available Components:")
    print(_component_parser.keys())
    print(f"This file ({__file__}) is part of the QDLC GUI and should be imported, not executed.")