







let rec last l : 'a option  = 
        match l with 
        | [] -> None
        | hd :: [] -> Some hd
        | hd :: tl -> last tl;;




last ["a"; "b"; "c"; "d"];


