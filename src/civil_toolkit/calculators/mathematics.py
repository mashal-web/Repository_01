"""Dependency-free engineering mathematics utilities."""
import math
from civil_toolkit.core.validation import require_finite_result, validate_number

def solve_linear(a: float,b: float) -> float:
    aa=validate_number(a,"a"); bb=validate_number(b,"b")
    if aa==0: raise ValueError("Linear equation has no unique solution when a is zero.")
    return require_finite_result(-bb/aa,"solution")

def solve_quadratic(a: float,b: float,c: float) -> tuple[complex,complex]:
    aa=validate_number(a,"a"); bb=validate_number(b,"b"); cc=validate_number(c,"c")
    if aa==0: raise ValueError("Quadratic coefficient a must be non-zero.")
    disc=bb*bb-4*aa*cc
    if not math.isfinite(disc): raise ValueError("Discriminant is not finite.")
    root=complex(disc)**0.5
    roots=((-bb+root)/(2*aa),(-bb-root)/(2*aa))
    if not all(math.isfinite(z.real) and math.isfinite(z.imag) for z in roots):
        raise ValueError("Quadratic roots are not finite.")
    return roots

def _matrix(M: list[list[float]],name: str) -> None:
    if not isinstance(M,list) or not M or any(not isinstance(r,list) or not r for r in M):
        raise ValueError(f"{name} must be a non-empty rectangular matrix.")
    if any(len(r)!=len(M[0]) for r in M): raise ValueError(f"{name} must be rectangular.")
    for row in M:
        for v in row: validate_number(v,name)

def matrix_add(A: list[list[float]],B: list[list[float]]) -> list[list[float]]:
    _matrix(A,"A"); _matrix(B,"B")
    if len(A)!=len(B) or any(len(x)!=len(y) for x,y in zip(A,B)): raise ValueError("Matrices must have identical dimensions.")
    return [[require_finite_result(x+y,"matrix result") for x,y in zip(ar,br)] for ar,br in zip(A,B)]

def matrix_multiply(A: list[list[float]],B: list[list[float]]) -> list[list[float]]:
    _matrix(A,"A"); _matrix(B,"B")
    if len(A[0])!=len(B): raise ValueError("Matrix dimensions are not compatible for multiplication.")
    return [[require_finite_result(sum(A[i][k]*B[k][j] for k in range(len(B))),"matrix result") for j in range(len(B[0]))] for i in range(len(A))]

def matrix_inverse(M: list[list[float]]) -> list[list[float]]:
    _matrix(M,"matrix"); n=len(M)
    if len(M[0])!=n: raise ValueError("Only square matrices can be inverted.")
    a=[[float(v) for v in row]+[float(i==j) for j in range(n)] for i,row in enumerate(M)]
    for col in range(n):
        pivot=max(range(col,n),key=lambda r:abs(a[r][col]))
        if a[pivot][col]==0: raise ValueError("Matrix is singular.")
        a[col],a[pivot]=a[pivot],a[col]; p=a[col][col]
        a[col]=[v/p for v in a[col]]
        for r in range(n):
            if r!=col:
                f=a[r][col]; a[r]=[x-f*y for x,y in zip(a[r],a[col])]
    return [[require_finite_result(v,"matrix inverse result") for v in row[n:]] for row in a]

def trig(value: float,function: str="sin",angle_unit: str="degrees") -> float:
    x=validate_number(value,"angle"); unit=angle_unit.lower()
    if unit not in ("degrees","radians"): raise ValueError("angle_unit must be degrees or radians.")
    x=math.radians(x) if unit=="degrees" else x
    funcs={"sin":math.sin,"cos":math.cos,"tan":math.tan}
    if function not in funcs: raise ValueError("function must be sin, cos, or tan.")
    if function=="tan" and abs(math.cos(x))<1e-15: raise ValueError("Tangent is undefined at this angle.")
    return require_finite_result(funcs[function](x),"trigonometric result")

def percentage(value: float,percent: float) -> float:
    return require_finite_result(validate_number(value,"value")*validate_number(percent,"percent")/100,"percentage")

def ratio_parts(total: float,first: float,second: float) -> tuple[float,float]:
    t=validate_number(total,"total"); a=validate_number(first,"first"); b=validate_number(second,"second")
    if t<0 or a<0 or b<0 or a+b==0: raise ValueError("Total and ratio parts must be non-negative and ratio sum positive.")
    den=require_finite_result(a+b,"ratio sum")
    return (require_finite_result(t*a/den,"first_share"),require_finite_result(t*b/den,"second_share"))

def convert_engineering(value: float,from_unit: str,to_unit: str) -> float:
    factors={"m":("length",1.0),"mm":("length",.001),"cm":("length",.01),"km":("length",1000.0),
      "m2":("area",1.0),"cm2":("area",.0001),"mm2":("area",.000001),
      "Pa":("pressure",1.0),"kPa":("pressure",1000.0),"MPa":("pressure",1000000.0),
      "N":("force",1.0),"kN":("force",1000.0)}
    if from_unit not in factors or to_unit not in factors or factors[from_unit][0]!=factors[to_unit][0]:
        raise ValueError("Units must belong to the same supported family.")
    return require_finite_result(validate_number(value,"value")*factors[from_unit][1]/factors[to_unit][1],"converted value")
