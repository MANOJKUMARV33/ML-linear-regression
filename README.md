Linear Equation with one predictor variable will be in the form of Y = MX + C. In our process we need to identify "M" and "C".

M = Sum[(x-x')*(y-y')]/Sum[(x-x')^2]

Where x' and y' is mean of the x and y

Step1: Calculate the mean of both X and Y. Two alternative function are available we can use anyone

numpy.mean(): Here np.mean(x)
x.mean()


Step2: Calculate Sum of (x-x')*(y-y') and (x-x')^2 for all rows. Then calculate M

Step3: Find C substituting x_mean, y_mean and M value in linear equation

Step4: Drawing Regression line in the plot

Step5: Verification of model with Rsquare method R^2 = Sum(Yp-y')^2 / Sum (y-y')^2
