import numpy as np
import matplotlib.pyplot as plt
from math import comb, sqrt, pi, exp


# ============================================================
# 1. BASIC PROBABILITY USING A CONTINGENCY TABLE
# ============================================================

# Example:
# Customers can be:
# - Mobile or Desktop users
# - Purchased or Did not purchase

mobile_purchased = 30
mobile_not_purchased = 20
desktop_purchased = 20
desktop_not_purchased = 30

total = (
    mobile_purchased
    + mobile_not_purchased
    + desktop_purchased
    + desktop_not_purchased
)

# P(A): probability that a customer purchased
p_purchase = (mobile_purchased + desktop_purchased) / total

# P(A ∩ B): probability that customer is Mobile AND Purchased
p_mobile_and_purchase = mobile_purchased / total

# P(A | B): probability of Purchase given that customer is Mobile
p_purchase_given_mobile = mobile_purchased / (
    mobile_purchased + mobile_not_purchased
)

print("1. BASIC PROBABILITY")
print("--------------------")
print("P(Purchase) =", p_purchase)
print("P(Mobile AND Purchase) =", p_mobile_and_purchase)
print("P(Purchase | Mobile) =", p_purchase_given_mobile)


# ============================================================
# 2. NORMAL DISTRIBUTION
# ============================================================

mean = 100
standard_deviation = 15

x = np.linspace(
    mean - 4 * standard_deviation,
    mean + 4 * standard_deviation,
    500
)

y = (
    1 / (standard_deviation * np.sqrt(2 * np.pi))
    * np.exp(
        -0.5 * ((x - mean) / standard_deviation) ** 2
    )
)

plt.figure(figsize=(9, 5))
plt.plot(x, y)

plt.axvline(mean, linestyle="--", label="Mean")
plt.axvline(mean - standard_deviation, linestyle="--")
plt.axvline(mean + standard_deviation, linestyle="--")
plt.axvline(mean - 2 * standard_deviation, linestyle="--")
plt.axvline(mean + 2 * standard_deviation, linestyle="--")
plt.axvline(mean - 3 * standard_deviation, linestyle="--")
plt.axvline(mean + 3 * standard_deviation, linestyle="--")

plt.title("Normal Distribution — 68-95-99.7 Rule")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.legend()

plt.show()


print("\n2. 68-95-99.7 RULE")
print("------------------")
print("Within 1 standard deviation: approximately 68%")
print("Within 2 standard deviations: approximately 95%")
print("Within 3 standard deviations: approximately 99.7%")


# ============================================================
# 3. BINOMIAL DISTRIBUTION
# ============================================================

# Example:
# A customer has a 60% probability of making a purchase.
# We observe 10 customers.

n = 10
p = 0.60

successes = np.arange(0, n + 1)

probabilities = []

for k in successes:
    probability = (
        comb(n, k)
        * (p ** k)
        * ((1 - p) ** (n - k))
    )

    probabilities.append(probability)

plt.figure(figsize=(9, 5))
plt.bar(successes, probabilities)

plt.title("Binomial Distribution")
plt.xlabel("Number of Successful Purchases")
plt.ylabel("Probability")

plt.show()


# ============================================================
# 4. CENTRAL LIMIT THEOREM
# ============================================================

# Create a right-skewed population
population = np.random.exponential(
    scale=50,
    size=100000
)

sample_size = 30
number_of_samples = 1000

sample_means = []

for i in range(number_of_samples):

    sample = np.random.choice(
        population,
        size=sample_size
    )

    sample_means.append(np.mean(sample))


plt.figure(figsize=(9, 5))

plt.hist(
    sample_means,
    bins=30,
    edgecolor="black"
)

plt.title("Central Limit Theorem — Distribution of Sample Means")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")

plt.show()


print("\n4. CENTRAL LIMIT THEOREM")
print("------------------------")
print("Population shape: Right-skewed")
print("Sample size:", sample_size)
print("Number of samples:", number_of_samples)
print("Mean of sample means:", np.mean(sample_means))
print("Population mean:", np.mean(population))

print("\nThe Central Limit Theorem shows that")
print("the distribution of sample means becomes")
print("approximately normal as the number of samples increases.")


