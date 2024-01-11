
def letter_histogram(word):
  histogram = {}
  for l in word:
    if l in histogram:
      histogram[l] = histogram[l] + 1
    else:
      histogram[l] = 1
  return histogram

print(letter_histogram('abracadabrabarracuda'))
