"""CLI adapters for the independent engineering calculation modules."""
import argparse
from civil_toolkit.calculators.concrete import beam_volume,column_volume,slab_volume,volume_with_allowance
from civil_toolkit.calculators.materials import estimate_brickwork
from civil_toolkit.calculators.steel import total_bar_weight
from civil_toolkit.calculators.surveying import horizontal_distance,vertical_difference,slope_distance,coordinate_distance,bearing_to_azimuth,azimuth_to_bearing,height_of_instrument,reduced_level_from_h_i
from civil_toolkit.calculators.mathematics import solve_linear,solve_quadratic,trig,percentage,convert_engineering
from civil_toolkit.calculators.soil_mechanics import water_content,void_ratio,porosity,degree_of_saturation,bulk_unit_weight,dry_unit_weight,phase_unit_weights

def build_parser() -> argparse.ArgumentParser:
    parser=argparse.ArgumentParser(prog="civil-toolkit",description="Civil Engineering Toolkit — educational calculations.")
    subs=parser.add_subparsers(dest="command",required=True)
    for name,third in (("slab","thickness"),("beam","depth"),("column","depth")):
        p=subs.add_parser(name,help=f"Calculate rectangular {name} volume.")
        col=name=="column"; p.add_argument("--height" if col else "--length",dest="height" if col else "length",type=float,required=True)
        p.add_argument("--width",type=float,required=True); p.add_argument("--"+third,type=float,required=True)
        p.add_argument("--allowance",type=float,default=0)
    p=subs.add_parser("brickwork",help="Estimate bricks and mortar for a rectangular wall.")
    for n in ("length","height","thickness"): p.add_argument("--"+n,type=float,required=True)
    for n,d in (("brick-length",190),("brick-width",90),("brick-height",90),("joint",10),("wastage",5),("cement-parts",1),("sand-parts",6)):
        p.add_argument("--"+n,type=float,default=d)
    p=subs.add_parser("steel",help="Calculate theoretical reinforcement bar weight.")
    p.add_argument("--diameter",type=float,required=True); p.add_argument("--length",type=float,required=True); p.add_argument("--count",type=int,default=1)
    p=subs.add_parser("survey-horizontal",help="Resolve slope distance into horizontal and vertical components.")
    p.add_argument("--slope-distance",type=float,required=True); p.add_argument("--angle",type=float,required=True)
    p=subs.add_parser("survey-slope",help="Calculate slope distance.")
    p.add_argument("--horizontal",type=float,required=True); p.add_argument("--vertical",type=float,required=True)
    p=subs.add_parser("survey-coordinate",help="Calculate distance between plane coordinates.")
    for n in ("easting1","northing1","easting2","northing2"): p.add_argument("--"+n,type=float,required=True)
    p=subs.add_parser("survey-bearing",help="Convert quadrant bearing to azimuth.")
    p.add_argument("--ns",choices=["N","S"],required=True); p.add_argument("--angle",type=float,required=True); p.add_argument("--ew",choices=["E","W"],required=True)
    p=subs.add_parser("survey-azimuth",help="Convert azimuth to quadrant bearing.")
    p.add_argument("--azimuth",type=float,required=True)
    p=subs.add_parser("survey-level",help="Calculate HI and foresight reduced level.")
    p.add_argument("--rl",type=float,required=True); p.add_argument("--bs",type=float,required=True); p.add_argument("--fs",type=float,required=True)
    p=subs.add_parser("math-linear",help="Solve a*x + b = 0.")
    p.add_argument("--a",type=float,required=True); p.add_argument("--b",type=float,required=True)
    p=subs.add_parser("math-quadratic",help="Solve a*x² + b*x + c = 0.")
    for n in ("a","b","c"): p.add_argument("--"+n,type=float,required=True)
    p=subs.add_parser("math-trig",help="Evaluate sin, cos, or tan.")
    p.add_argument("--value",type=float,required=True); p.add_argument("--function",choices=["sin","cos","tan"],default="sin"); p.add_argument("--unit",choices=["degrees","radians"],default="degrees")
    p=subs.add_parser("math-percent",help="Calculate a percentage.")
    p.add_argument("--value",type=float,required=True); p.add_argument("--percent",type=float,required=True)
    p=subs.add_parser("math-convert",help="Convert supported engineering units.")
    p.add_argument("--value",type=float,required=True); p.add_argument("--from-unit",required=True); p.add_argument("--to-unit",required=True)
    soil={"soil-water":("water-mass","dry-soil-mass"),"soil-void":("void-volume","solids-volume"),"soil-porosity":("void-volume","total-volume"),"soil-saturation":("water-volume","void-volume"),"soil-bulk":("weight","volume"),"soil-dry":("dry-weight","volume")}
    for cmd,opts in soil.items():
        p=subs.add_parser(cmd,help="Soil phase relationship: "+cmd[5:])
        for opt in opts: p.add_argument("--"+opt,type=float,required=True)
    p=subs.add_parser("soil-phase",help="Calculate bulk and dry unit weight from phase relationships.")
    p.add_argument("--gs",type=float,required=True); p.add_argument("--void-ratio",type=float,required=True); p.add_argument("--saturation",type=float,default=100)
    return parser

