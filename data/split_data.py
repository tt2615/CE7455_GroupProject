from random import shuffle
# file1=open("rawdata_web_crawler.txt", 'r', encoding='utf-8')
with open('rawdata_web_crawler.txt','r',encoding='utf-8') as file1:
    lines=file1.readlines()
    file1.close()
    abs_t = []
    abstracts = []
    titles = []
    i = 0
    for line in lines:
        if i % 3 == 0:
            titles.append(line)
        elif i % 3 == 1:
            abstracts.append(line)
        i += 1
    for i in range(len(abstracts)):
        if len(titles[i]) > 0 and len(abstracts[i]) > 0:
            h_a_pair = (titles[i], abstracts[i])
            abs_t.append(h_a_pair)
    shuffle(abs_t)
    total = len(abs_t)
    dev = total//10
    train  = total - dev - dev
    i = 0
with open('dev.dat','w',encoding='utf-8') as file1:
    for i in range(dev):
        file1.writelines(abs_t[i][0])
        file1.writelines(abs_t[i][1])
        file1.writelines("\n")
    file1.close()

with open('test.dat','w',encoding='utf-8') as file1:
    for i in range(dev, 2 * dev):
        file1.writelines(abs_t[i][0])
        file1.writelines(abs_t[i][1])
        file1.writelines("\n")
    file1.close()

with open('train.dat','w',encoding='utf-8') as file1:
    for i in range(2 * dev, total):
        file1.writelines(abs_t[i][0])
        file1.writelines(abs_t[i][1])
        file1.writelines("\n")
    file1.close()
