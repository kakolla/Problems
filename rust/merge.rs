// impl Solution {
pub fn merge_alternately(word1: String, word2: String) -> String {
    let mut res: String = "".to_string();
    // let i: i32 = 0;
    let l1: usize = word1.len();
    let l2: usize = word2.len();
    let shorter: usize;
    let longer: usize;
    if l1 < l2 {
        shorter = l1;
        longer = l2;
    } else {
        shorter = l2;
        longer = l1;
    }

    for i in 0..shorter {
        res.push(word1.chars().nth(i).unwrap());
        res.push(word2.chars().nth(i).unwrap());
        println!("{}", i);
    }

    // let mut j = shorter;
    for j in shorter..longer {
        if shorter == l1 {
            res.push(word2.chars().nth(j).unwrap());
        } else if shorter == l2 {
            res.push(word1.chars().nth(j).unwrap());
        }
    }
    return res;
}

pub fn main() {
    let res: String;
    res = merge_alternately("abc".to_string(), "pqr".to_string());
    println!("{}", res);
}
// }
