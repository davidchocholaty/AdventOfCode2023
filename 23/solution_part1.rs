use std::collections::{HashMap, HashSet, VecDeque};
use std::fs::File;
use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let file = File::open("input")?;
    let reader = io::BufReader::new(file);

    let grid: Vec<Vec<char>> = reader.lines()
        .map(|line| line.unwrap().chars().collect())
        .collect();

    let start = (0, grid[0].iter().position(|&ch| ch == '.').unwrap());
    let end = (grid.len() - 1, grid.last().unwrap().iter().position(|&ch| ch == '.').unwrap());

    let mut points = vec![start, end];

    for (r, row) in grid.iter().enumerate() {
        for (c, &ch) in row.iter().enumerate() {
            if ch == '#' {
                continue;
            }
            let mut neighbors = 0;
            for (nr, nc) in [(r as isize - 1, c as isize), (r as isize + 1, c as isize), (r as isize, c as isize - 1), (r as isize, c as isize + 1)] {
                if nr >= 0 && nr < grid.len() as isize && nc >= 0 && nc < grid[0].len() as isize {
                    if grid[nr as usize][nc as usize] != '#' {
                        neighbors += 1;
                    }
                }
            }
            if neighbors >= 3 {
                points.push((r, c));
            }
        }
    }

    let mut graph: HashMap<(usize, usize), HashMap<(usize, usize), usize>> = points.iter()
        .map(|&pt| (pt, HashMap::new()))
        .collect();

    let dirs: HashMap<char, Vec<(isize, isize)>> = vec![
        ('^', vec![(-1, 0)]),
        ('v', vec![(1, 0)]),
        ('<', vec![(0, -1)]),
        ('>', vec![(0, 1)]),
        ('.', vec![(-1, 0), (1, 0), (0, -1), (0, 1)]),
    ].into_iter().collect();

    for &(sr, sc) in &points {
        let mut stack = VecDeque::new();
        stack.push_back((0, sr, sc));
        let mut seen = HashSet::new();
        seen.insert((sr, sc));

        while let Some((n, r, c)) = stack.pop_back() {
            if n != 0 && points.contains(&(r, c)) {
                graph.entry((sr, sc)).or_default().insert((r, c), n);
                continue;
            }

            if let Some(directions) = dirs.get(&grid[r][c]) {
                for &(dr, dc) in directions {
                    let nr = (r as isize + dr) as usize;
                    let nc = (c as isize + dc) as usize;
                    if nr < grid.len() && nc < grid[0].len() && grid[nr][nc] != '#' && !seen.contains(&(nr, nc)) {
                        stack.push_back((n + 1, nr, nc));
                        seen.insert((nr, nc));
                    }
                }
            }
        }
    }

    let mut seen = HashSet::new();

    fn dfs(
        pt: (usize, usize),
        end: (usize, usize),
        graph: &HashMap<(usize, usize), HashMap<(usize, usize), usize>>,
        seen: &mut HashSet<(usize, usize)>
    ) -> i32 {
        if pt == end {
            return 0;
        }

        let mut max_distance = i32::MIN;
        seen.insert(pt);
        if let Some(neighbors) = graph.get(&pt) {
            for (&nx, &distance) in neighbors {
                if !seen.contains(&nx) {
                    max_distance = max_distance.max(dfs(nx, end, graph, seen) + distance as i32);
                }
            }
        }
        seen.remove(&pt);

        max_distance
    }

    let result = dfs(start, end, &graph, &mut seen);

    println!("{}", result);

    Ok(())
}
