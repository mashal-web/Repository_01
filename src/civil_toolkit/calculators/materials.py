"""Preliminary masonry and mortar quantity estimates.

Brick count uses wall volume divided by modular brick volume (brick dimensions
plus joints). Mortar is wall volume minus theoretical brick solids. Dry-volume
factor, cement density and bag mass are explicit estimating assumptions.
"""
import math
from dataclasses import dataclass
from civil_toolkit.core.validation import require_finite_result, require_non_negative, require_positive

@dataclass(frozen=True)
class MasonryEstimate:
    wall_volume_m3: float
    theoretical_bricks: float
    bricks_to_order: int
    mortar_wet_volume_m3: float
    mortar_dry_volume_m3: float
    cement_volume_m3: float
    sand_volume_m3: float
    cement_mass_kg: float
    cement_bags: float

def estimate_brickwork(length_m: float, height_m: float, thickness_m: float,
                       brick_length_mm: float = 190, brick_width_mm: float = 90,
                       brick_height_mm: float = 90, joint_mm: float = 10,
                       wastage_percent: float = 5, cement_parts: float = 1,
                       sand_parts: float = 6, dry_volume_factor: float = 1.33,
                       cement_density_kg_m3: float = 1440,
                       bag_mass_kg: float = 50) -> MasonryEstimate:
    """Estimate brick count and cement/sand for a rectangular wall.

    Wall dimensions are metres; brick and joint dimensions are mm. Mortar
    ratio is cement:sand by loose volume. Wastage applies to ordered bricks.
    """
    L=require_positive(length_m,"length_m"); H=require_positive(height_m,"height_m")
    T=require_positive(thickness_m,"thickness_m")
    bl=require_positive(brick_length_mm,"brick_length_mm")/1000
    bw=require_positive(brick_width_mm,"brick_width_mm")/1000
    bh=require_positive(brick_height_mm,"brick_height_mm")/1000
    j=require_non_negative(joint_mm,"joint_mm")/1000
    waste=require_non_negative(wastage_percent,"wastage_percent")
    cp=require_positive(cement_parts,"cement_parts"); sp=require_positive(sand_parts,"sand_parts")
    dry=require_positive(dry_volume_factor,"dry_volume_factor")
    density=require_positive(cement_density_kg_m3,"cement_density_kg_m3")
    bag=require_positive(bag_mass_kg,"bag_mass_kg")
    wall=require_finite_result(L*H*T,"wall_volume_m3")
    modular=(bl+j)*(bw+j)*(bh+j)
    count=require_finite_result(wall/modular,"theoretical_bricks")
    brick_solid=require_finite_result(count*bl*bw*bh,"brick_solid_volume_m3")
    if brick_solid > wall + max(1e-12,wall*1e-12):
        raise ValueError("Brick dimensions are incompatible with wall thickness/volume.")
    mortar=max(0.0,wall-brick_solid)
    dry_mortar=require_finite_result(mortar*dry,"mortar_dry_volume_m3")
    total=require_finite_result(cp+sp,"mix_ratio_total")
    cement=dry_mortar*cp/total; sand=dry_mortar*sp/total
    mass=require_finite_result(cement*density,"cement_mass_kg")
    return MasonryEstimate(wall,count,math.ceil(count*(1+waste/100)),mortar,dry_mortar,
        require_finite_result(cement,"cement_volume_m3"),require_finite_result(sand,"sand_volume_m3"),
        mass,require_finite_result(mass/bag,"cement_bags"))
