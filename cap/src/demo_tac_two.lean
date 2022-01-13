import tactic

-- intermediate statements using have
lemma haves (x : ℚ) (hx : 0 < x) : x / x = 1 :=
begin
  -- library_search,
end

lemma ors (P Q : Prop) (h : P ∨ Q) : Q ∨ P :=
begin
  cases h,
end
