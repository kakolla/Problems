

let _ = print_endline "Starting program";;
(* singly LL : value + ptr to next node *)
type mylist = Nil | Cons of int * mylist;;

let l2 = Cons(3,Nil);;




(* let rec get_length l =  *)
(*         match l with *)
(*         | Nil -> 0 *)
(*         | Cons(hd, tl) -> 1 + get_length tl;; *)



let rec get_length l = 
        match l with
        | [] -> 0
        | hd :: tl  -> 1 + get_length tl;;







let ls = Cons(3, Cons(2, Cons(1, Nil)));;

let answer = get_length ls;;
let answer_str = Int.to_string answer;;

print_endline "Length of list:";;
print_endline answer_str;;


print_endline "Printing list now:";;
(*Print *)
let rec print_list l = 
        match l with
        | Nil ->  print_endline("---")
        | Cons(hd, tl) ->
                        print_endline(Int.to_string hd);
                        print_list tl;;


print_list ls;;

(*add value to end of list*)
let rec snoc l value = 
        match l with 
        | Nil -> Cons(value, Nil)
        | Cons(hd, tl) -> Cons(hd, snoc tl value);;

print_endline "Adding to end of list";;

let ls2 = snoc ls 0;;

print_list ls2;;




print_endline "Creating a really big list";;
(*create a big list*)
let rec make_big_list n =
        if n <=0 then Nil
        else Cons(1, make_big_list (n-1));;


let l = make_big_list 100000 in get_lendth (Cons(98, l));;

let l = make_big_list 100000 in get_length (snoc l 98);;




        





