import tactic
import data.nat.parity

-- intermediate statements using have
lemma haves (x : ℚ) (hx : 0 < x) : x / x = 1 :=
begin
  -- library_search,
end

lemma ors (P Q : Prop) (h : P ∨ Q) : Q ∨ P :=
begin
  cases h,
end

lemma exist : ∃ n : ℕ, n + 3 = 7 :=
begin

end

lemma exist2 (m : ℕ) : ∃ n : ℕ, m < m ∧ even n :=
begin

end
