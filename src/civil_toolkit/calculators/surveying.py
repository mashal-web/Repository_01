"""Elementary plane surveying calculations.

Azimuth is clockwise from north in [0, 360). Quadrant bearings use N/S,
an angle from 0 to 90 degrees, then E/W. All angles are degrees.
"""
import math
from civil_toolkit.core.validation import require_finite_result, require_non_negative, validate_number

def _angle(value: float, name: str) -> float:
    return validate_number(value,name)

def horizontal_distance(slope_distance_m: float, vertical_angle_deg: float) -> float:
    s=require_non_negative(slope_distance_m,"slope_distance_m"); a=_angle(vertical_angle_deg,"vertical_angle_deg")
    if not -90<=a<=90: raise ValueError("vertical_angle_deg must be between -90 and 90.")
    return require_finite_result(s*math.cos(math.radians(a)),"horizontal_distance_m")

def vertical_difference(slope_distance_m: float, vertical_angle_deg: float) -> float:
    s=require_non_negative(slope_distance_m,"slope_distance_m"); a=_angle(vertical_angle_deg,"vertical_angle_deg")
    if not -90<=a<=90: raise ValueError("vertical_angle_deg must be between -90 and 90.")
    return require_finite_result(s*math.sin(math.radians(a)),"vertical_difference_m")

def slope_distance(horizontal_m: float, vertical_m: float) -> float:
    h=require_non_negative(horizontal_m,"horizontal_m"); v=validate_number(vertical_m,"vertical_m")
    return require_finite_result(math.hypot(h,v),"slope_distance_m")

def coordinate_distance(easting1: float, northing1: float, easting2: float, northing2: float) -> float:
    x1=validate_number(easting1,"easting1"); y1=validate_number(northing1,"northing1")
    x2=validate_number(easting2,"easting2"); y2=validate_number(northing2,"northing2")
    return require_finite_result(math.hypot(x2-x1,y2-y1),"coordinate_distance_m")

def bearing_to_azimuth(ns: str, angle_deg: float, ew: str) -> float:
    a=_angle(angle_deg,"angle_deg"); n=ns.upper() if isinstance(ns,str) else ""; e=ew.upper() if isinstance(ew,str) else ""
    if n not in ("N","S") or e not in ("E","W") or not 0<=a<=90:
        raise ValueError("Bearing requires N/S, an angle from 0 to 90 degrees, and E/W.")
    return {"NE":a,"SE":180-a,"SW":180+a,"NW":360-a}[n+e]%360

def azimuth_to_bearing(azimuth_deg: float) -> tuple[str,float,str]:
    a=_angle(azimuth_deg,"azimuth_deg")
    if not 0<=a<360: raise ValueError("azimuth_deg must be in [0, 360).")
    if a<=90: return ("N",a,"E")
    if a<=180: return ("S",180-a,"E")
    if a<=270: return ("S",a-180,"W")
    return ("N",360-a,"W")

def elevation_difference(back_sight_m: float, fore_sight_m: float) -> float:
    bs=require_non_negative(back_sight_m,"back_sight_m"); fs=require_non_negative(fore_sight_m,"fore_sight_m")
    return require_finite_result(bs-fs,"elevation_difference_m")

def height_of_instrument(reduced_level_m: float, back_sight_m: float) -> float:
    rl=validate_number(reduced_level_m,"reduced_level_m"); bs=require_non_negative(back_sight_m,"back_sight_m")
    return require_finite_result(rl+bs,"height_of_instrument_m")

def reduced_level_from_h_i(height_of_instrument_m: float, fore_sight_m: float) -> float:
    hi=validate_number(height_of_instrument_m,"height_of_instrument_m"); fs=require_non_negative(fore_sight_m,"fore_sight_m")
    return require_finite_result(hi-fs,"reduced_level_m")
