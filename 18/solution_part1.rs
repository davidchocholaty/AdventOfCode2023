use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("input")?;
    let reader = BufReader::new(file);

    let mut points = vec![(0, 0)];
    let mut dirs = HashMap::new();
    dirs.insert("U", (-1, 0));
    dirs.insert("D", (1, 0));
    dirs.insert("L", (0, -1));
    dirs.insert("R", (0, 1));

    let mut b = 0;

    for line in reader.lines() {
        let line = line?;
        let parts: Vec<&str> = line.split_whitespace().collect();
        let d = parts[0];
        let n: i32 = parts[1].parse().unwrap();
        let (dr, dc) = dirs[d];
        b += n;
        let (r, c) = points.last().copied().unwrap();
        points.push((r + dr * n, c + dc * n));
    }

    let len = points.len();
    let A: i32 = (0..len).map(|i| {
        let (r1, c1) = points[i];
        let (r2, c2) = points[(i + len - 1) % len];
        let (r3, c3) = points[(i + 1) % len];
        r1 * (c2 - c3)
    }).sum::<i32>().abs() / 2;

    let i = A - b / 2 + 1;

    println!("{}", i + b);

    Ok(())
}
