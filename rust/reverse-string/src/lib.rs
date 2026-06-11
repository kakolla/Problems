

// use std::str;
use unicode_reverse::reverse_grapheme_clusters_in_place;
pub fn reverse(input: &str) -> String {
    let mut output = input.to_string(); // clone it (not the ptr, but the acc data)
    reverse_grapheme_clusters_in_place(&mut output);

    return output.to_string();
    // let mut s: String = "".to_string();
    // let l: usize = input.len();
    // for i in (0..l).rev() {
    //     let c: [u8; 1] = [input.as_bytes()[i]];
    //     s.push_str(str::from_utf8(&c).unwrap());
    // }
    //
    // dbg!(&s);
    // return s.to_string()
    //
}


pub fn main() {
    println!("{}", reverse("abhi🦀"));
    // println!("{}", reverse("abhi"));


}
