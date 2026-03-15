import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# MARKET PARAMETERS
# ============================================================
alpha = 0.05      # Expected return per share
beta = 0.0001     # Market impact coefficient
c = 0.01          # Transaction cost per share
mu = 0.08         # Expected annual return (8%)
sigma = 0.20      # Annual volatility (20%)
k = 1000          # Order impact intensity
lam = 2           # Market drift rate

# ============================================================
# OPTIMIZATION FUNCTIONS (from earlier sections)
# ============================================================

def profit(x, alpha, beta, c):
  """Profit function: P(x) = αx - βx² - cx"""
  return alpha * x - beta * x**2 - c * x

def risk_adjusted_return(ell, mu, sigma):
  """Risk-adjusted return: R(ℓ) = ℓμ - (1/2)ℓ²σ²"""
  return ell * mu - 0.5 * (ell ** 2) * (sigma ** 2)

def execution_cost(t, k, lam):
  """Execution cost: C(t) = k/t + λt"""
  return k / t + lam * t

# ============================================================
# COMPUTE OPTIMAL VALUES
# ============================================================

# 1. Optimal trade size: x* = (α - c) / (2β)
optimal_x = (alpha - c) / (2 * beta)
max_profit = profit(optimal_x, alpha, beta, c)

# 2. Optimal leverage (Kelly): ℓ* = μ / σ²
optimal_leverage = mu / (sigma ** 2)
max_return = risk_adjusted_return(optimal_leverage, mu, sigma)

# 3. Optimal execution time: t* = √(k/λ)
optimal_time = np.sqrt(k / lam)
min_cost = execution_cost(optimal_time, k, lam)

# ============================================================
# PRINT RESULTS
# ============================================================

print("=" * 55)
print("OPTIMAL TRADE DESIGN SUMMARY")
print("=" * 55)
print(f"\n1. TRADE SIZE OPTIMIZATION")
print(f"   Formula: x* = (α - c) / (2β)")
print(f"   Optimal size: {optimal_x:.0f} shares")
print(f"   Maximum profit: ${max_profit:.2f}")
print(f"\n2. LEVERAGE OPTIMIZATION (Kelly Criterion)")
print(f"   Formula: ℓ* = μ / σ²")
print(f"   Optimal leverage: {optimal_leverage:.2f}x")
print(f"   Risk-adjusted return: {max_return*100:.2f}%")
print(f"\n3. EXECUTION TIME OPTIMIZATION")
print(f"   Formula: t* = √(k/λ)")
print(f"   Optimal execution: {optimal_time:.1f} minutes")
print(f"   Minimum cost: ${min_cost:.2f}")
print("=" * 55)

# ============================================================
# VISUALIZATION
# ============================================================

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

# Plot 1: Profit vs Trade Size
x_range = np.linspace(1, 400, 200)
profits = profit(x_range, alpha, beta, c)
axes[0].plot(x_range, profits, 'b-', linewidth=2)
axes[0].axvline(optimal_x, color='green', linestyle='--', label=f'Optimal: {optimal_x:.0f}')
axes[0].axhline(0, color='gray', linestyle='-', alpha=0.3)
axes[0].scatter([optimal_x], [max_profit], color='green', s=100, zorder=5)
axes[0].set_xlabel('Trade Size (shares)')
axes[0].set_ylabel('Profit ($)')
axes[0].set_title('Trade Size Optimization')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Plot 2: Risk-Adjusted Return vs Leverage
ell_range = np.linspace(0.1, 5, 200)
returns = risk_adjusted_return(ell_range, mu, sigma)
axes[1].plot(ell_range, returns * 100, 'b-', linewidth=2)
axes[1].axvline(optimal_leverage, color='green', linestyle='--', label=f'Optimal: {optimal_leverage:.1f}x')
axes[1].axhline(0, color='gray', linestyle='-', alpha=0.3)
axes[1].scatter([optimal_leverage], [max_return * 100], color='green', s=100, zorder=5)
axes[1].set_xlabel('Leverage (x)')
axes[1].set_ylabel('Risk-Adjusted Return (%)')
axes[1].set_title('Kelly Criterion')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# Plot 3: Execution Cost vs Time
t_range = np.linspace(5, 100, 200)
costs = execution_cost(t_range, k, lam)
axes[2].plot(t_range, costs, 'b-', linewidth=2)
axes[2].axvline(optimal_time, color='green', linestyle='--', label=f'Optimal: {optimal_time:.1f} min')
axes[2].scatter([optimal_time], [min_cost], color='green', s=100, zorder=5)
axes[2].set_xlabel('Execution Time (minutes)')
axes[2].set_ylabel('Total Cost ($)')
axes[2].set_title('Execution Speed Optimization')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
