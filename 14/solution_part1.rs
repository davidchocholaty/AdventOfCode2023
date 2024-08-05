use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let handle = stdin.lock();

    let grid: Vec<String> = handle.lines().filter_map(|line| line.ok()).collect();

    // Transpose the grid
    let transposed: Vec<String> = (0..grid[0].len())
        .map(|i| grid.iter().map(|line| line.chars().nth(i).unwrap()).collect())
        .collect();

    let sorted_rows: Vec<String> = transposed
        .into_iter()
        .map(|row| {
            row.split('#')
                .map(|group| {
                    let mut chars: Vec<char> = group.chars().collect();
                    chars.sort_by(|a, b| b.cmp(a)); // Sort in reverse order
                    chars.into_iter().collect()
                })
                .collect::<Vec<String>>()
                .join("#")
        })
        .collect();

    // Transpose again
    let final_grid: Vec<String> = (0..sorted_rows[0].len())
        .map(|i| sorted_rows.iter().map(|line| line.chars().nth(i).unwrap()).collect())
        .collect();

    let result: usize = final_grid
        .iter()
        .enumerate()
        .map(|(r, row)| row.chars().filter(|&c| c == 'O').count() * (final_grid.len() - r))
        .sum();

    println!("{}", result);
    Ok(())
}
