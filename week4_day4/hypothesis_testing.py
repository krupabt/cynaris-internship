import numpy as np
import pandas as pd
from scipy import stats


# =================================================
# WEEK 4 DAY 4 - HYPOTHESIS TESTING
# =================================================


# =================================================
# 1. FORMULATE HYPOTHESES FOR 3 BUSINESS SCENARIOS
# =================================================

print("=" * 60)
print("1. BUSINESS HYPOTHESES")
print("=" * 60)

print("\nScenario 1: New Marketing Campaign")
print("H0: The new marketing campaign does not change average sales.")
print("H1: The new marketing campaign changes average sales.")

print("\nScenario 2: Customer Satisfaction")
print("H0: The average customer satisfaction score is 4.0.")
print("H1: The average customer satisfaction score is different from 4.0.")

print("\nScenario 3: Two Sales Teams")
print("H0: The average sales of Team A and Team B are equal.")
print("H1: The average sales of Team A and Team B are different.")


# =================================================
# 2. ONE-SAMPLE T-TEST
# =================================================

print("\n" + "=" * 60)
print("2. ONE-SAMPLE T-TEST")
print("=" * 60)

# Monthly sales of a sample of employees
monthly_sales = np.array([
    51, 53, 49, 52, 55,
    54, 50, 56, 52, 51,
    53, 55, 54, 52, 50
])

# Business claim:
# Average monthly sales should be 50 units.

claimed_mean = 50

t_statistic, p_value = stats.ttest_1samp(
    monthly_sales,
    claimed_mean
)

print("Sample Mean:", np.mean(monthly_sales))
print("Claimed Mean:", claimed_mean)
print("T-statistic:", t_statistic)
print("P-value:", p_value)


# =================================================
# 3. 95% CONFIDENCE INTERVAL
# =================================================

confidence_level = 0.95

sample_mean = np.mean(monthly_sales)
sample_std = np.std(monthly_sales, ddof=1)
sample_size = len(monthly_sales)

standard_error = sample_std / np.sqrt(sample_size)

degrees_of_freedom = sample_size - 1

t_critical = stats.t.ppf(
    1 - (1 - confidence_level) / 2,
    degrees_of_freedom
)

margin_of_error = t_critical * standard_error

confidence_interval = (
    sample_mean - margin_of_error,
    sample_mean + margin_of_error
)

print("\n95% CONFIDENCE INTERVAL")
print("Lower Limit:", confidence_interval[0])
print("Upper Limit:", confidence_interval[1])


# =================================================
# 4. INTERPRET ONE-SAMPLE TEST
# =================================================

alpha = 0.05

print("\nONE-SAMPLE TEST INTERPRETATION")

if p_value < alpha:
    print("P-value is less than 0.05.")
    print("Reject the null hypothesis.")
    print("There is statistically significant evidence")
    print("that the average monthly sales is different from 50.")
else:
    print("P-value is greater than or equal to 0.05.")
    print("Fail to reject the null hypothesis.")
    print("There is not enough statistical evidence")
    print("to say that the average monthly sales is different from 50.")


# =================================================
# 5. TWO-SAMPLE T-TEST
# =================================================

print("\n" + "=" * 60)
print("3. TWO-SAMPLE T-TEST")
print("=" * 60)

# Sales data from two independent teams

team_a = np.array([
    42, 45, 47, 44, 46,
    48, 43, 45, 47, 46
])

team_b = np.array([
    50, 52, 48, 51, 53,
    49, 54, 50, 52, 51
])

print("Team A Mean:", np.mean(team_a))
print("Team B Mean:", np.mean(team_b))


# Welch's two-sample t-test
t_statistic_two, p_value_two = stats.ttest_ind(
    team_a,
    team_b,
    equal_var=False
)

print("T-statistic:", t_statistic_two)
print("P-value:", p_value_two)


# =================================================
# 6. CONFIDENCE INTERVAL FOR DIFFERENCE IN MEANS
# =================================================

mean_difference = np.mean(team_a) - np.mean(team_b)

standard_error_difference = np.sqrt(
    np.var(team_a, ddof=1) / len(team_a)
    +
    np.var(team_b, ddof=1) / len(team_b)
)

degrees_of_freedom_two = (
    (
        np.var(team_a, ddof=1) / len(team_a)
        +
        np.var(team_b, ddof=1) / len(team_b)
    ) ** 2
    /
    (
        (
            np.var(team_a, ddof=1) / len(team_a)
        ) ** 2 / (len(team_a) - 1)
        +
        (
            np.var(team_b, ddof=1) / len(team_b)
        ) ** 2 / (len(team_b) - 1)
    )
)

t_critical_two = stats.t.ppf(
    0.975,
    degrees_of_freedom_two
)

margin_of_error_two = (
    t_critical_two * standard_error_difference
)

confidence_interval_two = (
    mean_difference - margin_of_error_two,
    mean_difference + margin_of_error_two
)

print("\n95% CONFIDENCE INTERVAL FOR DIFFERENCE")
print("Lower Limit:", confidence_interval_two[0])
print("Upper Limit:", confidence_interval_two[1])


# =================================================
# 7. INTERPRET TWO-SAMPLE TEST
# =================================================

print("\nTWO-SAMPLE TEST INTERPRETATION")

if p_value_two < alpha:
    print("P-value is less than 0.05.")
    print("Reject the null hypothesis.")
    print("There is statistically significant evidence")
    print("that the average sales of Team A and Team B differ.")
else:
    print("P-value is greater than or equal to 0.05.")
    print("Fail to reject the null hypothesis.")
    print("There is not enough statistical evidence")
    print("to conclude that the team averages differ.")


# =================================================
# 8. TYPE I AND TYPE II ERRORS
# =================================================

print("\n" + "=" * 60)
print("4. TYPE I AND TYPE II ERRORS")
print("=" * 60)

print("\nType I Error:")
print("Rejecting the null hypothesis when it is actually true.")
print("Business example: A company concludes that a new")
print("marketing campaign increased sales when it actually did not.")

print("\nType II Error:")
print("Failing to reject the null hypothesis when it is actually false.")
print("Business example: A company concludes that a new")
print("marketing campaign did not improve sales when it actually did.")


# =================================================
# 9. FINAL SUMMARY
# =================================================

print("\n" + "=" * 60)
print("FINAL SUMMARY")
print("=" * 60)

print("Significance level (alpha):", alpha)

print("\nOne-sample t-test p-value:", p_value)

print("Two-sample t-test p-value:", p_value_two)

print("\nHypothesis testing helps businesses")
print("use statistical evidence to evaluate claims")
print("and make data-driven decisions.")
