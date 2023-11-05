import pytest
from geom2d.punto import Punto
from geom2d.vector import Vector

@pytest.mark.parametrize("pp1, pp2, vec", [
          (Punto(7.,5.), Punto(3.,2.), Vector(4.,3.)),
          (Punto(3.,2.), Punto(7.,5.), Vector( -4., -3.))
      ])
def test_resta(pp1, pp2, vec):
    assert pp1.__sub__(pp2) == vec

@pytest.mark.parametrize("p1, p2, d", [
    (Punto(7., 5.), Punto(3., 2.), 5.)
])
def test_distance(p1, p2, d):
    assert p1.distance(p2) == d

@pytest.mark.parametrize( "pp, vv", [
          (Punto(7,5), Vector(7,5)),
          (Punto(3,2), Vector(3,2))
      ])
def test_hash(pp, vv):
    assert pp.__hash__ != vv.__hash__
