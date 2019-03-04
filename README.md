# ProblemSolvingUsingPython
Given String: abcdefghijklmnop.
Generate pattern in python:
abcd
defg
ghij
jklm
mnop
We first split the string accordingly ie abcd defg ghij jklm mnop, we observe that there are 5 splits taking place
for split 1 we may write as, str(split[0:4])
    split2                   str(split[3:7])
    split3                   str(split[6:10])
    split4                   str(split[9:13])
    split5                   str(split[12:16])
We can deduce it as str(split[i,j])
where i will iterate 5 times in range 0-16 with interval of 3 and j would be just j=i+4, but we should stop before i>=12 as it will give result:
abcd
defg
ghij
jklm
mnop
p   (extra iteration)

Thank You!

