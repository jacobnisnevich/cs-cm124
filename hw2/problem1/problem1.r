#!/usr/bin/env Rscript

p_a_plus <- function(p, gamma) {
  return((gamma * p) / ((gamma - 1) * p + 1))
}

non_centrality <- function(p, gamma, N) {
  p_a_plus <- p_a_plus(p, gamma)
  p_a_minus <- p
  p_a <- mean(c(p_a_plus, p_a_minus))

  return((p_a_plus - p_a_minus) / (sqrt(2 / N) * sqrt(p_a * (1 - p_a))))
}

power <- function(non_centrality_param, alpha) {
  return(pnorm(qnorm(alpha / 2) + non_centrality_param) + 1 - pnorm(-1 * qnorm(alpha / 2) + non_centrality_param))
}

minor_allele_frequencies <- c(0.05, 0.2, 0.4)
relative_risks <- c(1.5, 2, 3)
alpha <- 0.05
n_vals <- c(500, 1000)

cat("Part 1\n\n")

for (N in n_vals) {
  for (gamma in relative_risks) {
    for (p in minor_allele_frequencies) {
      non_centrality_param <- non_centrality(p, gamma, N)
      cat(non_centrality_param)
      cat("\n")
    }
  }
  cat("\n")
}

cat("Part 2\n\n")

for (N in n_vals) {
  for (gamma in relative_risks) {
    for (p in minor_allele_frequencies) {
      non_centrality_param <- non_centrality(p, gamma, N)
      power_val <- power(non_centrality_param, alpha)
      cat(power_val)
      cat("\n")
    }
  }
  cat("\n")
}

cat("Part 3\n\n")

for (gamma in relative_risks) {
  for (p in minor_allele_frequencies) {
    for (N in (1:3000)) {
      non_centrality_param <- non_centrality(p, gamma, N)
      power_val <- power(non_centrality_param, alpha)

      if (power_val > 0.8) {
        cat(N)
        cat("\n")
        break
      }
    }
  }
}
