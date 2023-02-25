# Write your calculate_mean function here.
# Don't use in-built statistics module

def calculate_mean(fluxes):
  mean_fluxes = sum(fluxes)/len(fluxes)
  return mean_fluxes
    
    


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calculate_mean` function with examples:
  mean = calculate_mean([1,2.2,0.3,3.4,7.9])
  print(mean)
  
  mean = calculate_mean([1.2, 3.8, 2.2, 8.2, 7.1])
  print(mean)
  
  mean = calculate_mean([-1.2, -3.8, -2.2, -8.2, -7.1])
  print(mean)
  
