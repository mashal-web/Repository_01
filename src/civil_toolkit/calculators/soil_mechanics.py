"""Elementary soil phase-relationship calculations; no soil classification."""
from civil_toolkit.core.validation import require_finite_result, require_non_negative, require_positive

def water_content(water_mass: float,dry_soil_mass: float) -> float:
    w=require_non_negative(water_mass,"water_mass"); s=require_positive(dry_soil_mass,"dry_soil_mass")
    return require_finite_result(100*w/s,"water_content_percent")

def void_ratio(void_volume: float,solids_volume: float) -> float:
    v=require_non_negative(void_volume,"void_volume"); s=require_positive(solids_volume,"solids_volume")
    return require_finite_result(v/s,"void_ratio")

def porosity(void_volume: float,total_volume: float) -> float:
    v=require_non_negative(void_volume,"void_volume"); t=require_positive(total_volume,"total_volume")
    if v>t: raise ValueError("void_volume cannot exceed total_volume.")
    return require_finite_result(v/t,"porosity")

def degree_of_saturation(water_volume: float,void_volume: float) -> float:
    w=require_non_negative(water_volume,"water_volume"); v=require_positive(void_volume,"void_volume")
    if w>v: raise ValueError("water_volume cannot exceed void_volume.")
    return require_finite_result(100*w/v,"degree_of_saturation_percent")

def bulk_unit_weight(total_weight_kN: float,total_volume_m3: float) -> float:
    w=require_non_negative(total_weight_kN,"total_weight_kN"); v=require_positive(total_volume_m3,"total_volume_m3")
    return require_finite_result(w/v,"bulk_unit_weight_kN_m3")

def dry_unit_weight(dry_weight_kN: float,total_volume_m3: float) -> float:
    w=require_non_negative(dry_weight_kN,"dry_weight_kN"); v=require_positive(total_volume_m3,"total_volume_m3")
    return require_finite_result(w/v,"dry_unit_weight_kN_m3")

def phase_unit_weights(specific_gravity: float,void_ratio_value: float,saturation_percent: float=100,water_unit_weight_kN_m3: float=9.81) -> tuple[float,float]:
    G=require_positive(specific_gravity,"specific_gravity"); e=require_non_negative(void_ratio_value,"void_ratio")
    sr=require_non_negative(saturation_percent,"saturation_percent")
    if sr>100: raise ValueError("saturation_percent cannot exceed 100.")
    gw=require_positive(water_unit_weight_kN_m3,"water_unit_weight_kN_m3")
    return (require_finite_result(gw*(G+(sr/100)*e)/(1+e),"bulk_unit_weight_kN_m3"),
            require_finite_result(gw*G/(1+e),"dry_unit_weight_kN_m3"))

def phase_relationships(void_ratio_value: float,saturation_percent: float) -> dict[str,float]:
    e=require_non_negative(void_ratio_value,"void_ratio"); sr=require_non_negative(saturation_percent,"saturation_percent")
    if sr>100: raise ValueError("saturation_percent cannot exceed 100.")
    return {"porosity":require_finite_result(e/(1+e),"porosity"),"degree_of_saturation":sr,
            "water_to_solids_volume_ratio":require_finite_result((sr/100)*e,"water_to_solids_volume_ratio")}
