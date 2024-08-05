use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn find_mirror(grid: &[Vec<char>]) -> usize {
    let rows = grid.len();

    for r in 1..rows {
        let above: Vec<Vec<char>> = grid[..r].iter().rev().cloned().collect();
        let below = &grid[r..];

        let min_len = std::cmp::min(above.len(), below.len());
        let above = &above[..min_len];
        let below = &below[..min_len];

        let diff_sum: usize = above.iter().zip(below).map(|(a, b)| {
            a.iter().zip(b).filter(|(x, y)| x != y).count()
        }).sum();

        if diff_sum == 1 {
            return r;
        }
    }

    0
}

fn main() -> io::Result<()> {
    let path = "input";
    println!("Attempting to open file: {}", path);

    let file = File::open(path).map_err(|err| {
        eprintln!("Error opening file '{}': {}", path, err);
        err
    })?;

    let reader = io::BufReader::new(file);

    let mut total = 0;
    let mut block = String::new();

    for line in reader.lines() {
        let line = line?;

        if line.trim().is_empty() {
            if !block.trim().is_empty() {
                let grid: Vec<Vec<char>> = block.lines()
                                                .map(|l| l.chars().collect())
                                                .collect();

                let row = find_mirror(&grid);
                total += row * 100;

                let col_grid: Vec<Vec<char>> = (0..grid[0].len())
                    .map(|c| grid.iter().map(|r| r[c]).collect())
                    .collect();

                let col = find_mirror(&col_grid);
                total += col;

                block.clear();
            }
        } else {
            block.push_str(&line);
            block.push('\n');
        }
    }

    if !block.trim().is_empty() {
        let grid: Vec<Vec<char>> = block.lines()
                                        .map(|l| l.chars().collect())
                                        .collect();

        let row = find_mirror(&grid);
        total += row * 100;

        let col_grid: Vec<Vec<char>> = (0..grid[0].len())
            .map(|c| grid.iter().map(|r| r[c]).collect())
            .collect();

        let col = find_mirror(&col_grid);
        total += col;
    }

    println!("Total: {}", total);
    Ok(())
}
