

let _ = print_endline "Starting program";;
(* singly LL : value + ptr to next node *)
type mylist = Nil | Cons of int * mylist;;

let l2 = Cons(3,Nil);;




let rec get_length l = 
        match l with
        | Nil -> 0
        | Cons(hd, tl) -> 1 + get_length tl;;


let ls = Cons(3, Cons(2, Cons(1, Nil)));;

let answer = get_length ls;;
let answer_str = Int.to_string answer;;

print_endline answer_str;;










