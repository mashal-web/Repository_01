# Engineering calculator formulas

All methods are educational calculations. Units and conventions are specified below.

## Concrete
For a rectangular element, V = L × B × H, where dimensions are metres and volume is m³. Optional user-selected allowance: Ve = V(1 + p/100). No allowance is prescribed.

## Materials: brickwork and mortar
Wall volume: Vw = Lw Hw Tw. Modular brick volume includes joints:
Vm = (lb + j)(bb + j)(hb + j).
Theoretical brick count N = Vw/Vm. Order count No = ceil(N(1 + w/100)), where w is the user-selected wastage percentage. Theoretical brick solid volume is N lb bb hb; wet mortar is Vw less brick solids. Dry mortar volume is wet mortar multiplied by the selected dry-volume factor.

For cement:sand loose-volume ratio c:s:
Vc = Vd c/(c+s), Vs = Vd s/(c+s).
Cement mass = Vc × assumed cement bulk density; bag count = cement mass / assumed bag mass. Defaults (190×90×90 mm brick, 10 mm joint, 5% wastage, 1:6 mix, 1.33 dry factor, 1440 kg/m³ cement density, 50 kg bag) are assumptions, not standards.

## Steel
Approximate theoretical bar weight: W = (d²/162) × L, where d is diameter in mm, L is length in metres, and W is approximate kg. Multiply by bar count for a batch.

## Surveying
For slope distance S and vertical angle θ measured from horizontal: H = S cos θ and ΔV = S sin θ. Reconstruct slope distance with S = sqrt(H² + V²). Plane coordinate distance D = sqrt((E2−E1)² + (N2−N1)²).

Azimuth is clockwise from north in [0°, 360°). Quadrant conversions: NE=A, SE=180°−A, SW=180°+A, NW=360°−A. Leveling by height of instrument: HI = RL + BS; RLnext = HI − FS.

## Engineering mathematics
Linear equation ax+b=0: x=−b/a, requiring a≠0. Quadratic equation ax²+bx+c=0: x = (−b ± sqrt(b²−4ac))/(2a). Complex roots are returned for a negative discriminant.

Matrix addition/multiplication follow standard dimension rules. Matrix inverse uses pivoted Gauss–Jordan elimination and rejects singular matrices. Trigonometric functions accept degrees or radians. Percentage is v p/100. A total T divided in ratio a:b gives Ta/(a+b) and Tb/(a+b).

Supported unit conversions within a family: length (m, mm, cm, km), area (m², cm², mm²), pressure (Pa, kPa, MPa), force (N, kN).

## Soil mechanics
Water content w = Mw/Ms × 100%. Void ratio e = Vv/Vs; porosity n = Vv/V = e/(1+e); degree of saturation Sr = Vw/Vv × 100%.

Bulk and dry unit weights: γ = W/V; γd = Ws/V. With specific gravity Gs, void ratio e, saturation fraction Sr and water unit weight γw:
γ = γw(Gs + Sr e)/(1+e); γd = γw Gs/(1+e).
Here Sr is a fraction from 0 to 1 in the phase-weight equation.

## Scope
These formulas do not represent a full design or standards-compliance procedure. See assumptions.md for exclusions and cautions.
