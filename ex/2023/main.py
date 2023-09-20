animal = input()
count = 0;
for c in animal:
    if c =='a'or c =='e'or c =='i'or c =='o'or c =='u'or c =='A' or c =='E'or c =='I'or c =='O'or c =='U':
        count +=1;

print("frasco", count%3)