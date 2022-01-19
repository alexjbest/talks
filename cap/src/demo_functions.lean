import data.nat.basic

def f (n : ℕ) : ℕ := n + 1

def     --- we are making a new definition
F       --- the thing we are defining is called F
(n : ℕ) --- it has argument (input) a natural number called n
: ℕ     --- the output type is a natural number
:=      --- define the left hand side to be the right side
n + 1   --- the input + 1

#eval f 3

lemma f_pos : ∀ n, 0 < f n :=
begin
  intro n,
  rw f,
  induction n,
  { rw [zero_add],
    exact zero_lt_one, },
  { transitivity n_n + 1,
    exact n_ih,
    apply add_lt_add_right,
    exact lt_add_one n_n, },
end

lemma f_pos' (n : ℕ) : 0 < f n := nat.succ_pos n
