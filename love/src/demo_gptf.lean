import tactic.gptf

lemma my_lemma {α} (a : α) : a = a :=
begin
  gptf {n := 32, temp := 1.0} -- this will query the server and return a set of 'try this' commands.
end