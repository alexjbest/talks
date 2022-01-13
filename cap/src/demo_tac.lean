import tactic

lemma one : 7 + 0 = 7 :=
begin
  sorry,
end

lemma three : ∀ n, n + 0 = n :=
begin
  rw add_zero,
end


lemma our_zero_add (n : ℕ) : 0 + n = n :=
begin

end

lemma more_props (P Q : Prop) (hP : P) (hQ : Q) : P ∧ Q :=
begin

end