def run_cli(argv: list[str] | None=None) -> int:
    parser=build_parser(); a=parser.parse_args(argv); c=a.command
    try:
        if c in ("slab","beam","column"):
            if c=="slab": v=slab_volume(a.length,a.width,a.thickness)
            elif c=="beam": v=beam_volume(a.length,a.width,a.depth)
            else: v=column_volume(a.height,a.width,a.depth)
            print(f"Geometric concrete volume: {v:.3f} m³")
            print(f"Volume including allowance: {volume_with_allowance(v,a.allowance):.3f} m³")
        elif c=="brickwork":
            r=estimate_brickwork(a.length,a.height,a.thickness,a.brick_length,a.brick_width,a.brick_height,a.joint,a.wastage,a.cement_parts,a.sand_parts)
            print(f"Theoretical bricks: {r.theoretical_bricks:.2f}; bricks to order: {r.bricks_to_order}")
            print(f"Estimated wet mortar: {r.mortar_wet_volume_m3:.3f} m³")
            print(f"Estimated cement: {r.cement_bags:.2f} bags ({r.cement_mass_kg:.1f} kg); sand: {r.sand_volume_m3:.3f} m³")
        elif c=="steel": print(f"Theoretical steel weight: {total_bar_weight(a.diameter,a.length,a.count):.3f} kg")
        elif c=="survey-horizontal":
            print(f"Horizontal distance: {horizontal_distance(a.slope_distance,a.angle):.3f} m")
            print(f"Vertical difference: {vertical_difference(a.slope_distance,a.angle):.3f} m")
        elif c=="survey-slope": print(f"Slope distance: {slope_distance(a.horizontal,a.vertical):.3f} m")
        elif c=="survey-coordinate": print(f"Coordinate distance: {coordinate_distance(a.easting1,a.northing1,a.easting2,a.northing2):.3f} m")
        elif c=="survey-bearing": print(f"Azimuth: {bearing_to_azimuth(a.ns,a.angle,a.ew):.3f}°")
        elif c=="survey-azimuth":
            ns,ang,ew=azimuth_to_bearing(a.azimuth); print(f"Bearing: {ns} {ang:.3f}° {ew}")
        elif c=="survey-level":
            hi=height_of_instrument(a.rl,a.bs); print(f"Height of instrument: {hi:.3f} m")
            print(f"Foresight reduced level: {reduced_level_from_h_i(hi,a.fs):.3f} m")
        elif c=="math-linear": print(f"x = {solve_linear(a.a,a.b):.6g}")
        elif c=="math-quadratic": print(f"Roots: {solve_quadratic(a.a,a.b,a.c)}")
        elif c=="math-trig": print(f"Result: {trig(a.value,a.function,a.unit):.8g}")
        elif c=="math-percent": print(f"Result: {percentage(a.value,a.percent):.8g}")
        elif c=="math-convert": print(f"Converted value: {convert_engineering(a.value,a.from_unit,a.to_unit):.8g} {a.to_unit}")
        elif c=="soil-water": print(f"Water content: {water_content(a.water_mass,a.dry_soil_mass):.3f} %")
        elif c=="soil-void": print(f"Void ratio: {void_ratio(a.void_volume,a.solids_volume):.5g}")
        elif c=="soil-porosity": print(f"Porosity: {porosity(a.void_volume,a.total_volume):.5g}")
        elif c=="soil-saturation": print(f"Degree of saturation: {degree_of_saturation(a.water_volume,a.void_volume):.3f} %")
        elif c=="soil-bulk": print(f"Bulk unit weight: {bulk_unit_weight(a.weight,a.volume):.3f} kN/m³")
        elif c=="soil-dry": print(f"Dry unit weight: {dry_unit_weight(a.dry_weight,a.volume):.3f} kN/m³")
        elif c=="soil-phase":
            bulk,dry=phase_unit_weights(a.gs,a.void_ratio,a.saturation)
            print(f"Bulk unit weight: {bulk:.3f} kN/m³"); print(f"Dry unit weight: {dry:.3f} kN/m³")
    except (TypeError,ValueError,OverflowError) as exc:
        parser.error(str(exc))
    return 0
