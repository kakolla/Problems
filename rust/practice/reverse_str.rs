

use std::str;
pub fn reverse(input: &str) -> String {
    let mut s: String = "".to_string();
    let l: usize = input.len();
    for i in (0..l).rev() {
        let c: [u8; 1] = [input.as_bytes()[i]];
        s.push_str(str::from_utf8(&c).unwrap());
    }
   
    dbg!(&s);
    return s.to_string()

}


pub fn main() {
    // println!("{}", reverse("abhi🦀"));
    println!("{}", reverse("abhi"));


}
