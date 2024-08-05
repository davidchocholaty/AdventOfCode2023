use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("input")?;
    let reader = BufReader::new(file);

    let mut points = vec![(0_i64, 0_i64)];
    let mut dirs = HashMap::new();
    dirs.insert('U', (-1_i64, 0_i64));
    dirs.insert('D', (1_i64, 0_i64));
    dirs.insert('L', (0_i64, -1_i64));
    dirs.insert('R', (0_i64, 1_i64));

    let mut b: i64 = 0;

    for line in reader.lines() {
        let line = line?;
        let parts: Vec<&str> = line.split_whitespace().collect();
        let x = &parts[2][2..parts[2].len() - 1];
        let dr_dc = match x.chars().last().unwrap() {
            '0' => dirs[&'R'],
            '1' => dirs[&'D'],
            '2' => dirs[&'L'],
            '3' => dirs[&'U'],
            _ => (0, 0),  // Default case, should not happen
        };
        let dr = dr_dc.0;
        let dc = dr_dc.1;
        let n = i64::from_str_radix(&x[..x.len() - 1], 16).unwrap();
        b += n;
        let (r, c) = points.last().copied().unwrap();
        points.push((r + dr * n, c + dc * n));
    }

    let len = points.len();
    let A: i64 = (0..len).map(|i| {
        let (r1, c1) = points[i];
        let (r2, c2) = points[(i + len - 1) % len];
        let (r3, c3) = points[(i + 1) % len];
        r1 * (c2 - c3)
    }).sum::<i64>().abs() / 2;

    let i = A - b / 2 + 1;

    println!("{}", i + b);

    Ok(())
}
