










(*
 # last_two ["a"; "b"; "c"; "d"];;
- : (string * string) option = Some ("c", "d")
# last_two ["a"];;
- : (string * string) option = None


 *)


let rec last_two lst fst snd = 
        match lst with 
        | [] -> None
        | hd :: [] -> None
        | hd :: tl :: smt -> last_two smt hd tl
        | hd :: tl :: [] -> (hd, tl)



