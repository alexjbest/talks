import data.list.basic

variables {α : Type*} [ring α]

lemma ex (l : list α) (h : l ≠ []) : ∃ a k, l = k ++ [a] :=
begin
  split,
  swap,
  -- library_search,
  -- split,
  -- swap,
  -- let d := l.length - 1,
  -- suggest using d,
end

lemma a : true :=
have 1 = 1 := rfl,
trivial

lemma b : true :=
(λ h : 1 = 1, trivial) rfl
