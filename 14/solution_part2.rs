use std::collections::HashSet;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let grid: Vec<String> = read_lines("input")
        .unwrap()
        .map(|line| line.unwrap())
        .collect();

    let mut grid = grid;
    let mut seen: HashSet<Vec<String>> = HashSet::new();
    let mut array: Vec<Vec<String>> = Vec::new();
    
    array.push(grid.clone());
    seen.insert(grid.clone());

    let mut iter = 0;

    loop {
        iter += 1;
        cycle(&mut grid);
        if seen.contains(&grid) {
            break;
        }
        seen.insert(grid.clone());
        array.push(grid.clone());
    }

    let first = array.iter().position(|x| *x == grid).unwrap();

    let final_grid = &array[(1_000_000_000 - first) % (iter - first) + first];

    let sum: usize = final_grid.iter()
        .enumerate()
        .map(|(r, row)| row.matches('O').count() * (final_grid.len() - r))
        .sum();

    println!("{}", sum);
}

fn cycle(grid: &mut Vec<String>) {
    for _ in 0..4 {
        transpose(grid);
        for row in grid.iter_mut() {
            let parts: Vec<String> = row.split('#')
                .map(|group| {
                    let mut chars: Vec<char> = group.chars().collect();
                    chars.sort_unstable_by(|a, b| b.cmp(a));
                    chars.into_iter().collect()
                })
                .collect();
            *row = parts.join("#");
        }
        for row in grid.iter_mut() {
            *row = row.chars().rev().collect();
        }
    }
}

fn transpose(grid: &mut Vec<String>) {
    let n = grid.len();
    let mut new_grid = vec![String::new(); n];
    for row in grid.iter() {
        for (i, ch) in row.chars().enumerate() {
            new_grid[i].push(ch);
        }
    }
    *grid = new_grid;
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
