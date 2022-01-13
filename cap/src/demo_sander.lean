import tactic
import data.real.basic
variables {R : Type*} [comm_ring R] (x y : R)

def F : R := x^3 + 2*x*y + y^3 - 1
def G : R := 2*x^2 - 3*y^2 + 2
def H : R := x^3 + 3*x*y + 7*y^2 - 1
def a : R := -568781583*x*y^2 + 1152704112*x*y + 1004446918*x + 1486171233*y^3 + 2278972316*y^2 - 8787246228*y - 7750297898
def b : R := 330260274*x^2*y^2 - 1686462745*x^2*y - 2236672062*x^2 - 189593861*x*y^3 + 53974430*x*y^2 + 4521329982*x*y +
  2236672062*x + 495390411*y^4 - 1823304087*y^3 - 8168304546*y^2 - 4521329982*y + 2236672062
def c : R := -91738965*x*y^2 + 2220221378*x*y + 3468897206*x - 1106983511*y^3 - 2386921176*y^2 - 255413736*y + 3276953774

lemma sander : a x y * F x y + b x y * G x y + c x y * H x y = 8946688248 :=
begin
  simp [a, b, c, F, G, H],
  ring,
end

lemma sander2 {x y : ℝ} : ¬(F x y = 0 ∧ G x y = 0 ∧ H x y = 0) :=
begin
  rintro ⟨hF, hG, hH⟩,
  have := sander x y,
  simp [hF, hG, hH] at this,
  linarith,
end
